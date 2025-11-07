import streamlit as st

st.set_page_config(page_title="Workout Library", page_icon="💪", layout="wide", initial_sidebar_state="expanded")

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
    .workout-card { background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1)); backdrop-filter: blur(10px);
        border-radius: 12px; padding: 20px; margin: 10px 0; border: 1px solid rgba(255, 255, 255, 0.2); }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("# 🌟 Navigation")
    st.markdown("---")
    if st.button("📊 Dashboard", use_container_width=True): st.switch_page("pages/maindashboard.py")
    if st.button("📈 Progress Tracker", use_container_width=True): st.switch_page("pages/progress.py")
    if st.button("🎯 Goals Manager", use_container_width=True): st.switch_page("pages/goalmanager.py")
    if st.button("💪 Workout Library", use_container_width=True, type="primary"): st.rerun()
    if st.button("🍽️ Meal Planner", use_container_width=True): st.switch_page("pages/mealplanner.py")
    if st.button("🤖 AI Health Coach", use_container_width=True): st.switch_page("pages/aicoach.py")
    st.markdown("---")
    if st.button("🏠 Home", use_container_width=True): st.switch_page("app.py")

workouts = [
    {"title": "Full Body Strength", "duration": "45 min", "difficulty": "Intermediate", "type": "Strength", "calories": "350",
     "exercises": ["Push-ups (3x15)", "Squats (3x20)", "Planks (3x60s)", "Lunges (3x12)", "Burpees (3x10)"]},
    {"title": "Cardio Blast", "duration": "30 min", "difficulty": "Beginner", "type": "Cardio", "calories": "400",
     "exercises": ["Jumping Jacks (3x30)", "High Knees (3x45s)", "Mountain Climbers (3x20)", "Running in Place (5 min)", "Cool Down (5 min)"]},
    {"title": "Yoga Flow", "duration": "60 min", "difficulty": "Beginner", "type": "Yoga", "calories": "200",
     "exercises": ["Sun Salutations (5 rounds)", "Warrior Poses (2 min each)", "Tree Pose (1 min each side)", "Child's Pose (5 min)", "Savasana (10 min)"]},
    {"title": "HIIT Power", "duration": "20 min", "difficulty": "Advanced", "type": "HIIT", "calories": "450",
     "exercises": ["Burpees (40s on, 20s off)", "Jump Squats (40s on, 20s off)", "Push-ups (40s on, 20s off)", "Plank Jacks (40s on, 20s off)", "Repeat 4x"]},
    {"title": "Core Crusher", "duration": "25 min", "difficulty": "Intermediate", "type": "Core", "calories": "250",
     "exercises": ["Crunches (3x25)", "Russian Twists (3x30)", "Leg Raises (3x15)", "Bicycle Crunches (3x20)", "Plank (3x90s)"]},
]

st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h1 style='font-size: 3em; margin: 0;'>💪 Workout Library</h1>
    <p style='font-size: 1.2em; margin-top: 10px;'>Find the perfect workout for your goals</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🍽️ Plan Your Meals", use_container_width=True, type="primary"):
        st.switch_page("pages/mealplanner.py")

st.markdown("---")

st.markdown("## 🔍 Filter Workouts")
col1, col2, col3 = st.columns(3)
with col1:
    filter_type = st.selectbox("Type", ["All", "Strength", "Cardio", "Yoga", "HIIT", "Core"])
with col2:
    filter_difficulty = st.selectbox("Difficulty", ["All", "Beginner", "Intermediate", "Advanced"])
with col3:
    filter_duration = st.selectbox("Duration", ["All", "< 30 min", "30-45 min", "> 45 min"])

st.markdown("## 🏋️ Available Workouts")

for idx, workout in enumerate(workouts):
    st.markdown(f"""
    <div class='workout-card'>
        <h3 style='margin: 0 0 10px 0;'>{workout['title']}</h3>
        <p style='margin: 5px 0;'>
            <span style='background: rgba(16, 185, 129, 0.3); padding: 4px 12px; border-radius: 12px; margin-right: 8px;'>{workout['type']}</span>
            <span style='background: rgba(59, 130, 246, 0.3); padding: 4px 12px; border-radius: 12px; margin-right: 8px;'>{workout['difficulty']}</span>
            <span style='background: rgba(245, 158, 11, 0.3); padding: 4px 12px; border-radius: 12px;'>{workout['duration']}</span>
        </p>
        <p style='margin: 10px 0 5px 0;'><strong>🔥 Calories Burned:</strong> ~{workout['calories']} kcal</p>
        <p style='margin: 5px 0;'><strong>Exercises:</strong></p>
        <ul style='margin: 5px 0; padding-left: 20px;'>
            {''.join([f"<li>{ex}</li>" for ex in workout['exercises']])}
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([4, 1])
    with col2:
        if st.button(f"Start Workout", key=f"start_{idx}", use_container_width=True):
            st.success(f"🎯 {workout['title']} started! Go get 'em! 💪")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p style='font-size: 1em; color: rgba(255, 255, 255, 0.9);'>💪 The only bad workout is the one you didn't do!</p>
</div>
""", unsafe_allow_html=True)
