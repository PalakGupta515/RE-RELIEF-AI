import streamlit as st
import os

# ==============================================
# PAGE CONFIGURATION
# ==============================================

st.set_page_config(
    page_title="Relief Ai",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================
# CUSTOM CSS - BLUE AESTHETIC DESIGN
# ==============================================
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu, footer, header, .stDeployButton {visibility: hidden;}

    /* Blue animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #1E3C72, #2A5298, #4A90E2, #6DD5FA, #89F7FE);
        background-size: 400% 400%;
        animation: gradientShift 12s ease infinite;
        font-family: 'Poppins', sans-serif;
        color: white !important;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Center layout */
    .main-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: 100vh;
        text-align: center;
        color: #fff;
    }

    .title {
        font-size: 4rem;
        font-weight: 800;
        text-shadow: 2px 2px 15px rgba(0,0,0,0.3);
        margin-bottom: 0.5rem;
    }

    .subtitle {
        font-size: 1.5rem;
        font-weight: 400;
        margin-bottom: 2rem;
        color: #eaf6ff;
    }

    /* Rotating tagline */
    .rotating-text {
        font-size: 1.3rem;
        font-weight: 500;
        margin-bottom: 2.5rem;
        animation: fadeText 12s infinite;
        color: #f2f8ff;
    }

    @keyframes fadeText {
        0%, 25% { opacity: 1; }
        33%, 100% { opacity: 0; }
    }

    .quote {
        font-size: 1.1rem;
        font-style: italic;
        opacity: 0.9;
        margin-bottom: 2.5rem;
        max-width: 700px;
        color: #f0faff;
    }

    /* Button styling */
    div[data-testid="stButton"] button {
        background: linear-gradient(90deg, #1E3C72, #2A5298);
        color: white;
        border: none;
        font-size: 1.2rem;
        font-weight: 500;
        border-radius: 40px;
        padding: 0.9rem 2.8rem;
        box-shadow: 0px 5px 20px rgba(30, 60, 114, 0.4);
        transition: all 0.3s ease;
    }

    div[data-testid="stButton"] button:hover {
        background: linear-gradient(90deg, #2A5298, #1E3C72);
        transform: scale(1.07);
        box-shadow: 0px 8px 25px rgba(30, 60, 114, 0.6);
    }

    /* Feature cards */
    .feature-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 1.5rem;
        margin-top: 3rem;
        flex-wrap: wrap;
    }

    .feature-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 1.5rem;
        width: 230px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        color: #ffffff;
    }

    .feature-card:hover {
        transform: translateY(-8px);
        background: rgba(255, 255, 255, 0.2);
    }

    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }

    .feature-title {
        font-weight: 600;
        font-size: 1.2rem;
        margin-bottom: 0.3rem;
    }

    .feature-desc {
        font-size: 0.9rem;
        opacity: 0.9;
    }

    /* Footer */
    .footer {
        position: absolute;
        bottom: 10px;
        width: 100%;
        text-align: center;
        color: #dff3ff;
        font-size: 0.95rem;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================
# PAGE CONTENT
# ==============================================
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.markdown("<div class='title'>🌟 Lifestyle Changer 🌟</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your personal guide to a calm, focused, and better you.</div>", unsafe_allow_html=True)

# Rotating tagline
st.markdown("""
<div class="rotating-text" id="rotate"></div>

<script>
const messages = [
  "Build Better Habits 💪",
  "Transform Your Health 🌿",
  "Achieve Your Goals 🎯",
  "Live Your Best Life ✨"
];
let index = 0;
const rotate = document.getElementById("rotate");
function changeText() {
    rotate.textContent = messages[index];
    index = (index + 1) % messages.length;
}
changeText();
setInterval(changeText, 3000);
</script>
""", unsafe_allow_html=True)

# Quote
st.markdown("<div class='quote'>“Small daily habits lead to the biggest transformations.”</div>", unsafe_allow_html=True)

# ✅ Fixed Button to open login.py page
if st.button("Start Journey 🚀"):
    st.switch_page("pages/login.py")

# Features
st.markdown("""
<div class='feature-container'>
    <div class='feature-card'>
        <div class='feature-icon'>📈</div>
        <div class='feature-title'>Track Progress</div>
        <div class='feature-desc'>Visualize your growth with daily progress insights.</div>
    </div>
    <div class='feature-card'>
        <div class='feature-icon'>🧘‍♀️</div>
        <div class='feature-title'>Build Habits</div>
        <div class='feature-desc'>Develop consistent routines for a balanced lifestyle.</div>
    </div>
    <div class='feature-card'>
        <div class='feature-icon'>🔥</div>
        <div class='feature-title'>Stay Motivated</div>
        <div class='feature-desc'>Keep your spirit high with curated inspiration daily.</div>
    </div>
</div>


""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
