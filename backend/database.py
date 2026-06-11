from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://linktracker:linktracker@localhost:5432/linktracker"
    redis_url: str    = "redis://localhost:6379/0"
    base_url: str     = "http://localhost:8000"
    env: str          = "dev"

    class Config:
        env_file = ".env"
        extra = "ignore"   # silently ignore any .env keys not declared here


settings = Settings()

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def init_db():
    """Create tables if they don't exist. Called on app startup."""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Dependency injected into FastAPI route handlers."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
