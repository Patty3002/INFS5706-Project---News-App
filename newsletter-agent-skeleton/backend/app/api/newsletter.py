from fastapi import APIRouter
import json

from app.services.news_service import get_top_headlines, remove_incomplete_articles, remove_duplicates

router = APIRouter(
    prefix="/api/v1",
    tags=["news"],
)

@router.get("/headlines")
def get_headlines(category="business"):
    articles = get_top_headlines(category)
    no_invalids = remove_incomplete_articles(articles)
    no_dups = remove_duplicates(no_invalids)
    return no_dups
