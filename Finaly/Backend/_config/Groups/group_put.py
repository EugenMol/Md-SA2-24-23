from bson import ObjectId
from fastapi import HTTPException

from settings import meters_collection


async def group_update(_id: str, group_name: str):
    from settings import groups_collection
    object_id = ObjectId(_id)
    meter_filter = {"_id": object_id}
    document = groups_collection.find_one({'_id': object_id})
    if document:
        grname = document.get('group_name')
        update_result = meters_collection.update_many(
            {'group_name': grname},
            {'$set': {'group_name.$': group_name}}
        )

    update_fields = {}
    update_fields["group_name"] = group_name

    if not update_fields:
        raise HTTPException(status_code=400, detail="Не указаны поля для обновления")

    update = {"$set": update_fields}
    result = groups_collection.update_one(meter_filter, update)

    if result.modified_count > 0:
        return {"message": f"Документ успешно обновлен"}
    else:
        raise HTTPException(status_code=404, detail="Отсуствуют новые данные")
