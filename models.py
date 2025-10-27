from pydantic import BaseModel, Field

class Task(BaseModel):
    shortname: str
    description: str
    iscompleted: bool = Field(default = False)