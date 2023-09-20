from typing import List

from bson import ObjectId
from fastapi import HTTPException


async def meter_update(_id: str, meter_name: str = None, meter_serial: str = None,
                       physical_address: int = None,
                       protocol_name: str = None, ki: int = None,
                       ku: int = None, active: bool = None):
    from settings import meters_collection
    object_id = ObjectId(_id)
    meter_filter = {"_id": object_id}
    update_fields = {}
    if meter_name is not None:
        update_fields["meter_name"] = meter_name
    if meter_serial is not None:
        update_fields["meter_serial"] = meter_serial
    if physical_address is not None:
        update_fields["physical_address"] = physical_address
    if protocol_name is not None:
        update_fields["protocol_name"] = protocol_name
    if ki is not None:
        update_fields["ki"] = ki
    if ku is not None:
        update_fields["ku"] = ku
    if active is not None:
        update_fields["active"] = active
    if not update_fields:
        raise HTTPException(status_code=400, detail="Не указаны поля для обновления")

    update = {"$set": update_fields}
    result = meters_collection.update_one(meter_filter, update)

    if result.modified_count > 0:
        return {"message": f"Документ успешно обновлен"}
    else:
        raise HTTPException(status_code=404, detail="Отсуствуют новые данные")

