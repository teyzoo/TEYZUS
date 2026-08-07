from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    telegram_id: str
    query: str = Field(min_length=1, max_length=32)


class SearchResult(BaseModel):
    username: str
    available: bool | None = None
    status: str
    ai_score: float | None = None
    estimated_price_min: float | None = None
    estimated_price_max: float | None = None


class SearchResponse(BaseModel):
    query: str
    normalized_query: str
    results: list[SearchResult]
    remaining_searches: int | None = None
