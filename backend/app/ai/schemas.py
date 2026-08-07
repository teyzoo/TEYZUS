from pydantic import BaseModel


class AIRequest(BaseModel):
    username: str


class AIResponse(BaseModel):
    username: str
    beauty: float
    readability: float
    rarity: float
    brand: float
    liquidity: float
    total: float
