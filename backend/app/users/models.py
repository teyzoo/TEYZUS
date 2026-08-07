from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    telegram_id = Column(
        String,
        unique=True,
        index=True
    )

    username = Column(
        String,
        nullable=True
    )

    first_name = Column(
        String,
        nullable=True
    )

    language = Column(
        String,
        default="unknown"
    )

    premium = Column(
        Boolean,
        default=False
    )

    balance = Column(
        Integer,
        default=0
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
