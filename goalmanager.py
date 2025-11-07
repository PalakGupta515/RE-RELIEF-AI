import streamlit as st
from datetime import date

st.set_page_config(page_title="Goals Manager", page_icon="🎯", layout="wide", initial_sidebar_state="expanded")

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
    .goal-card { background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1)); backdrop-filter: blur(10px);
        border-radius: 12px; padding: 20px; margin: 10px 0; border-left: 4px solid #10b981; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("# 🌟 Navigation")
    st.markdown("---")
    if st.button("📊 Dashboard", use_container_width=True): st.switch_page("pages/maindashboard.py")
    if st.button("📈 Progress Tracker", use_container_width=True): st.switch_page("pages/progress.py")
    if st.button("🎯 Goals Manager", use_container_width=True, type="primary"): st.rerun()
    if st.button("💪 Workout Library", use_container_width=True): st.switch_page("pages/workoutlibrary.py")
    if st.button("🍽️ Meal Planner", use_container_width=True): st.switch_page("pages/mealplanner.py")
    if st.button("🤖 AI Health Coach", use_container_width=True): st.switch_page("pages/aicoach.py")
    st.markdown("---")
    if st.button("🏠 Home", use_container_width=True): st.switch_page("app.py")

if 'goals' not in st.session_state:
    st.session_state.goals = [
        {"title": "Lose 5kg", "category": "Weight Loss", "target": "65kg", "current": "70kg", "progress": 0, "deadline": "2025-12-31"},
        {"title": "Run 5K", "category": "Fitness", "target": "5km", "current": "2km", "progress": 40, "deadline": "2025-11-30"},
        {"title": "Sleep 8h daily", "category": "Sleep", "target": "8h", "current": "7h", "progress": 87, "deadline": "2025-12-15"},
    ]

st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h1 style='font-size: 3em; margin: 0;'>🎯 Goals Manager</h1>
    <p style='font-size: 1.2em; margin-top: 10px;'>Set, track, and achieve your health goals</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("💪 Browse Workout Library", use_container_width=True, type="primary"):
        st.switch_page("pages/workoutlibrary.py")

st.markdown("---")

st.markdown("## 🎯 Your Active Goals")

for idx, goal in enumerate(st.session_state.goals):
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"""
        <div class='goal-card'>
            <h3 style='margin: 0 0 10px 0;'>{goal['title']}</h3>
            <p style='margin: 5px 0;'><strong>Category:</strong> {goal['category']}</p>
            <p style='margin: 5px 0;'><strong>Target:</strong> {goal['target']} | <strong>Current:</strong> {goal['current']}</p>
            <p style='margin: 5px 0;'><strong>Deadline:</strong> {goal['deadline']}</p>
            <div style='background: rgba(255,255,255,0.2); border-radius: 10px; height: 12px; margin-top: 10px;'>
                <div style='background: linear-gradient(90deg, #10b981, #34d399); height: 100%; border-radius: 10px; width: {goal['progress']}%;'></div>
            </div>
            <p style='text-align: right; margin: 5px 0 0 0; font-size: 0.9em;'>{goal['progress']}% Complete</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button(f"✏️ Edit", key=f"edit_{idx}", use_container_width=True):
            st.info("Edit functionality coming soon!")
        if st.button(f"✅ Complete", key=f"complete_{idx}", use_container_width=True):
            st.success(f"Goal '{goal['title']}' marked as complete! 🎉")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("## ➕ Add New Goal")
with st.expander("Create New Goal"):
    new_title = st.text_input("Goal Title", placeholder="e.g., Run 10K")
    new_category = st.selectbox("Category", ["Weight Loss", "Muscle Gain", "Fitness", "Sleep", "Nutrition", "Habits"])
    new_target = st.text_input("Target", placeholder="e.g., 10km")
    new_deadline = st.date_input("Deadline", value=date.today())
    
    if st.button("Create Goal", use_container_width=True):
        st.session_state.goals.append({
            "title": new_title, "category": new_category, "target": new_target,
            "current": "0", "progress": 0, "deadline": str(new_deadline)
        })
        st.success(f"✅ Goal '{new_title}' created!")
        st.rerun()

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p style='font-size: 1em; color: rgba(255, 255, 255, 0.9);'>🎯 Goals give you direction. Stay focused!</p>
</div>
""", unsafe_allow_html=True)
