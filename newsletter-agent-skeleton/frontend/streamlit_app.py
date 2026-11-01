import streamlit as st
import requests

API_URL = "http://localhost:8000/api/v1/headlines"

st.set_page_config(
    page_title="Daily Newsletter",
    page_icon="📰"
)

st.title("📰 Daily Newsletter")
st.write("Welcome to your daily newsletter! Let's get started.")
st.write("""Note: Human on the loop required!
            This app uses AI. The AI is brilliant, but it sometimes sees things that aren’t there. 
            If it tells you a penguin invented the stock market, please fact-check before investing. 🐧🤔
            AI responses may be inaccurate. Please read all articles of interest to fact-check. 
        """
)
st.write("For more information about Human in the Loop practices, check out this website: (https://hai.stanford.edu/ai-definitions/what-is-human-in-the-loop)")

try:
    response = requests.get(
        API_URL,
        timeout=90
    )

    response.raise_for_status()

    articles = response.json()

    for i, article in enumerate(articles, start=1):
        with st.container(border=True):
            st.caption(f"Story {i} - {article["category"]}")
            
            st.subheader(article["headline"])

            st.write("### Summary")
            st.write(article["summary"])

            st.write("### Why this matters")
            st.write(article["purpose"])

            st.link_button(
                "Read original article",
                article["url"]
            )
except requests.exceptions.RequestException as error:
    st.error(f"Could not connect to the backend: {error}")