from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_database
from app.premium.models import PremiumSubscription
from app.premium.schemas import PremiumCreate


router = APIRouter(
    prefix="/premium",
    tags=["Premium"]
)


@router.get("/{telegram_id}")
def get_premium(
    telegram_id: str,
    db: Session = Depends(get_database)
):
    subscription = (
        db.query(PremiumSubscription)
        .filter(
            PremiumSubscription.telegram_id == telegram_id
        )
        .first()
    )

    if not subscription:
        return {
            "telegram_id": telegram_id,
            "active": False,
            "plan": "free"
        }

    return {
        "telegram_id": telegram_id,
        "active": subscription.active,
        "plan": subscription.plan,
        "started_at": subscription.started_at,
        "expires_at": subscription.expires_at
    }


@router.post("/")
def create_premium(
    premium: PremiumCreate,
    db: Session = Depends(get_database)
):
    existing = (
        db.query(PremiumSubscription)
        .filter(
            PremiumSubscription.telegram_id
            == premium.telegram_id
        )
        .first()
    )

    if existing:
        return {
            "status": "exists",
            "premium_id": existing.id
        }

    subscription = PremiumSubscription(
        telegram_id=premium.telegram_id,
        plan=premium.plan,
        active=False
    )

    db.add(subscription)
    db.commit()
    db.refresh(subscription)

    return {
        "status": "created",
        "premium_id": subscription.id,
        "active": False
    }
