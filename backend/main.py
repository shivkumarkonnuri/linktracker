import random
import string
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from prometheus_fastapi_instrumentator import Instrumentator

from database import get_db, init_db
from models import ShortenedURL
from schemas import ShortenRequest, ShortenResponse, StatsResponse
from redis_client import get_redis

app = FastAPI(title="LinkTracker", version="1.0.0")

Instrumentator().instrument(app).expose(app)

@app.on_event("startup")
def on_startup():
    init_db()

def generate_code(length: int = 6) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# ── GET /health ── must be above /{code} wildcard ─────────────
@app.get("/health")
def health():
    return {"status": "ok"}

# ── POST /shorten ──────────────────────────────────────────────
@app.post("/shorten", response_model=ShortenResponse, status_code=201)
async def shorten_url(
    body: ShortenRequest,
    db: Session = Depends(get_db),
    r=Depends(get_redis),
):
    long_url = str(body.url)

    for _ in range(5):
        code = generate_code()
        if not db.query(ShortenedURL).filter_by(code=code).first():
            break
    else:
        raise HTTPException(status_code=500, detail="Could not generate unique code")

    record = ShortenedURL(code=code, long_url=long_url)
    db.add(record)
    db.commit()

    await r.setex(f"url:{code}", 604800, long_url)

    return ShortenResponse(
        code=code,
        short_url=f"http://localhost/s/{code}",
        long_url=long_url,
    )

# ── GET /stats/{code} ── must be above /{code} wildcard ───────
@app.get("/stats/{code}", response_model=StatsResponse)
def get_stats(code: str, db: Session = Depends(get_db)):
    record = db.query(ShortenedURL).filter_by(code=code).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not found")
    return record

# ── GET /{code} ── wildcard — must be last ─────────────────────
@app.get("/s/{code}")
async def redirect(
    code: str,
    db: Session = Depends(get_db),
    r=Depends(get_redis),
):
    long_url = await r.get(f"url:{code}")

    if not long_url:
        record = db.query(ShortenedURL).filter_by(code=code).first()
        if not record:
            raise HTTPException(status_code=404, detail="Short URL not found")
        long_url = record.long_url
        await r.setex(f"url:{code}", 604800, long_url)

    await r.publish("clicks", f"{code}|{long_url}")

    db.query(ShortenedURL).filter_by(code=code).update(
        {"hit_count": ShortenedURL.hit_count + 1}
    )
    db.commit()

    return RedirectResponse(url=long_url, status_code=301)
