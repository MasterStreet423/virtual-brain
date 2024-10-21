from typing import Literal
import pydantic


class Dialog(pydantic.BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str
    