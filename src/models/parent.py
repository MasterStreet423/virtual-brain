import pydantic

class Parent(pydantic.BaseModel):
    name: str
    relationship: str