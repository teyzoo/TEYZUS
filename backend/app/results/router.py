from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_database
from app.results.models import UsernameResult
from app.results.schemas import ResultCreate


router = APIRouter(
    prefix="/results",
    tags=["Results"]
)


@router.post("/")
def create_result(
    result: ResultCreate,
    db: Session = Depends(get_database)
):

    new_result = UsernameResult(
        telegram_id=result.telegram_id,
        username=result.username,
        status=result.status,
        ai_score=result.ai_score,
        price_min=result.price_min,
        price_max=result.price_max
    )


    db.add(new_result)
    db.commit()
    db.refresh(new_result)


    return {
        "status": "saved",
        "id": new_result.id
    }


@router.get("/{telegram_id}")
def history(
    telegram_id: str,
    db: Session = Depends(get_database)
):

    results = (
        db.query(UsernameResult)
        .filter(
            UsernameResult.telegram_id
            == telegram_id
        )
        .all()
    )


    return results
