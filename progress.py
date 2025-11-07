import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta, date


st.set_page_config(page_title="Progress Tracker", page_icon="📈", layout="wide", initial_sidebar_state="expanded")


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
    h1, h2, h3, h4, p, label, .stMarkdown { color: white !important; font-family: 'Inter', 'Segoe UI', sans-serif; }
    .glass-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px); border-radius: 16px; padding: 24px;
        border: 1px solid rgba(255, 255, 255, 0.2); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15); margin: 15px 0;
    }
    .stButton > button {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.25), rgba(255, 255, 255, 0.15));
        backdrop-filter: blur(10px); color: white; border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 12px; padding: 10px 24px; font-weight: 600; transition: all 0.3s ease;
    }
    .stButton > button:hover { background: linear-gradient(135deg, rgba(255, 255, 255, 0.35), rgba(255, 255, 255, 0.25));
        transform: translateY(-2px); box-shadow: 0 6px 25px rgba(0, 0, 0, 0.2); }
    [data-testid="stMetricValue"] { font-size: 2em; font-weight: 700; color: white; }
    [data-testid="stMetricLabel"] { color: rgba(255, 255, 255, 0.95); }
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px); border-radius: 12px; padding: 20px; border: 1px solid rgba(255, 255, 255, 0.2);
    }
</style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.markdown("# 🌟 Navigation")
    st.markdown("---")
    if st.button("📊 Dashboard", use_container_width=True): st.switch_page("pages/maindashboard.py")
    if st.button("📈 Progress Tracker", use_container_width=True, type="primary"): st.rerun()
    if st.button("🎯 Goals Manager", use_container_width=True): st.switch_page("pages/goalmanager.py")
    if st.button("💪 Workout Library", use_container_width=True): st.switch_page("pages/workoutlibrary.py")
    if st.button("🍽️ Meal Planner", use_container_width=True): st.switch_page("pages/mealplanner.py")
    if st.button("🤖 AI Health Coach", use_container_width=True): st.switch_page("pages/aicoach.py")
    st.markdown("---")
    if st.button("🏠 Home", use_container_width=True): st.switch_page("app.py")
    if st.button("📋 Summary", use_container_width=True): st.switch_page("pages/summary.py")


# Initialize sample data
if 'weight_history' not in st.session_state:
    today = date.today()
    dates = [(today - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(29, -1, -1)]
    initial_weight_val = st.session_state.get('weight', 70)
    weights = [initial_weight_val - (i * 0.15) + (i % 3) * 0.1 for i in range(30)]
    st.session_state.weight_history = pd.DataFrame({'Date': dates, 'Weight (kg)': weights})


if 'sleep_history' not in st.session_state:
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    sleep_hours = [7.5, 6.8, 7.2, 8.1, 7.0, 8.5, 7.8]
    st.session_state.sleep_history = pd.DataFrame({'Day': days, 'Hours': sleep_hours})


if 'workout_history' not in st.session_state:
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    workouts = [30, 0, 45, 30, 0, 60, 40]
    st.session_state.workout_history = pd.DataFrame({'Day': days, 'Minutes': workouts})


if 'calorie_history' not in st.session_state:
    target = st.session_state.get('calories', 2000)
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    calories = [1950, 2100, 1980, 2050, 2200, 1900, 2020]
    st.session_state.calorie_history = pd.DataFrame({'Day': days, 'Consumed': calories, 'Target': [target] * 7})


st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h1 style='font-size: 3em; margin: 0;'>📈 Your Progress Tracker</h1>
    <p style='font-size: 1.2em; margin-top: 10px;'>Track your journey to a healthier lifestyle</p>
</div>
""", unsafe_allow_html=True)


# Goal Manager Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎯 Manage Your Goals", use_container_width=True, type="primary"):
        st.switch_page("pages/goalmanager.py")


st.markdown("---")


st.markdown("## 📊 This Week's Overview")
col1, col2, col3, col4 = st.columns(4)


current_weight = st.session_state.get('weight', 70)
initial_weight = float(st.session_state.weight_history['Weight (kg)'].iloc[0])
weight_change = round(current_weight - initial_weight, 1)
avg_sleep = round(st.session_state.sleep_history['Hours'].mean(), 1)
total_workouts = st.session_state.workout_history['Minutes'].astype(bool).sum()
avg_calories = round(st.session_state.calorie_history['Consumed'].mean())


with col1: st.metric("⚖️ Weight Change", f"{abs(weight_change)} kg", f"{weight_change:+.1f} kg" if weight_change != 0 else "No change")
with col2: st.metric("😴 Avg Sleep", f"{avg_sleep}h", "Optimal" if 7 <= avg_sleep <= 9 else "Needs work")
with col3: st.metric("💪 Workouts", f"{total_workouts} days", f"{total_workouts}/7 days")
with col4: st.metric("🍽️ Avg Calories", f"{avg_calories}", "On track" if abs(avg_calories - st.session_state.get('calories', 2000)) < 200 else "Adjust")


st.markdown("<br>", unsafe_allow_html=True)


st.markdown("## ⚖️ Weight Progress (Last 30 Days)")
fig_weight = go.Figure()
fig_weight.add_trace(go.Scatter(x=st.session_state.weight_history['Date'], y=st.session_state.weight_history['Weight (kg)'],
    mode='lines+markers', name='Weight', line=dict(color='#10b981', width=3), marker=dict(size=8, color='#34d399')))
fig_weight.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'),
    xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'), yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)', title='Weight (kg)'),
    hovermode='x unified', height=400)
st.plotly_chart(fig_weight, use_container_width=True)


st.markdown("<br>", unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    st.markdown("### 😴 Sleep Hours (Last 7 Days)")
    fig_sleep = go.Figure()
    fig_sleep.add_trace(go.Bar(x=st.session_state.sleep_history['Day'], y=st.session_state.sleep_history['Hours'],
        marker=dict(color=st.session_state.sleep_history['Hours'], colorscale='Blues', showscale=False),
        text=st.session_state.sleep_history['Hours'], textposition='outside'))
    fig_sleep.add_hline(y=7.5, line_dash="dash", line_color="rgba(255,255,255,0.5)", annotation_text="Target: 7.5h")
    fig_sleep.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'),
        xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)', title='Hours'), height=350)
    st.plotly_chart(fig_sleep, use_container_width=True)


with col2:
    st.markdown("### 💪 Workout Minutes (Last 7 Days)")
    fig_workout = go.Figure()
    fig_workout.add_trace(go.Bar(x=st.session_state.workout_history['Day'], y=st.session_state.workout_history['Minutes'],
        marker=dict(color=st.session_state.workout_history['Minutes'], colorscale='Greens', showscale=False),
        text=st.session_state.workout_history['Minutes'], textposition='outside'))
    fig_workout.add_hline(y=30, line_dash="dash", line_color="rgba(255,255,255,0.5)", annotation_text="Target: 30min")
    fig_workout.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='white'),
        xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)', title='Minutes'), height=350)
    st.plotly_chart(fig_workout, use_container_width=True)


st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p style='font-size: 1em; color: rgba(255, 255, 255, 0.9);'>📈 Consistency is key! Keep tracking your progress.</p>
</div>
""", unsafe_allow_html=True)
