from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime, timezone


class Base(DeclarativeBase):
    pass


class ShortenedURL(Base):
    __tablename__ = "shortened_urls"

    id         = Column(Integer, primary_key=True, autoincrement=True)
    code       = Column(String(10), unique=True, nullable=False, index=True)
    long_url   = Column(String(2048), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    hit_count  = Column(Integer, default=0)


class ClickEvent(Base):
    __tablename__ = "click_events"

    id         = Column(Integer, primary_key=True, autoincrement=True)
    code       = Column(String(10), nullable=False, index=True)
    long_url   = Column(String(2048), nullable=False)
    clicked_at = Column(String(32), nullable=False)
