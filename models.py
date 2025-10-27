from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int
    shortname: str
    description: str
    iscompleted: bool = Field(default = False)