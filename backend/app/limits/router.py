from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_database
from app.limits.service import get_search_limit


router = APIRouter(
    prefix="/limits",
    tags=["Limits"]
)


@router.get("/{telegram_id}")
def get_limits(
    telegram_id: str,
    premium: bool = False,
    db: Session = Depends(get_database)
):
    _, daily_limit, remaining = get_search_limit(
        db,
        telegram_id,
        premium
    )

    return {
        "telegram_id": telegram_id,
        "premium": premium,
        "daily_limit": daily_limit,
        "remaining": remaining
    }
