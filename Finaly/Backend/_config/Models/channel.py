from typing import List

from pydantic import BaseModel


class Channel(BaseModel):
    name: str
    type: str
    ip: str = ""
    port: str = ""
    serial_port: str = ""
    baud_rate: str = ""
    data_bits: str = ""
    parity: str = ""
    stop_bits: str = ""
    active: bool
    meters: List[dict] = []