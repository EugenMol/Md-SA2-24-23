from pydantic import BaseModel


class Group(BaseModel):
    group_name: str
