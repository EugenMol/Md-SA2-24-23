from bson import ObjectId
from fastapi import HTTPException

from settings import meters_collection



async def get_document_by_id(_id: str):
    object_id = ObjectId(_id)
    metr_filter = {"_id": object_id}

    document = meters_collection.find_one(metr_filter)

    if document:
        document["_id"] = str(document["_id"])
        return document
    else:
        raise HTTPException(status_code=404, detail="Документ с указанным _id не найден")
