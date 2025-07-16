# app.py

import streamlit as st
import requests
import random
import time
from bs4 import BeautifulSoup
from datetime import datetime

# --------- Page Config ---------
st.set_page_config(page_title="Trend Finder", page_icon="🔍", layout="centered")

# --------- Custom CSS ---------
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --------- App Title ---------
st.markdown("<h1 class='main-title'>🔥 Trend Finder Tool</h1>", unsafe_allow_html=True)
st.markdown("Find the latest trending keywords by niche and platform.", unsafe_allow_html=True)

# --------- Dropdowns ---------
platform = st.selectbox("Choose a platform:", ["YouTube", "Pinterest", "Google Trends"])
niche = st.selectbox("Choose a niche:", ["Animals", "Fashion", "Technology", "Fitness", "Food", "Gaming", "Education", "Health", "Business", "DIY"])

# --------- Action Buttons ---------
col1, col2 = st.columns(2)
find_btn = col1.button("🔍 Find Keywords")
download_btn = col2.button("⬇️ Download Result")

# --------- Result Box ---------
result_box = st.empty()
adsterra_url = "https://your-adsterra-direct-link.com"  # Replace with your real Adsterra link

# --------- Helper: Open Popunder Ad ---------
def open_popunder():
    st.markdown(
        f"""
        <script>
            window.open("{adsterra_url}", "_blank");
        </script>
        """,
        unsafe_allow_html=True,
    )

# --------- Helper: Fake Keyword Scraper ---------
def get_keywords(platform, niche):
    """Fake keyword finder using random samples (replace with real scraping later)"""
    samples = {
        "Animals": ["cute dogs", "funny cats", "baby animals", "wildlife facts", "pet hacks", "dog breeds", "cat toys", "animal memes", "rescue animals", "fish tanks"],
        "Fashion": ["summer outfits", "streetwear 2025", "vintage fashion", "DIY jewelry", "men's trends", "korean fashion", "fall lookbook", "eco fashion", "designer bags", "trendy shoes"],
        "Technology": ["AI tools", "iPhone tips", "latest gadgets", "coding hacks", "Python tutorials", "tech reviews", "streaming devices", "VR games", "cloud tools", "robotics 2025"],
        # Add more niches...
    }
    time.sleep(2)  # Simulate loading
    return random.sample(samples.get(niche, []), 10)

# --------- MAIN ACTION ---------
if find_btn:
    with st.spinner("🔄 Searching for trending keywords..."):
        open_popunder()
        keywords = get_keywords(platform, niche)
        result_text = "\n".join(keywords)
        result_box.text_area("🎯 Trending Keywords", value=result_text, height=200)
        st.session_state["keywords"] = result_text

if download_btn:
    if "keywords" in st.session_state:
        open_popunder()
        filename = f"{platform.lower()}_{niche.lower()}_{datetime.now().strftime('%Y%m%d%H%M')}.txt"
        st.download_button("📥 Click to Download", st.session_state["keywords"], file_name=filename)
    else:
        st.warning("Please generate keywords first.")
