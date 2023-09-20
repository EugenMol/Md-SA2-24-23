from bson import ObjectId
from fastapi import HTTPException


async def get_channel_by_id(_id: str):
    from settings import channels_collection
    object_id = ObjectId(_id)
    metr_filter = {"_id": object_id}

    document = channels_collection.find_one(metr_filter)

    if document:
        document["_id"] = str(document["_id"])
        return document
    else:
        raise HTTPException(status_code=404, detail="Документ с указанным _id не найден")
