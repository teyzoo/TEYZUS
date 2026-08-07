from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database import Base


class SearchQuery(Base):
    __tablename__ = "search_queries"

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

    query = Column(
        String,
        nullable=False,
        index=True
    )

    results_count = Column(
        Integer,
        default=0,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
