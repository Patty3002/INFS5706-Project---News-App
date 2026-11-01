import os
from dotenv import load_dotenv
import math
import requests
import json
import streamlit as st

load_dotenv()
gnews_key = st.secrets["GNEWS_API_KEY"]
guardian_key = st.secrets["GUARDIAN_API_KEY"]

NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
GNEWS_API_URL = f"https://gnews.io/api/v4/top-headlines?category=general&lang=en&country=us&max=10&&apikey={gnews_key}"
GUARDIAN_API_URL = f"https://content.guardianapis.com/search?api-key={guardian_key}"


# Gets the top headline for each category, country and page size,
# returning the result as JSON. For the prototype, the country ]
# will be the US (only option in NewsAPI)

# Source: NewsAPI

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

# Removes articles that do not have a title, url, or description
def remove_incomplete_articles(articles):
    valid_articles = list()

    for article in articles["articles"]:

        if not article["title"] or not article["url"] or not article["description"]:
            continue

        valid_articles.append(article)

    return valid_articles

# Remove duplicate articles, ensuring that the list given to the user
# does not contain repeat articles
def remove_duplicates(json_array):
    unique_articles = list()
    urls = set()
    titles = set()

    for article in json_array:
        url = article["url"]
        title = article["title"].strip().lower()

        if url in urls or title in titles:
            continue

        urls.add(url)
        titles.add(url)
        unique_articles.append(article)

    return unique_articles

# Removes similar articles, which is done via a 
# sentence transformer model. The model is trained using NLP,
# calculating embeddings and returning a similarity score


def normalise_score(score):
    shift = (score + 1) / 2
    skew = math.sqrt(shift)
    return round(skew * 100, 2)
"""
def remove_similar_articles(articles):
    model = SentenceTransformer('all-MiniLM-L6-v2')

    temp_articles = articles.copy()
    
    for i in range(len(temp_articles)):
        title1 = temp_articles[i]["title"]
        for j in range(i + 1, len(temp_articles)):
            title2 = temp_articles[j]["title"]

            embedding1 = model.encode(title1, convert_to_tensor=True)
            embedding2 = model.encode(title2, convert_to_tensor=True)

            similarity = util.cos_sim(embedding1, embedding2)
    
    embeddings = model.encode(temp_articles, convert_to_tensor=True)
    similarity_matrix = util.cos_sim(embeddings, embeddings)
    for i in range(len(temp_articles)):
        for j in range(i + 1, len(temp_articles)):
            raw_score = similarity_matrix[i][j].item()
            final_score = normalise_score(raw_score)
            if final_score > 80:
                articles.remove(temp_articles[j])

    return articles
"""
# Gets a response from the GNews API
def get_top_headlines_gnews():
    response = requests.get(
        GNEWS_API_URL,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()

def get_headlines_guardian():
    response = requests.get(
        GUARDIAN_API_URL,
        timeout=10
    )

    response.raise_for_status()
    
    result = response.json()
    result["articles"] = result.pop("results")
    return result

def process_guardian(result):
    articles = result["articles"]
    for article in articles:
        response = requests.get(
            article["apiurl"]
        )