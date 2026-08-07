from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database import Base


class SearchLimit(Base):
    __tablename__ = "search_limits"

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

    used = Column(
        Integer,
        default=0,
        nullable=False
    )

    reset_at = Column(
        DateTime,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
