import streamlit as st

# =========================================
# PAGE CONFIGURATION
# =========================================
st.set_page_config(
    page_title="Your Lifestyle Summary", 
    page_icon="📊", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================
# PROFESSIONAL GRADIENT BACKGROUND + STYLING
# =========================================
st.markdown("""
<style>
    /* Animated Professional Gradient */
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
    
    /* Main Container */
    .main {
        padding: 2rem;
    }
    
    /* Hide Streamlit Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
    /* Typography */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        color: white !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    /* Professional Metric Cards */
    [data-testid="stMetricValue"] {
        font-size: 2.5em;
        font-weight: 700;
        color: white;
    }
    
    [data-testid="stMetricDelta"] {
        font-size: 1em;
        color: rgba(255, 255, 255, 0.9);
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 1.1em;
        font-weight: 500;
        color: rgba(255, 255, 255, 0.95);
    }
    
    /* Custom Metric Card Container */
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0.05));
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 24px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    div[data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 48px rgba(0, 0, 0, 0.25);
    }
    
    /* Professional Tip Cards */
    .tip-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1));
        backdrop-filter: blur(15px);
        border-radius: 12px;
        padding: 18px 22px;
        margin: 12px 0;
        border-left: 4px solid;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        color: white;
        font-size: 1.05em;
        line-height: 1.6;
        transition: all 0.3s ease;
    }
    
    .tip-card:hover {
        transform: translateX(5px);
        box-shadow: 0 6px 28px rgba(0, 0, 0, 0.15);
    }
    
    .tip-success {
        border-left-color: #10b981;
    }
    
    .tip-warning {
        border-left-color: #f59e0b;
    }
    
    .tip-info {
        border-left-color: #3b82f6;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 2em;
        font-weight: 700;
        margin: 30px 0 20px 0;
        color: white;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    
    /* Hero Section */
    .hero-section {
        text-align: center;
        padding: 40px 20px;
        margin-bottom: 30px;
    }
    
    .hero-title {
        font-size: 3.5em;
        font-weight: 800;
        color: white;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        margin-bottom: 10px;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        font-size: 1.3em;
        color: rgba(255, 255, 255, 0.9);
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    
    /* Divider */
    hr {
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        margin: 40px 0;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.25), rgba(255, 255, 255, 0.15));
        backdrop-filter: blur(10px);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 12px;
        padding: 12px 28px;
        font-weight: 600;
        font-size: 1.05em;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.35), rgba(255, 255, 255, 0.25));
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.2);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1));
        backdrop-filter: blur(10px);
        border-radius: 12px;
        color: white;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# =========================================
# HERO SECTION
# =========================================
st.markdown("""
<div class='hero-section'>
    <h1 class='hero-title'>📊 Your Health Dashboard</h1>
    <p class='hero-subtitle'>Personalized insights to transform your lifestyle</p>
</div>
""", unsafe_allow_html=True)

# =========================================
# CHECK IF DATA EXISTS
# =========================================
if 'name' not in st.session_state:
    st.warning("⚠️ No data found! Please complete the onboarding first.")
    if st.button("Go to Onboarding", use_container_width=True):
        st.switch_page("pages/onboarding.py")
    st.stop()

# =========================================
# CALCULATE HEALTH METRICS
# =========================================

# BMI Calculation
height_m = st.session_state.get('height', 170) / 100
weight = st.session_state.get('weight', 70)
bmi = round(weight / (height_m ** 2), 1)

if bmi < 18.5:
    bmi_category = "Underweight"
    bmi_delta = "⚠️ Below normal"
elif 18.5 <= bmi < 25:
    bmi_category = "Normal"
    bmi_delta = "✅ Healthy range"
elif 25 <= bmi < 30:
    bmi_category = "Overweight"
    bmi_delta = "⚠️ Above normal"
else:
    bmi_category = "Obese"
    bmi_delta = "🔴 Action needed"

# Sleep Quality
sleep_hours = st.session_state.get('sleep_hours', 7)
if 7 <= sleep_hours <= 9:
    sleep_quality = "Optimal"
    sleep_delta = "✅ Perfect"
elif 6 <= sleep_hours < 7 or 9 < sleep_hours <= 10:
    sleep_quality = "Fair"
    sleep_delta = "⚠️ Needs improvement"
else:
    sleep_quality = "Poor"
    sleep_delta = "🔴 Critical"

# Screen Time Analysis
screen_time = st.session_state.get('screen_time', 6)
if screen_time <= 4:
    screen_status = "Healthy"
    screen_delta = "✅ Excellent"
elif 4 < screen_time <= 8:
    screen_status = "Moderate"
    screen_delta = "⚠️ Monitor closely"
else:
    screen_status = "High"
    screen_delta = "🔴 Reduce usage"

# Calculate Lifestyle Score
activity_map = {
    'Sedentary': 20,
    'Lightly Active': 40,
    'Moderately Active': 60,
    'Very Active': 80,
    'Extremely Active': 100
}
activity_level = st.session_state.get('activity', 'Moderately Active')
activity_score = activity_map.get(activity_level, 60)

lifestyle_score = round((
    (100 if 7 <= sleep_hours <= 9 else 50) * 0.25 +
    (100 if screen_time <= 4 else 50 if screen_time <= 8 else 20) * 0.15 +
    activity_score * 0.30 +
    (100 if 18.5 <= bmi < 25 else 60) * 0.30
))

# =========================================
# PROFESSIONAL METRIC CARDS
# =========================================
st.markdown("<h2 class='section-header'>📈 Your Health Metrics</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="🏋️ BMI Index",
        value=f"{bmi}",
        delta=bmi_category
    )

with col2:
    st.metric(
        label="😴 Sleep Quality",
        value=f"{sleep_hours}h",
        delta=sleep_quality
    )

with col3:
    st.metric(
        label="📱 Screen Time",
        value=f"{screen_time}h",
        delta=screen_status
    )

with col4:
    st.metric(
        label="💫 Lifestyle Score",
        value=f"{lifestyle_score}",
        delta="Out of 100"
    )

st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# PERSONALIZED TIPS SECTION
# =========================================
st.markdown("<h2 class='section-header'>💡 Your Personalized Action Plan</h2>", unsafe_allow_html=True)

tips = []

# BMI-based tips
if bmi < 18.5:
    tips.append(("🍽️ **Increase Caloric Intake**: Your BMI is {:.1f} (Underweight). Focus on nutrient-dense foods like nuts, avocados, whole grains, and lean proteins. Aim for 300-500 extra calories daily.".format(bmi), "warning"))
elif bmi >= 25:
    tips.append(("🥗 **Balanced Nutrition Plan**: Your BMI is {:.1f} ({}). Create a 300-500 calorie deficit with lean proteins, vegetables, and whole grains. Avoid processed foods.".format(bmi, bmi_category), "warning"))
else:
    tips.append(("✅ **Maintain Healthy Weight**: Excellent! Your BMI of {:.1f} is in the optimal range. Continue your current eating habits and stay active.".format(bmi), "success"))

# Sleep tips
if sleep_hours < 7:
    tips.append(("😴 **Improve Sleep Duration**: You're averaging {}h of sleep. Adults need 7-9 hours. Create a bedtime routine, avoid screens 1 hour before bed, and keep your room cool (65-68°F).".format(sleep_hours), "warning"))
elif sleep_hours > 9:
    tips.append(("⏰ **Optimize Sleep Duration**: {}h of sleep might be excessive. Oversleeping can indicate health issues. Aim for 7-9 hours and consult a doctor if fatigue persists.".format(sleep_hours), "info"))
else:
    tips.append(("🌙 **Excellent Sleep Habits**: Perfect! You're getting {}h of sleep. Maintain consistent sleep/wake times, even on weekends, to reinforce this healthy pattern.".format(sleep_hours), "success"))

# Sleep schedule
sleep_schedule = st.session_state.get('sleep_time', 'Between 8–11 PM')
wake_schedule = st.session_state.get('wake_time', 'Between 6–8 AM')

if sleep_schedule == "After 11 PM":
    tips.append(("🌆 **Earlier Bedtime Recommended**: Sleeping after 11 PM can disrupt your circadian rhythm. Gradually shift your bedtime 15 minutes earlier each week until you're sleeping by 10 PM.", "info"))
elif sleep_schedule == "Before 8 PM":
    tips.append(("🌅 **Early Bird Schedule**: You have an early sleep pattern. Ensure you get morning sunlight exposure to reinforce this natural rhythm and maintain sleep quality.", "success"))

if wake_schedule == "After 8 AM":
    tips.append(("☀️ **Earlier Wake Time**: Consider waking before 8 AM to maximize productivity and align with natural circadian rhythms. Morning sunlight exposure is crucial for health.", "info"))
elif wake_schedule == "Before 6 AM":
    tips.append(("🌄 **Early Riser Excellence**: Waking before 6 AM gives you a productivity advantage. Ensure you're getting adequate sleep (7-9h) to avoid burnout.", "success"))

# Screen time
if screen_time > 8:
    tips.append(("📱 **Urgent: Reduce Screen Time**: {}h daily is excessive. Apply the 20-20-20 rule (every 20 min, look 20 feet away for 20 sec). Set app limits and create 'screen-free' hours.".format(screen_time), "warning"))
elif screen_time > 4:
    tips.append(("👀 **Monitor Screen Usage**: {}h daily is moderate but improvable. Take regular breaks, use blue light filters after sunset, and practice eye exercises.".format(screen_time), "info"))
else:
    tips.append(("✨ **Healthy Digital Habits**: Excellent! Your {}h screen time is well-balanced. Continue maintaining this healthy relationship with technology.".format(screen_time), "success"))

# Water intake
water_intake = st.session_state.get('water_intake', 8)
if water_intake < 8:
    tips.append(("💧 **Increase Hydration**: You're drinking {} glasses daily. Aim for 8-10 glasses. Set hourly reminders, keep a water bottle nearby, and drink before each meal.".format(water_intake), "info"))
else:
    tips.append(("🥤 **Excellent Hydration**: Perfect! {} glasses daily keeps you properly hydrated, supporting metabolism, skin health, and cognitive function.".format(water_intake), "success"))

# Activity level
if activity_level in ['Sedentary', 'Lightly Active']:
    tips.append(("🏃 **Increase Physical Activity**: You're currently {}. Start with 30 minutes of moderate exercise 3x/week (walking, cycling, swimming). Gradually increase to 150 min/week.".format(activity_level), "warning"))
elif activity_level == 'Moderately Active':
    tips.append(("💪 **Enhance Your Routine**: Good activity level! Add 2 days of strength training. Mix cardio with resistance exercises for optimal health benefits.", "info"))
else:
    tips.append(("🏆 **Outstanding Activity Level**: Amazing! You're very active. Ensure 1-2 rest days weekly and focus on recovery with stretching, foam rolling, and proper nutrition.", "success"))

# Exercise frequency
exercise_days = st.session_state.get('exercise_days', 3)
if exercise_days < 3:
    tips.append(("📅 **Increase Exercise Frequency**: You exercise {} days/week. Aim for 3-5 days minimum. Even 20-30 minute sessions count. Schedule workouts like important appointments.".format(exercise_days), "info"))
elif exercise_days >= 5:
    tips.append(("🎯 **Consistent Exercise Routine**: Excellent! {} days/week is outstanding. Ensure variety (cardio, strength, flexibility) and prioritize rest for recovery.".format(exercise_days), "success"))

# Stress management
stress_level = st.session_state.get('stress', 'Medium')
if stress_level in ['High', 'Very High']:
    tips.append(("🧘 **Stress Management Priority**: Your stress level is {}. Practice daily meditation (10-15 min), deep breathing, or yoga. Consider journaling and limit caffeine.".format(stress_level), "warning"))
elif stress_level == 'Medium':
    tips.append(("🌿 **Maintain Stress Balance**: Moderate stress is manageable. Continue healthy coping mechanisms, try mindfulness apps, exercise regularly, and ensure work-life balance.", "info"))
else:
    tips.append(("😌 **Excellent Stress Management**: Great job maintaining low stress! Share your strategies with others and continue your current practices.", "success"))

# Calorie tips
goal = st.session_state.get('goal', 'Maintain Health')
calories = st.session_state.get('calories', 2000)

if goal == 'Weight Loss' and calories > 2200:
    tips.append(("⚖️ **Adjust Calorie Target**: For weight loss, {} calories might be high. Consider 1,500-1,800 depending on activity. Consult a nutritionist for personalized advice.".format(calories), "info"))
elif goal == 'Muscle Gain' and calories < 2500:
    tips.append(("💪 **Increase Calories for Muscle Growth**: For muscle gain, {} calories is low. Aim for 2,500-3,000 with high protein (1.6-2.2g/kg). Strength train 4-5x/week.".format(calories), "info"))

# Display tips with professional styling
tip_count = 0
for tip_text, tip_type in tips[:8]:  # Show max 8 most relevant tips
    tip_class = f"tip-{tip_type}"
    st.markdown(f"""
    <div class='tip-card {tip_class}'>
        {tip_text}
    </div>
    """, unsafe_allow_html=True)
    tip_count += 1

st.markdown("<br>", unsafe_allow_html=True)

# =========================================
# COMPLETE PROFILE SUMMARY
# =========================================
with st.expander("📋 View Complete Profile Details"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 👤 Personal Information")
        st.write(f"**Name:** {st.session_state.get('name', 'N/A')}")
        st.write(f"**Age:** {st.session_state.get('age', 'N/A')} years")
        st.write(f"**Gender:** {st.session_state.get('gender', 'N/A')}")
        st.write(f"**Height:** {st.session_state.get('height', 'N/A')} cm")
        st.write(f"**Weight:** {st.session_state.get('weight', 'N/A')} kg")
        
        st.markdown("### 🍽️ Nutrition & Diet")
        st.write(f"**Daily Calories:** {st.session_state.get('calories', 'N/A')} kcal")
        st.write(f"**Water Intake:** {st.session_state.get('water_intake', 'N/A')} glasses")
        st.write(f"**Dietary Preference:** {st.session_state.get('diet', 'N/A')}")
    
    with col2:
        st.markdown("### 😴 Sleep & Activity")
        st.write(f"**Sleep Time:** {st.session_state.get('sleep_time', 'N/A')}")
        st.write(f"**Wake Time:** {st.session_state.get('wake_time', 'N/A')}")
        st.write(f"**Sleep Duration:** {st.session_state.get('sleep_hours', 'N/A')} hours")
        st.write(f"**Screen Time:** {st.session_state.get('screen_time', 'N/A')} hours/day")
        st.write(f"**Activity Level:** {st.session_state.get('activity', 'N/A')}")
        
        st.markdown("### 🎯 Goals & Fitness")
        st.write(f"**Primary Goal:** {st.session_state.get('goal', 'N/A')}")
        st.write(f"**Target Weight:** {st.session_state.get('target_weight', 'N/A')} kg")
        st.write(f"**Exercise Days:** {st.session_state.get('exercise_days', 'N/A')} days/week")
        st.write(f"**Workout Type:** {st.session_state.get('workout', 'N/A')}")
        st.write(f"**Stress Level:** {st.session_state.get('stress', 'N/A')}")

st.markdown("<hr>", unsafe_allow_html=True)

# =========================================
# ACTION BUTTONS
# =========================================
st.markdown("<h2 class='section-header'>🚀 Next Steps</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📊 Main Dashboard", use_container_width=True, type="primary"):
        st.switch_page("pages/maindashboard.py")

with col2:
    if st.button("🏠 Go to Home", use_container_width=True):
        st.switch_page("app.py")

with col3:
    if st.button("⬅️ Edit Profile", use_container_width=True):
        st.session_state.step = 1
        st.switch_page("pages/onboarding.py")

# =========================================
# FOOTER
# =========================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p style='font-size: 1.1em; color: rgba(255, 255, 255, 0.9);'>
        💙 Small changes today create a healthier tomorrow
    </p>
    <p style='font-size: 0.9em; color: rgba(255, 255, 255, 0.7);'>
        Stay consistent • Track progress • Celebrate wins
    </p>
</div>
""", unsafe_allow_html=True)

