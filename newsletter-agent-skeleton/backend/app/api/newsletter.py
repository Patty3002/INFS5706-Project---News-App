from fastapi import APIRouter
import json

from app.services.news_service import get_top_headlines, remove_incomplete_articles, remove_duplicates, get_top_headlines_gnews
from app.services.summary_service import prep_summary, get_summary

router = APIRouter(
    prefix="/api/v1",
    tags=["news"],
)

@router.get("/headlines")
def get_headlines(category="business"):
    articles = get_top_headlines(category)
    no_invalids_newsapi = remove_incomplete_articles(articles)
    gnews_articles = get_top_headlines_gnews()
    no_invalids_gnews = remove_incomplete_articles(gnews_articles)
    no_invalids = no_invalids_newsapi + no_invalids_gnews
    no_dups = remove_duplicates(no_invalids)
    prep = prep_summary(no_dups)
    summary = get_summary(prep)
    return summary