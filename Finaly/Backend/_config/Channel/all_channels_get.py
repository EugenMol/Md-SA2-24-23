from fastapi import HTTPException, FastAPI
from fastapi.responses import JSONResponse
from bson import ObjectId
import json


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)


async def get_all_channels():
    from settings import channels_collection

    documents = channels_collection.find()
    result = []

    for document in documents:
        document["_id"] = str(document["_id"])
        result.append(document)

    if len(result) > 0:
        json_content = JSONEncoder().encode(result)
        return JSONResponse(content=json.loads(json_content), status_code=200)
    else:
        raise HTTPException(status_code=404, detail="Документы не найдены")
