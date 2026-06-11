import asyncio
import logging
import os
from datetime import datetime, timezone

import redis.asyncio as redis
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [WORKER] %(levelname)s %(message)s"
)
log = logging.getLogger(__name__)

REDIS_URL    = os.getenv("REDIS_URL", "redis://localhost:6379/0")
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://linktracker:linktracker@localhost:5432/linktracker")

# Sync SQLAlchemy engine (worker is I/O-light, sync is fine here)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

async def process_click(message: str):
    """
    message format: "code|long_url"
    Logs the click and persists a timestamped record to the DB.
    """
    try:
        parts = message.split("|", 1)
        if len(parts) != 2:
            log.warning("Malformed message: %s", message)
            return

        code, long_url = parts
        clicked_at = datetime.now(timezone.utc).isoformat()

        log.info("Click recorded — code=%s url=%s at=%s", code, long_url, clicked_at)

        # Persist click event to DB for audit trail
        with SessionLocal() as db:
            db.execute(
                text("""
                    INSERT INTO click_events (code, long_url, clicked_at)
                    VALUES (:code, :long_url, :clicked_at)
                    ON CONFLICT DO NOTHING
                """),
                {"code": code, "long_url": long_url, "clicked_at": clicked_at}
            )
            db.commit()

    except Exception as e:
        log.error("Failed to process click: %s", e)

async def main():
    log.info("Worker starting — connecting to Redis at %s", REDIS_URL)

    r = redis.Redis.from_url(REDIS_URL, decode_responses=True)
    pubsub = r.pubsub()
    await pubsub.subscribe("clicks")

    log.info("Subscribed to 'clicks' channel — waiting for events...")

    async for message in pubsub.listen():
        if message["type"] == "message":
            await process_click(message["data"])

if __name__ == "__main__":
    asyncio.run(main())
