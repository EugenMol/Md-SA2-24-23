from fastapi import HTTPException
from Models.meter import Meter
from settings import meters_collection, channels_collection, groups_collection


async def meter_add(data: Meter):
    query = {
        "meter_name": data.meter_name,
        "physical_address": data.physical_address,
        "meter_serial": data.meter_serial,
    }

    existing_document = meters_collection.find_one(query)

    if existing_document:
        raise HTTPException(status_code=404, detail="Record with matching values already exists.")

    all_documents = meters_collection.find({}, {"vm_id": 1}).sort("vm_id")
    existing_vm_ids = [doc["vm_id"] for doc in all_documents]
    next_vm_id = 1

    for vm_id in existing_vm_ids:
        if vm_id == next_vm_id:
            next_vm_id += 1
        else:
            break

    result = {
        "meter_name": data.meter_name,
        "meter_serial": data.meter_serial,
        "channel_name": data.channel_name,
        "group_name": data.group_name,
        "vm_id": next_vm_id,
        "active": 1 if data.active else 0,
        "physical_address": data.physical_address,
        "protocol_name": data.protocol_name,
        "ki": data.ki,
        "ku": data.ku,
    }

    inserted_result = meters_collection.insert_one(result)
    result["_id"] = str(inserted_result.inserted_id)

    new_meter = {
        "vm_id": next_vm_id,
        "physical_address": data.physical_address,
        "protocol_name": data.protocol_name,
        "ki": data.ki,
        "ku": data.ku,
        "groups": []
    }

    for group_name in data.group_name:
        existing_group = groups_collection.find_one({"group_name": group_name})
        group_id = existing_group["_id"]

        if existing_group:
            groups_collection.update_one(
                {"group_name": group_name},
                {"$push": {"vm_id": new_meter["vm_id"]}}
            )

            new_meter["groups"].append(group_id)
        else:
            pass

    existing_channel = channels_collection.find_one({"name": data.channel_name})

    if existing_channel:
        channels_collection.update_one(
            {"name": data.channel_name},
            {"$push": {"meters": new_meter}}
        )
    return result
