from pydantic import BaseModel, HttpUrl
from datetime import datetime

class ShortenRequest(BaseModel):
    url: HttpUrl

class ShortenResponse(BaseModel):
    code: str
    short_url: str
    long_url: str

class StatsResponse(BaseModel):
    code: str
    long_url: str
    hit_count: int
    created_at: datetime
