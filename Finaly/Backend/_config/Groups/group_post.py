from fastapi import HTTPException

from Models.group import Group


async def group_add(data: Group):
    from settings import groups_collection

    query = {
        "group_name": data.group_name,
    }

    existing_document = groups_collection.find_one(query)

    if existing_document:
        raise HTTPException(status_code=404, detail="Record with matching values already exists.")

    result = {
        "group_name": data.group_name,

    }

    inserted_result = groups_collection.insert_one(result)
    result["_id"] = str(inserted_result.inserted_id)

    return result
