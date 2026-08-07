from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_database

from app.search.models import SearchQuery
from app.search.schemas import (
    SearchRequest,
    SearchResponse
)

from app.search.service import (
    generate_candidates,
    normalize_username,
    validate_username
)

from app.search.enrichment import enrich_username
from app.search.checker import check_username

from app.limits.service import consume_search
from app.premium.models import PremiumSubscription


router = APIRouter(
    prefix="/search",
    tags=["Search"]
)


def check_premium(
    db: Session,
    telegram_id: str
):

    subscription = (
        db.query(PremiumSubscription)
        .filter(
            PremiumSubscription.telegram_id
            == telegram_id
        )
        .first()
    )

    return bool(
        subscription
        and subscription.active
    )


@router.post(
    "/",
    response_model=SearchResponse
)
def search_username(
    request: SearchRequest,
    db: Session = Depends(get_database)
):

    premium = check_premium(
        db,
        request.telegram_id
    )


    allowed, remaining = consume_search(
        db,
        request.telegram_id,
        premium
    )


    if not allowed:

        raise HTTPException(
            status_code=429,
            detail="Search limit reached"
        )


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

        check = check_username(
            username
        )

        analysis = enrich_username(
            username
        )


        results.append({
            **check,
            **analysis
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
        remaining_searches=remaining
    )
