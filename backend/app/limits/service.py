from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.limits.models import SearchLimit


FREE_DAILY_LIMIT = 3
PREMIUM_DAILY_LIMIT = 100


def get_search_limit(
    db: Session,
    telegram_id: str,
    premium: bool = False
):
    now = datetime.utcnow()

    limit = (
        db.query(SearchLimit)
        .filter(
            SearchLimit.telegram_id == telegram_id
        )
        .first()
    )

    if not limit:
        limit = SearchLimit(
            telegram_id=telegram_id,
            used=0,
            reset_at=now + timedelta(days=1)
        )

        db.add(limit)
        db.commit()
        db.refresh(limit)

    elif now >= limit.reset_at:
        limit.used = 0
        limit.reset_at = now + timedelta(days=1)

        db.commit()
        db.refresh(limit)

    daily_limit = (
        PREMIUM_DAILY_LIMIT
        if premium
        else FREE_DAILY_LIMIT
    )

    remaining = max(
        daily_limit - limit.used,
        0
    )

    return limit, daily_limit, remaining


def consume_search(
    db: Session,
    telegram_id: str,
    premium: bool = False
):
    limit, daily_limit, remaining = get_search_limit(
        db,
        telegram_id,
        premium
    )

    if remaining <= 0:
        return False, 0

    limit.used += 1

    db.commit()

    return True, daily_limit - limit.used
