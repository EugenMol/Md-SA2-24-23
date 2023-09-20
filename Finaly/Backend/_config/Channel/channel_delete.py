from bson import ObjectId
from fastapi import HTTPException


async def channel_remove(_id: str):
    from settings import channels_collection

    object_id = ObjectId(_id)

    filter_id = {"_id": object_id}
    result = channels_collection.delete_one(filter_id)

    if result.deleted_count > 0:
        return {"message": f"Документ  успешно удален"}
    else:
        raise HTTPException(status_code=404, detail="Документ с указанным _id не найден")