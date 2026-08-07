from fastapi import APIRouter

from app.ai.scoring import analyze_username
from app.ai.schemas import AIRequest


router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post("/analyze")
def analyze(
    request: AIRequest
):

    result = analyze_username(
        request.username
    )

    return {
        "username": request.username,
        **result
    }
