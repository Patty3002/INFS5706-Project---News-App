import os
from google import genai
from google.genai import types
from pydantic import BaseModel
from dotenv import load_dotenv
from typing import List
import json

# Extracts the title, description, content and url from each article
def prep_summary(articles):
    res = list()
    for article in articles:
        res.append({
            "title": article["title"],
            "description": article["description"],
            "content": article["content"],
            "url": article["url"]
        })
    return res

class HeadlineSummary(BaseModel):
    headline: str
    category: str
    summary: str
    purpose: str
    url: str

class BatchResponse(BaseModel):
    articles: List[HeadlineSummary]

def get_summary(articles):
    load_dotenv()
    gemini_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=gemini_key)
    responses = list()
    for i in range(0, len(articles), 4):
        article_input = articles[i:i+4]
        prompt = f"""You are a news analyst. You will be given up to four news articles below. For each individual news article, produce a structured briefing in exactly the format specified.

            The articles are here: {article_input}

            For each article, output:

            **Headline:** Restate the headline exactly as provided.
            **Category:** You should assign a category to the article based on its content into the following categories: Business (all business news), World (News from any country that is not Australia), Australia, Technology, Politics, Law, Science, Sport, Entertainment
            **Summary:** A maximum of two sentences covering the key facts (who, what, when/where, outcome), giving enough information that a reader understands the article without opening it.
            **Purpose:** 2-4 sentences explaining why this story matters in the wider context, including relevant background or prior events, with a little more depth. Lead with the single most important insight.
            **URL:** Copy the URL exactly as provided.

            At the end, you should have up to four sections, each containing a headline, summary, purpose and URL.

            Rules:
            - You should only summarise news articles. Please skip anything that is not a news article, such as cartoons or advertisements, or any irrelevant articles. You must include relevant articles.
            - Do not fabricate any information, or include any inappropriate information.
            - News articles must have at least one and at most two categories. You should assign each article an appropriate category
            - Base the Summary only on the content provided. If only a headline or snippet is available, keep the summary limited to what it supports and say so.
            - You should try your best to find the key facts, but if they are missing (for example there is no information on who), you may omit that specific key fact.
            - The summary should separate and attribute any speculations, opinions or claims from established facts
            - In Purpose, only reference background events you are confident about. If you are unsure, say so explicitly rather than guessing.
            - Never invent or alter a URL. If none is provided, write "Not provided".
            - Keep the original article order.
            - Use a neutral, factual tone. Try your best not to be biased
            - Do not use phrases such as 'This article, this provided text, according to this text". Keep it professional.

        """

        response = client.models.generate_content(
            model='gemini-3.5-flash-lite',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=BatchResponse,
            ),
        )

        batch_result = json.loads(response.text)

        responses.extend(batch_result["articles"])

    return responses