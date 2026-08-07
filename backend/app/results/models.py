from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from app.database import Base


class UsernameResult(Base):

    __tablename__ = "username_results"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    telegram_id = Column(
        String,
        nullable=False,
        index=True
    )


    username = Column(
        String,
        nullable=False,
        index=True
    )


    status = Column(
        String,
        default="unknown"
    )


    ai_score = Column(
        Float,
        nullable=True
    )


    price_min = Column(
        Float,
        nullable=True
    )


    price_max = Column(
        Float,
        nullable=True
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
