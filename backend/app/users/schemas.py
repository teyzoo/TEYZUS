from pydantic import BaseModel


class UserCreate(BaseModel):

    telegram_id: str
    username: str | None = None
    first_name: str | None = None
    language: str = "unknown"
