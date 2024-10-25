import pydantic
from typing import Literal

class ResponseFormat(pydantic.BaseModel):
    # needTalk: bool
    action: Literal["remember", "add_acquaintance","leave","none"]
    action_data: str
    respuesta: str
    emocion_actual: str
