from bson import ObjectId
from fastapi import HTTPException

from settings import db


async def group_remove(_id: str):
    from settings import groups_collection
    from settings import meters_collection
    from settings import channels_collection
    object_id = ObjectId(_id)
    filter_id = {"_id": object_id}
    document = groups_collection.find_one({'_id': object_id})

    if document:
        group_name = document.get('group_name')
        collection_list = db.list_collection_names()
        if 'meters_collection' in collection_list:
            meters_collection.update_many({}, {'$pull': {'group_name': group_name}})
            target_group_id = ObjectId(object_id)
            channels_collection.update_many({}, {'$pull': {'meters.$[].groups': target_group_id}})

    result = groups_collection.delete_one(filter_id)
    if result.deleted_count > 0:
        return {"message": f"Документ  успешно удален"}
    else:
        raise HTTPException(status_code=404, detail="Документ с указанным _id не найден")
