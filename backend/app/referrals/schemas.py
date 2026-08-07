from pydantic import BaseModel


class ReferralCreate(BaseModel):
    referrer_telegram_id: str
    referred_telegram_id: str
    source: str | None = None
