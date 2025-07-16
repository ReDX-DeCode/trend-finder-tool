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
    """Fake keyword finder using random samples (safe version)"""
    samples = {
        "Animals": ["cute dogs", "funny cats", "baby animals", "wildlife facts", "pet hacks", "dog breeds", "cat toys", "animal memes", "rescue animals", "fish tanks"],
        "Fashion": ["summer outfits", "streetwear 2025", "vintage fashion", "DIY jewelry", "men's trends", "korean fashion", "fall lookbook", "eco fashion", "designer bags", "trendy shoes"],
        "Technology": ["AI tools", "iPhone tips", "latest gadgets", "coding hacks", "Python tutorials", "tech reviews", "streaming devices", "VR games", "cloud tools", "robotics 2025"],
        "Fitness": ["home workouts", "fat burn tips", "gym diet", "yoga basics", "muscle building", "fitness vlogs", "stretching guide", "HIIT training", "workout gear", "healthy habits"],
        "Food": ["easy recipes", "vegan meals", "snack ideas", "food hacks", "meal prep", "baking tips", "restaurant review", "healthy snacks", "grilled chicken", "air fryer meals"],
        "Gaming": ["top 10 games", "mobile gaming", "gta 6 leaks", "fps skills", "gaming setup", "esports news", "streaming tips", "horror games", "game reviews", "console wars"],
        "Education": ["study hacks", "exam tips", "learn Python", "math tricks", "study motivation", "free courses", "student planner", "college prep", "note taking", "learn AI"],
        "Health": ["mental health", "sleep hacks", "meditation apps", "stress relief", "skin care", "immunity tips", "hydration facts", "doctor advice", "cold remedies", "health goals"],
        "Business": ["startup tips", "business ideas", "side hustle", "investing guide", "freelance tips", "digital marketing", "ecommerce trends", "growth hacks", "sales tricks", "brand building"],
        "DIY": ["diy crafts", "home decor", "make candles", "recycled art", "budget makeover", "handmade gifts", "diy storage", "room decor", "wall painting", "plant pots"]
    }

    time.sleep(2)  # Simulate loading
    keywords = samples.get(niche, [])
    if len(keywords) < 10:
        return keywords
    return random.sample(keywords, 10)


# --------- MAIN ACTION ---------

# --------- FIND BUTTON LOGIC ---------
if find_btn:
    with st.spinner("🔄 Searching for trending keywords..."):
        keywords = get_keywords(platform, niche)  # Generate 10 keywords
        result_text = "\n".join(keywords)  # Join as text block
        result_box.text_area("🎯 Trending Keywords", value=result_text, height=200)  # Show result
        st.session_state["keywords"] = result_text  # Store in session

# --------- DOWNLOAD BUTTON LOGIC ---------
if download_btn:
    if "keywords" in st.session_state:
        filename = f"{platform.lower()}_{niche.lower()}_{datetime.now().strftime('%Y%m%d%H%M')}.txt"
        st.download_button(
            label="📥 Click to Download",
            data=st.session_state["keywords"],
            file_name=filename,
            mime="text/plain"
        )
    else:
        st.warning("⚠️ Please generate keywords first using the Find button.")
