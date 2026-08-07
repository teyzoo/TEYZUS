from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_database
from app.search.models import SearchQuery
from app.search.schemas import SearchRequest, SearchResponse
from app.search.service import (
    generate_candidates,
    normalize_username,
    validate_username
)


router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


@router.post(
    "/",
    response_model=SearchResponse
)
def search_username(
    request: SearchRequest,
    db: Session = Depends(get_database)
):
    normalized = normalize_username(
        request.query
    )

    if not validate_username(normalized):
        raise HTTPException(
            status_code=400,
            detail="Invalid username format"
        )

    candidates = generate_candidates(
        normalized
    )

    results = []

    for username in candidates:
        results.append({
            "username": username,
            "available": None,
            "status": "pending_check",
            "ai_score": None,
            "estimated_price_min": None,
            "estimated_price_max": None
        })

    search_record = SearchQuery(
        telegram_id=request.telegram_id,
        query=normalized,
        results_count=len(results)
    )

    db.add(search_record)
    db.commit()

    return SearchResponse(
        query=request.query,
        normalized_query=normalized,
        results=results,
        remaining_searches=None
    )
