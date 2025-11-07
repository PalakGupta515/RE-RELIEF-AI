import streamlit as st
from datetime import datetime, date

# =========================================
# PAGE CONFIGURATION
# =========================================
st.set_page_config(
    page_title="Main Dashboard", 
    page_icon="📊", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================
# MATCHING GRADIENT BACKGROUND
# =========================================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #4facfe 75%, #00f2fe 100%);
        background-size: 400% 400%;
        animation: gradientFlow 15s ease infinite;
    }
    
    @keyframes gradientFlow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
    h1, h2, h3, h4, p, label, .stMarkdown {
        color: white !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    /* Glassmorphism Cards */
    .glass-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 24px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        margin: 15px 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.25), rgba(255, 255, 255, 0.15));
        backdrop-filter: blur(10px);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 12px;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.35), rgba(255, 255, 255, 0.25));
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.2);
    }
    
    [data-testid="stMetricValue"] {
        font-size: 2em;
        font-weight: 700;
        color: white;
    }
    
    [data-testid="stMetricLabel"] {
        color: rgba(255, 255, 255, 0.95);
    }
    
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .progress-bar {
        background: rgba(255, 255, 255, 0.2);
        border-radius: 10px;
        height: 12px;
        overflow: hidden;
        margin: 10px 0;
    }
    
    .progress-fill {
        background: linear-gradient(90deg, #10b981, #34d399);
        height: 100%;
        border-radius: 10px;
        transition: width 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# =========================================
# SIDEBAR NAVIGATION
# =========================================
with st.sidebar:
    st.markdown("# 🌟 Navigation")
    st.markdown("---")
    
    if st.button("📊 Dashboard", use_container_width=True, type="primary"):
        st.rerun()
    
    if st.button("📈 Progress Tracker", use_container_width=True):
        st.switch_page("pages/progress.py")
    
    if st.button("🎯 Goals", use_container_width=True):
        st.info("Coming soon!")
    
    if st.button("💪 Workouts", use_container_width=True):
        st.info("Coming soon!")
    
    if st.button("🍽️ Meal Planner", use_container_width=True):
        st.info("Coming soon!")
    
    if st.button("⚙️ Settings", use_container_width=True):
        st.info("Coming soon!")
    
    st.markdown("---")
    
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
    
    if st.button("📋 Summary", use_container_width=True):
        st.switch_page("pages/summary.py")

# =========================================
# INITIALIZE SESSION STATE FOR DAILY TRACKING
# =========================================
if 'daily_water' not in st.session_state:
    st.session_state.daily_water = 0
if 'daily_calories_logged' not in st.session_state:
    st.session_state.daily_calories_logged = 0
if 'daily_steps' not in st.session_state:
    st.session_state.daily_steps = 0
if 'daily_workout_mins' not in st.session_state:
    st.session_state.daily_workout_mins = 0
if 'activity_log' not in st.session_state:
    st.session_state.activity_log = []
if 'streak_days' not in st.session_state:
    st.session_state.streak_days = 5

# =========================================
# HERO SECTION
# =========================================
current_hour = datetime.now().hour
if current_hour < 12:
    greeting = "Good Morning"
    emoji = "🌅"
elif current_hour < 18:
    greeting = "Good Afternoon"
    emoji = "☀️"
else:
    greeting = "Good Evening"
    emoji = "🌙"

name = st.session_state.get('name', 'Friend')

st.markdown(f"""
<div style='text-align: center; padding: 20px;'>
    <h1 style='font-size: 3em; margin: 0;'>{emoji} {greeting}, {name}!</h1>
    <p style='font-size: 1.2em; margin-top: 10px;'>Today is {date.today().strftime('%A, %B %d, %Y')}</p>
</div>
""", unsafe_allow_html=True)

# ADD PROGRESS TRACKER BUTTON
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("📈 View Your Progress Tracker", use_container_width=True, type="primary"):
        st.switch_page("pages/progress.py")

st.markdown("---")

# =========================================
# STREAK & QUICK STATS
# =========================================
st.markdown("## 🔥 Your Streak & Quick Stats")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🔥 Streak", f"{st.session_state.streak_days} days", "+1 day")

with col2:
    st.metric("💧 Water Today", f"{st.session_state.daily_water} glasses", f"{8 - st.session_state.daily_water} to go")

with col3:
    st.metric("🍽️ Calories Logged", f"{st.session_state.daily_calories_logged} kcal", f"{st.session_state.get('calories', 2000) - st.session_state.daily_calories_logged} left")

with col4:
    st.metric("⏱️ Active Minutes", f"{st.session_state.daily_workout_mins} min", "30 min goal")

st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# QUICK LOG SECTION
# =========================================
st.markdown("## ➕ Quick Log")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='glass-card'>
        <h3>💧 Log Water Intake</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        if st.button("➕ Add 1 Glass", use_container_width=True, key="water1"):
            st.session_state.daily_water += 1
            st.session_state.activity_log.append(f"Added 1 glass of water - {datetime.now().strftime('%I:%M %p')}")
            st.rerun()
    with col_b:
        if st.button("➕ Add 2 Glasses", use_container_width=True, key="water2"):
            st.session_state.daily_water += 2
            st.session_state.activity_log.append(f"Added 2 glasses of water - {datetime.now().strftime('%I:%M %p')}")
            st.rerun()
    with col_c:
        if st.button("🔄 Reset", use_container_width=True, key="water_reset"):
            st.session_state.daily_water = 0
            st.rerun()

with col2:
    st.markdown("""
    <div class='glass-card'>
        <h3>🍽️ Log Meal</h3>
    </div>
    """, unsafe_allow_html=True)
    
    meal_type = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner", "Snack"], key="meal_type")
    meal_calories = st.number_input("Calories", min_value=0, max_value=2000, step=50, key="meal_cal")
    
    if st.button("➕ Log Meal", use_container_width=True, key="log_meal"):
        st.session_state.daily_calories_logged += meal_calories
        st.session_state.activity_log.append(f"Logged {meal_type} - {meal_calories} kcal - {datetime.now().strftime('%I:%M %p')}")
        st.success(f"✅ {meal_type} logged! {meal_calories} calories added.")
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='glass-card'>
        <h3>🏃 Log Workout</h3>
    </div>
    """, unsafe_allow_html=True)
    
    workout_type = st.selectbox("Workout Type", ["Cardio", "Strength", "Yoga", "Sports", "Walking"], key="workout_type")
    workout_duration = st.number_input("Duration (minutes)", min_value=5, max_value=180, step=5, key="workout_dur")
    
    if st.button("➕ Log Workout", use_container_width=True, key="log_workout"):
        st.session_state.daily_workout_mins += workout_duration
        st.session_state.activity_log.append(f"Completed {workout_duration}min {workout_type} - {datetime.now().strftime('%I:%M %p')}")
        st.success(f"✅ {workout_type} workout logged! {workout_duration} minutes added.")
        st.rerun()

with col2:
    st.markdown("""
    <div class='glass-card'>
        <h3>😴 Log Sleep</h3>
    </div>
    """, unsafe_allow_html=True)
    
    sleep_hours_logged = st.slider("Hours slept last night", min_value=0.0, max_value=12.0, value=7.0, step=0.5, key="sleep_log")
    sleep_quality_log = st.select_slider("Sleep Quality", ["Poor", "Fair", "Good", "Excellent"], value="Good", key="sleep_qual")
    
    if st.button("➕ Log Sleep", use_container_width=True, key="log_sleep"):
        st.session_state.activity_log.append(f"Logged {sleep_hours_logged}h sleep ({sleep_quality_log}) - {datetime.now().strftime('%I:%M %p')}")
        st.success(f"✅ Sleep logged! {sleep_hours_logged}h - {sleep_quality_log} quality.")
        st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# DAILY GOALS PROGRESS
# =========================================
st.markdown("## 🎯 Today's Goals Progress")

# Water goal
water_target = 8
water_progress = min((st.session_state.daily_water / water_target) * 100, 100)
st.markdown(f"**💧 Water Intake:** {st.session_state.daily_water}/{water_target} glasses")
st.markdown(f"""
<div class='progress-bar'>
    <div class='progress-fill' style='width: {water_progress}%;'></div>
</div>
""", unsafe_allow_html=True)

# Calorie goal
calorie_target = st.session_state.get('calories', 2000)
calorie_progress = min((st.session_state.daily_calories_logged / calorie_target) * 100, 100)
st.markdown(f"**🍽️ Calorie Intake:** {st.session_state.daily_calories_logged}/{calorie_target} kcal")
st.markdown(f"""
<div class='progress-bar'>
    <div class='progress-fill' style='width: {calorie_progress}%;'></div>
</div>
""", unsafe_allow_html=True)

# Workout goal
workout_target = 30
workout_progress = min((st.session_state.daily_workout_mins / workout_target) * 100, 100)
st.markdown(f"**💪 Active Minutes:** {st.session_state.daily_workout_mins}/{workout_target} min")
st.markdown(f"""
<div class='progress-bar'>
    <div class='progress-fill' style='width: {workout_progress}%;'></div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# RECENT ACTIVITY FEED
# =========================================
st.markdown("## 📜 Recent Activity")

if st.session_state.activity_log:
    for activity in reversed(st.session_state.activity_log[-10:]):  # Show last 10 activities
        st.markdown(f"""
        <div style='background: rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 12px; margin: 8px 0;'>
            ✅ {activity}
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("No activities logged today. Start tracking your lifestyle!")

st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# MOTIVATIONAL WIDGET
# =========================================
st.markdown("## 💭 Daily Motivation")

quotes = [
    "The secret of getting ahead is getting started. - Mark Twain",
    "Success is the sum of small efforts repeated day in and day out. - Robert Collier",
    "You don't have to be great to start, but you have to start to be great. - Zig Ziglar",
    "The only bad workout is the one that didn't happen.",
    "Take care of your body. It's the only place you have to live. - Jim Rohn"
]

import random
if 'daily_quote' not in st.session_state:
    st.session_state.daily_quote = random.choice(quotes)

st.markdown(f"""
<div class='glass-card' style='text-align: center;'>
    <p style='font-size: 1.2em; font-style: italic;'>"{st.session_state.daily_quote}"</p>
</div>
""", unsafe_allow_html=True)

if st.button("🔄 New Quote", use_container_width=False):
    st.session_state.daily_quote = random.choice(quotes)
    st.rerun()

# =========================================
# FOOTER
# =========================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p style='font-size: 1em; color: rgba(255, 255, 255, 0.9);'>
        💪 Keep going! Every step counts towards your goals.
    </p>
</div>
""", unsafe_allow_html=True)
