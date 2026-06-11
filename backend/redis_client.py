import redis.asyncio as redis
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    redis_url: str    = "redis://localhost:6379/0"
    database_url: str = "postgresql://linktracker:linktracker@localhost:5432/linktracker"
    base_url: str     = "http://localhost:8000"
    env: str          = "dev"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()

redis_pool = redis.ConnectionPool.from_url(
    settings.redis_url,
    decode_responses=True
)


def get_redis() -> redis.Redis:
    return redis.Redis(connection_pool=redis_pool)
