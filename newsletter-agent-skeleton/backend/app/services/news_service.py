import os
from dotenv import load_dotenv

import requests


NEWS_API_URL = "https://newsapi.org/v2/top-headlines"


def get_top_headlines(
    category,
    country = "us",
    page_size = 10,
):
    load_dotenv()
    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        raise ValueError("NEWS_API_KEY is not configured")

    parameters = {
        "apiKey": api_key,
        "category": category,
        "country": country,
        "pageSize": page_size,
    }

    response = requests.get(
        NEWS_API_URL,
        params=parameters,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()