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
            This app uses AI to turn messy headlines into neat summaries. Please make sure that you
            cross-check and read articles of interest to confirm that all information is accurate. 
        """
)

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