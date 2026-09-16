from fastapi import APIRouter

from app.services.news_service import get_top_headlines

router = APIRouter(
    prefix="/api/v1",
    tags=["news"],
)

@router.get("/headlines")
def get_headlines(category="business"):
    return get_top_headlines(category)