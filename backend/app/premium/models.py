from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

from app.database import Base


class PremiumSubscription(Base):
    __tablename__ = "premium_subscriptions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    telegram_id = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    active = Column(
        Boolean,
        default=False
    )

    plan = Column(
        String,
        default="free"
    )

    started_at = Column(
        DateTime,
        nullable=True
    )

    expires_at = Column(
        DateTime,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
