

import streamlit as st

st.set_page_config(page_title="Your Lifestyle Info", page_icon="🌙", layout="wide")

if "step" not in st.session_state:
    st.session_state.step = 1

# Set defaults for all keys needed for input fields
defaults = {
    "name": "",
    "age": 25,
    "gender": "Male",
    "height": 170,
    "weight": 70,
    "calories": 2000,
    "sleep_hours": 7,
    "screen_time": 5.0,
    "water_intake": 8,
    "sleep_time": "Between 8–11 PM",
    "wake_time": "Between 6–8 AM",
    "activity": "Moderately Active",
    "goal": "Maintain Health",
    "target_weight": 70,
    "exercise_days": 3,
    "diet": "None",
    "stress": "Medium",
    "workout": "Gym"
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1

# ========================= FIXED BLUE THEME =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(120deg, #001F54, #003B73, #0077B6, #00B4D8);
    background-size: 300% 300%;
    animation: gradientFlow 10s ease infinite;
    color: white;
}
@keyframes gradientFlow {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
h2, h3, h4, label, p, .stMarkdown { color: white !important; }
.stProgress > div > div > div > div { background-color: #00B4D8 !important; }
div.stButton > button {
    background-color: #00B4D8; color: white; border-radius: 10px; border: none; padding: 10px 20px; transition: 0.3s;
}
div.stButton > button:hover {
    background-color: #0077B6; transform: scale(1.05); box-shadow: 0 0 10px #00B4D8;
}
</style>
""", unsafe_allow_html=True)
# ======================================================================

st.markdown("<h2 style='text-align:center;'>💫 Lifestyle Information Wizard</h2>", unsafe_allow_html=True)
st.progress(st.session_state.step / 3)

if st.session_state.step == 1:
    st.subheader("Step 1: Basic Profile")
    st.text_input("Name", key="name")
    st.number_input("Age", min_value=10, max_value=100, key="age")
    st.selectbox("Gender", ["Male", "Female", "Other"], key="gender")
    st.number_input("Height (cm)", min_value=100, max_value=250, key="height")
    st.number_input("Weight (kg)", min_value=30, max_value=200, key="weight")

    if st.button("Next ➡️"):
        if not st.session_state.name.strip() or st.session_state.age < 10 or st.session_state.height < 100 or st.session_state.weight < 30:
            st.warning("Please fill all fields before continuing.")
        else:
            next_step()

elif st.session_state.step == 2:
    st.subheader("Step 2: Lifestyle Habits")
    st.number_input("Average Daily Calorie Intake", min_value=500, max_value=6000, key="calories")
    st.number_input("Average Sleep Hours per Night", min_value=3.0, max_value=12.0, key="sleep_hours")
    st.number_input("Daily Screen Time (hours)", min_value=0.0, max_value=24.0, key="screen_time")
    st.number_input("Water Intake (glasses/day)", min_value=1, max_value=20, key="water_intake")
    st.selectbox("When do you usually sleep?", ["Before 8 PM", "Between 8–11 PM", "After 11 PM"], key="sleep_time")
    st.selectbox("When do you usually wake up?", ["Before 6 AM", "Between 6–8 AM", "After 8 AM"], key="wake_time")
    st.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"], key="activity")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            prev_step()
    with col2:
        if st.button("Next ➡️"):
            # Minimal logic check
            if st.session_state.calories == 0 or st.session_state.sleep_hours == 0 or st.session_state.water_intake == 0:
                st.warning("Please fill all fields before continuing.")
            else:
                next_step()

elif st.session_state.step == 3:
    st.subheader("Step 3: Goals & Preferences")
    st.selectbox("Primary Goal", ["Weight Loss", "Muscle Gain", "Maintain Health", "Better Habits"], key="goal")
    st.number_input("Target Weight (optional)", min_value=30, max_value=200, key="target_weight")
    st.slider("Exercise Days per Week", 0, 7, key="exercise_days")
    st.selectbox("Dietary Preference", ["Vegetarian", "Vegan", "Gluten-free", "None"], key="diet")
    st.select_slider("Stress Level", ["Low", "Medium", "High"], key="stress")
    st.selectbox("Preferred Workout Type", ["Gym", "Home", "Outdoor", "Yoga", "Cardio"], key="workout")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Back"):
            prev_step()
    with col2:
        if st.button("Finish 🎯"):
            st.success("✅ Data saved successfully! Redirecting to summary...")
            st.switch_page("pages/summary.py")
