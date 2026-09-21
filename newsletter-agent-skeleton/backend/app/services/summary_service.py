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
        prompt = f"""Act as a news analyst and summarise and analyse the following news headline data and produce a summary of each article. 
                Please highlight the most important insights. 
                For the headline section, you may just restate the headline provided by the article.
                For the summary, it should be two sentences maximum but give sufficient information on the content of the article.
                For the purpose, please highlight why the headline is important in the wider context,
                which can include past series of events. 
                For the url, simply provide the url to the article
                The news headline data is here: {article}"""

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