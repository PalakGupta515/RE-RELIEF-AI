import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Health Coach", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
        background-size: 400% 400%; animation: gradientFlow 15s ease infinite; }
    @keyframes gradientFlow { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;} .stDeployButton {visibility: hidden;}
    h1, h2, h3, h4, p, label, .stMarkdown { color: white !important; font-family: 'Inter', 'Segoe UI', sans-serif; }
    .glass-card { background: linear-gradient(135deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.05)); backdrop-filter: blur(10px);
        border-radius: 16px; padding: 24px; border: 1px solid rgba(255, 255, 255, 0.2); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15); margin: 15px 0; }
    .stButton > button { background: linear-gradient(135deg, rgba(255, 255, 255, 0.25), rgba(255, 255, 255, 0.15)); backdrop-filter: blur(10px);
        color: white; border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 12px; padding: 10px 24px; font-weight: 600; transition: all 0.3s ease; }
    .stButton > button:hover { background: linear-gradient(135deg, rgba(255, 255, 255, 0.35), rgba(255, 255, 255, 0.25)); transform: translateY(-2px); box-shadow: 0 6px 25px rgba(0, 0, 0, 0.2); }
    .user-message { background: linear-gradient(135deg, rgba(16, 185, 129, 0.3), rgba(52, 211, 153, 0.2)); backdrop-filter: blur(10px);
        border-radius: 16px 16px 4px 16px; padding: 15px 20px; margin: 10px 0; max-width: 70%; margin-left: auto; border: 1px solid rgba(16, 185, 129, 0.3); }
    .ai-message { background: linear-gradient(135deg, rgba(59, 130, 246, 0.3), rgba(96, 165, 250, 0.2)); backdrop-filter: blur(10px);
        border-radius: 16px 16px 16px 4px; padding: 15px 20px; margin: 10px 0; max-width: 70%; border: 1px solid rgba(59, 130, 246, 0.3); }
    .stTextInput > div > div > input { background: rgba(255, 255, 255, 0.1); color: white; border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 12px; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("# 🌟 Navigation")
    st.markdown("---")
    if st.button("📊 Dashboard", use_container_width=True): st.switch_page("pages/maindashboard.py")
    if st.button("📈 Progress Tracker", use_container_width=True): st.switch_page("pages/progress.py")
    if st.button("🎯 Goals Manager", use_container_width=True): st.switch_page("pages/goalmanager.py")
    if st.button("💪 Workout Library", use_container_width=True): st.switch_page("pages/workoutlibrary.py")
    if st.button("🍽️ Meal Planner", use_container_width=True): st.switch_page("pages/mealplanner.py")
    if st.button("🤖 AI Health Coach", use_container_width=True, type="primary"): st.rerun()
    st.markdown("---")
    if st.button("🏠 Home", use_container_width=True): st.switch_page("app.py")
    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

# Initialize Gemini API
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# User context for personalization
user_context = f"""
You are a professional health and fitness coach. The user's profile:
- Name: {st.session_state.get('name', 'User')}
- Age: {st.session_state.get('age', 'N/A')}
- Weight: {st.session_state.get('weight', 'N/A')} kg
- Height: {st.session_state.get('height', 'N/A')} cm
- Goal: {st.session_state.get('goal', 'Maintain Health')}
- Activity Level: {st.session_state.get('activity', 'Moderately Active')}
- Dietary Preference: {st.session_state.get('diet', 'None')}

Provide personalized, actionable health and fitness advice. Be encouraging, professional, and specific.
"""

st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h1 style='font-size: 3em; margin: 0;'>🤖 AI Health Coach</h1>
    <p style='font-size: 1.2em; margin-top: 10px;'>Your personal AI-powered health assistant</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Quick action buttons
st.markdown("### 🎯 Quick Actions")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("💪 Suggest Workout", use_container_width=True):
        st.session_state.chat_history.append({"role": "user", "content": "Suggest a workout plan for me based on my profile"})
        st.rerun()

with col2:
    if st.button("🍽️ Meal Ideas", use_container_width=True):
        st.session_state.chat_history.append({"role": "user", "content": "Give me healthy meal ideas for today"})
        st.rerun()

with col3:
    if st.button("🎯 Set Goals", use_container_width=True):
        st.session_state.chat_history.append({"role": "user", "content": "Help me set realistic health goals"})
        st.rerun()

with col4:
    if st.button("💡 Motivation", use_container_width=True):
        st.session_state.chat_history.append({"role": "user", "content": "Give me some motivation to stay on track"})
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# Chat container
chat_container = st.container()

with chat_container:
    st.markdown("### 💬 Chat")
    
    # Display chat history
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"""
            <div class='user-message'>
                <p style='margin: 0;'><strong>You:</strong> {message['content']}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='ai-message'>
                <p style='margin: 0;'><strong>AI Coach:</strong> {message['content']}</p>
            </div>
            """, unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Ask me anything about health, fitness, nutrition...")

if user_input:
    # Add user message to history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # Generate AI response
    try:
        # Create conversation history for context
        conversation = user_context + "\n\n"
        for msg in st.session_state.chat_history[-5:]:  # Last 5 messages for context
            conversation += f"{msg['role'].capitalize()}: {msg['content']}\n"
        
        response = model.generate_content(conversation)
        ai_response = response.text
        
        # Add AI response to history
        st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
        
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
        st.info("💡 Make sure you've added your GEMINI_API_KEY to Streamlit secrets!")
        st.info("Get your free API key from: https://makersuite.google.com/app/apikey")
    
    st.rerun()

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p style='font-size: 1em; color: rgba(255, 255, 255, 0.9);'>🤖 Your AI coach is here 24/7. Ask anything!</p>
</div>
""", unsafe_allow_html=True)
