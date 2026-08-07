from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_database
from app.referrals.models import Referral
from app.referrals.schemas import ReferralCreate


router = APIRouter(
    prefix="/referrals",
    tags=["Referrals"]
)


@router.post("/")
def create_referral(
    referral: ReferralCreate,
    db: Session = Depends(get_database)
):
    existing = (
        db.query(Referral)
        .filter(
            Referral.referred_telegram_id
            == referral.referred_telegram_id
        )
        .first()
    )

    if existing:
        return {
            "status": "exists",
            "referral_id": existing.id
        }

    new_referral = Referral(
        referrer_telegram_id=referral.referrer_telegram_id,
        referred_telegram_id=referral.referred_telegram_id,
        source=referral.source
    )

    db.add(new_referral)
    db.commit()
    db.refresh(new_referral)

    return {
        "status": "created",
        "referral_id": new_referral.id
    }


@router.get("/{telegram_id}")
def get_referrals(
    telegram_id: str,
    db: Session = Depends(get_database)
):
    referrals = (
        db.query(Referral)
        .filter(
            Referral.referrer_telegram_id == telegram_id
        )
        .all()
    )

    return {
        "telegram_id": telegram_id,
        "count": len(referrals)
    }
