from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from app.database import Base


class Referral(Base):
    __tablename__ = "referrals"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    referrer_telegram_id = Column(
        String,
        nullable=False,
        index=True
    )

    referred_telegram_id = Column(
        String,
        unique=True,
        nullable=False,
        index=True
    )

    source = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
