
from fastapi import HTTPException


async def get_all_groups():
    from settings import groups_collection
    documents = groups_collection.find()
    result = []

    for document in documents:
        document["_id"] = str(document["_id"])
        result.append(document)

    if len(result) > 0:
        return result
    else:
        raise HTTPException(status_code=404, detail="Документы не найдены")