from pydantic import BaseModel


class ResultCreate(BaseModel):

    telegram_id: str
    username: str
    status: str = "unknown"

    ai_score: float | None = None

    price_min: float | None = None

    price_max: float | None = None
