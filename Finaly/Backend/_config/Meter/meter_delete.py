from bson import ObjectId
from fastapi import HTTPException


async def meter_remove(_id: str):
    from settings import meters_collection, groups_collection, channels_collection

    object_id = ObjectId(_id)

    filter_id = {"_id": object_id}
    document = meters_collection.find_one({'_id': object_id})

    if document:
        group_name = document.get('vm_id')
        groups_collection.update_many({}, {'$pull': {'vm_id': group_name}})
        channels_collection.update_many({},{'$pull': {'meters': {'vm_id': group_name}}})
    result = meters_collection.delete_one(filter_id)

    if result.deleted_count > 0:
        return {"message": f"Документ  успешно удален"}
    else:
        raise HTTPException(status_code=404, detail="Документ с указанным _id не найден")
