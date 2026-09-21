import os
from google import genai
from google.genai import types
from pydantic import BaseModel
from dotenv import load_dotenv
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
    summary: str
    purpose: str
    url: str

def get_summary(articles):
    load_dotenv()
    gemini_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=gemini_key)
    responses = list()
    for article in articles:
        prompt = f"""You are a news analyst. You will be given a news article below. For each one, produce a structured briefing in exactly the format specified.

            The article is here: {article}

            For each article, output:

            **Headline:** Restate the headline exactly as provided.
            **Summary:** A maximum of two sentences covering the key facts (who, what, when/where, outcome), giving enough information that a reader understands the article without opening it.
            **Purpose:** 2-4 sentences explaining why this story matters in the wider context, including relevant background or prior events, with a little more depth. Lead with the single most important insight.
            **URL:** Copy the URL exactly as provided.

            Rules:
            - You should only summarise news articles. Please skip anything that is not a news article, such as cartoons or advertisements, or any irrelevant articles. You must include relevant articles.
            - Do not fabricate any information, or include any inappropriate information.
            - Base the Summary only on the content provided. If only a headline or snippet is available, keep the summary limited to what it supports and say so.
            - You should try your best to find the key facts, but if they are missing (for example there is no information on who), you may omit that specific key fact.
            - The summary should separate and attribute any speculations, opinions or claims from established facts
            - In Purpose, only reference background events you are confident about. If you are unsure, say so explicity rather than guessing.
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
                response_schema=HeadlineSummary,
            ),
        )
        responses.append(json.loads(response.text))

    return responses