from fastapi import HTTPException
from Models.channel import Channel


async def channel_add(data: Channel):
    from settings import channels_collection

    query = {
        "name": data.name,
        "address": f"{data.ip}:{data.port}"
    }

    existing_document = channels_collection.find_one(query)

    if existing_document:
        raise HTTPException(status_code=404, detail="Record with matching values already exists.")
    if data.type == 'TCP':
        result = {
            "name": data.name,
            "type": data.type,
            "ip": data.ip,
            "port": data.port,
            # "serial_port": data.serial_port,
            # "baud_rate": data.baud_rate,
            # "data_bits": data.data_bits,
            # "parity": data.parity,
            # "stop_bits": data.stop_bits,
            "active": 1 if data.active else 0,
        }

        inserted_result = channels_collection.insert_one(result)
        result["_id"] = str(inserted_result.inserted_id)
        return result
    elif data.type == 'COM':
        result = {
            "name": data.name,
            "type": data.type,
            # "ip": data.ip,
            # "port": data.port,
            "serial_port": data.serial_port,
            "baud_rate": data.baud_rate,
            "data_bits": data.data_bits,
            # "parity": data.parity,
            "stop_bits": data.stop_bits,
            "active": 1 if data.active else 0,
        }
        inserted_result = channels_collection.insert_one(result)
        result["_id"] = str(inserted_result.inserted_id)
        return result
