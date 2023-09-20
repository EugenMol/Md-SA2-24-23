from bson import ObjectId
from fastapi import HTTPException


async def channel_update(_id: str, name: str = None, type: str = None, ip: str = None,
                         port: str = None,
                         serial_port: str = None, baud_rate: str = None,
                         data_bits: str = None, parity: str = None, stop_bits: str = None, active: bool = None):
    from settings import channels_collection
    object_id = ObjectId(_id)
    meter_filter = {"_id": object_id}
    update_fields = {}
    if name is not None:
        update_fields["name"] = name
    if type is not None:
        update_fields["type"] = type
    if ip is not None:
        update_fields["ip"] = ip
    if port is not None:
        update_fields["port"] = port
    if serial_port is not None:
        update_fields["serial_port"] = serial_port
    if baud_rate is not None:
        update_fields["baud_rate"] = baud_rate
    if data_bits is not None:
        update_fields["data_bits"] = data_bits
    if parity is not None:
        update_fields["parity"] = parity
    if stop_bits is not None:
        update_fields["stop_bits"] = stop_bits
    if active is not None:
        update_fields["active"] = active
    if not update_fields:
        raise HTTPException(status_code=400, detail="Не указаны поля для обновления")

    update = {"$set": update_fields}
    result = channels_collection.update_one(meter_filter, update)

    if result.modified_count > 0:
        return {"message": f"Документ успешно обновлен"}
    else:
        raise HTTPException(status_code=404, detail="Отсуствуют новые данные")
