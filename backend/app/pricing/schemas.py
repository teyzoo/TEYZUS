from pydantic import BaseModel


class PriceRequest(BaseModel):
    username: str
    ai_score: float | None = None


class PriceResponse(BaseModel):
    username: str
    min_price: float
    max_price: float
    category: str
