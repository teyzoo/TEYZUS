from pydantic import BaseModel


class PremiumCreate(BaseModel):
    telegram_id: str
    plan: str = "monthly"
