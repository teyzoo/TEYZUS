from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.limits.models import SearchLimit


FREE_DAILY_LIMIT = 5
PREMIUM_DAILY_LIMIT = None


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

    if premium:
        return limit, PREMIUM_DAILY_LIMIT, None

    remaining = max(
        FREE_DAILY_LIMIT - limit.used,
        0
    )

    return limit, FREE_DAILY_LIMIT, remaining


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

    if premium:
        limit.used += 1
        db.commit()

        return True, None

    if remaining <= 0:
        return False, 0

    limit.used += 1

    db.commit()

    return True, FREE_DAILY_LIMIT - limit.used
