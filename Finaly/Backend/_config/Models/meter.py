from typing import List

from pydantic import BaseModel


class Meter(BaseModel):
    meter_name: str
    meter_serial: str
    channel_name: str
    group_name: List[str] = []
    physical_address: int
    protocol_name: str
    ki: int
    ku: int
    active: bool
