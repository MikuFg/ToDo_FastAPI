from pydantic import BaseModel

class Task(BaseModel):
    id: int
    shortname: str
    description: str
    iscompleted: bool = False