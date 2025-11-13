from pydantic import BaseModel

class CaesarItem(BaseModel):
    text: str
    offset: int
    mode: str


class FenceToDecryptItem(BaseModel):
    text: str
