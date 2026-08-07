from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_database
from app.users.models import User
from app.users.schemas import UserCreate


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_database)
):

    existing_user = (
        db.query(User)
        .filter(
            User.telegram_id == user.telegram_id
        )
        .first()
    )


    if existing_user:

        return {
            "status": "exists",
            "user_id": existing_user.id
        }


    new_user = User(
        telegram_id=user.telegram_id,
        username=user.username,
        first_name=user.first_name,
        language=user.language
    )


    db.add(new_user)
    db.commit()
    db.refresh(new_user)


    return {
        "status": "created",
        "user_id": new_user.id
    }


@router.get("/{telegram_id}")
def get_user(
    telegram_id: str,
    db: Session = Depends(get_database)
):

    user = (
        db.query(User)
        .filter(
            User.telegram_id == telegram_id
        )
        .first()
    )


    if not user:

        return {
            "status": "not_found"
        }


    return {
        "id": user.id,
        "telegram_id": user.telegram_id,
        "username": user.username,
        "first_name": user.first_name,
        "premium": user.premium,
        "balance": user.balance
    }
