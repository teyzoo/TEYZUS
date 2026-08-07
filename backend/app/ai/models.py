from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from app.database import Base


class UsernameAIAnalysis(Base):
    __tablename__ = "username_ai_analysis"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        nullable=False,
        index=True
    )

    beauty_score = Column(
        Float,
        default=0
    )

    readability_score = Column(
        Float,
        default=0
    )

    rarity_score = Column(
        Float,
        default=0
    )

    brand_score = Column(
        Float,
        default=0
    )

    liquidity_score = Column(
        Float,
        default=0
    )

    total_score = Column(
        Float,
        default=0
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
