from fastapi import APIRouter

from app.pricing.estimator import estimate_price
from app.pricing.schemas import PriceRequest


router = APIRouter(
    prefix="/pricing",
    tags=["Pricing"]
)


@router.post("/estimate")
def price_estimate(
    request: PriceRequest
):

    result = estimate_price(
        request.username,
        request.ai_score
    )

    return {
        "username": request.username,
        **result
    }
