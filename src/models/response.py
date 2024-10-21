import pydantic


class ResponseFormat(pydantic.BaseModel):
    # needTalk: bool
    necesita_recordar: bool
    para_recordar: str
    mensaje: str
    emocion_actual: str
