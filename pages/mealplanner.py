import streamlit as st

st.set_page_config(page_title="Meal Planner", page_icon="🍽️", layout="wide", initial_sidebar_state="expanded")

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
    .meal-card { background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.1)); backdrop-filter: blur(10px);
        border-radius: 12px; padding: 20px; margin: 10px 0; border: 1px solid rgba(255, 255, 255, 0.2); }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("# 🌟 Navigation")
    st.markdown("---")
    if st.button("📊 Dashboard", use_container_width=True): st.switch_page("pages/maindashboard.py")
    if st.button("📈 Progress Tracker", use_container_width=True): st.switch_page("pages/progress.py")
    if st.button("🎯 Goals Manager", use_container_width=True): st.switch_page("pages/goalmanager.py")
    if st.button("💪 Workout Library", use_container_width=True): st.switch_page("pages/workoutlibrary.py")
    if st.button("🍽️ Meal Planner", use_container_width=True, type="primary"): st.rerun()
    if st.button("🤖 AI Health Coach", use_container_width=True): st.switch_page("pages/aicoach.py")
    st.markdown("---")
    if st.button("🏠 Home", use_container_width=True): st.switch_page("app.py")

meals = {
    "Breakfast": [
        {"name": "Greek Yogurt Bowl", "calories": 350, "protein": "25g", "carbs": "45g", "fats": "8g", "time": "10 min",
         "ingredients": ["Greek yogurt", "Berries", "Granola", "Honey", "Almonds"]},
        {"name": "Protein Pancakes", "calories": 420, "protein": "30g", "carbs": "50g", "fats": "12g", "time": "15 min",
         "ingredients": ["Eggs", "Protein powder", "Banana", "Oats", "Cinnamon"]},
        {"name": "Avocado Toast", "calories": 380, "protein": "15g", "carbs": "40g", "fats": "20g", "time": "8 min",
         "ingredients": ["Whole grain bread", "Avocado", "Eggs", "Cherry tomatoes", "Feta cheese"]},
    ],
    "Lunch": [
        {"name": "Grilled Chicken Salad", "calories": 450, "protein": "40g", "carbs": "25g", "fats": "18g", "time": "20 min",
         "ingredients": ["Chicken breast", "Mixed greens", "Cherry tomatoes", "Cucumbers", "Olive oil dressing"]},
        {"name": "Quinoa Buddha Bowl", "calories": 500, "protein": "22g", "carbs": "60g", "fats": "16g", "time": "25 min",
         "ingredients": ["Quinoa", "Chickpeas", "Roasted veggies", "Tahini", "Spinach"]},
        {"name": "Turkey Wrap", "calories": 420, "protein": "35g", "carbs": "45g", "fats": "12g", "time": "10 min",
         "ingredients": ["Whole wheat wrap", "Turkey slices", "Lettuce", "Tomato", "Hummus"]},
    ],
    "Dinner": [
        {"name": "Salmon & Sweet Potato", "calories": 550, "protein": "42g", "carbs": "50g", "fats": "18g", "time": "30 min",
         "ingredients": ["Salmon fillet", "Sweet potato", "Broccoli", "Olive oil", "Lemon"]},
        {"name": "Chicken Stir-Fry", "calories": 480, "protein": "38g", "carbs": "45g", "fats": "14g", "time": "25 min",
         "ingredients": ["Chicken breast", "Mixed vegetables", "Brown rice", "Soy sauce", "Ginger"]},
        {"name": "Lean Beef Tacos", "calories": 520, "protein": "40g", "carbs": "48g", "fats": "18g", "time": "20 min",
         "ingredients": ["Lean ground beef", "Corn tortillas", "Lettuce", "Salsa", "Greek yogurt"]},
    ],
    "Snacks": [
        {"name": "Protein Smoothie", "calories": 280, "protein": "25g", "carbs": "35g", "fats": "6g", "time": "5 min",
         "ingredients": ["Protein powder", "Banana", "Almond milk", "Spinach", "Peanut butter"]},
        {"name": "Apple & Almond Butter", "calories": 220, "protein": "7g", "carbs": "28g", "fats": "10g", "time": "2 min",
         "ingredients": ["Apple", "Almond butter"]},
        {"name": "Cottage Cheese & Berries", "calories": 180, "protein": "18g", "carbs": "20g", "fats": "4g", "time": "3 min",
         "ingredients": ["Cottage cheese", "Mixed berries", "Honey"]},
    ]
}

st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h1 style='font-size: 3em; margin: 0;'>🍽️ Meal Planner</h1>
    <p style='font-size: 1.2em; margin-top: 10px;'>Plan your nutrition for optimal results</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🤖 Ask AI for Meal Suggestions", use_container_width=True, type="primary"):
        st.switch_page("pages/aicoach.py")

st.markdown("---")

st.markdown("## 📅 Weekly Meal Plan")

selected_day = st.selectbox("Select Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

st.markdown(f"### {selected_day}'s Meals")

for meal_type, meal_list in meals.items():
    st.markdown(f"#### {meal_type}")
    
    for idx, meal in enumerate(meal_list):
        with st.expander(f"{meal['name']} - {meal['calories']} kcal"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**⏱️ Prep Time:** {meal['time']}")
                st.markdown(f"**📊 Nutrition:** Protein: {meal['protein']} | Carbs: {meal['carbs']} | Fats: {meal['fats']}")
                st.markdown("**🛒 Ingredients:**")
                for ingredient in meal['ingredients']:
                    st.write(f"• {ingredient}")
            
            with col2:
                if st.button("Add to Plan", key=f"{meal_type}_{idx}", use_container_width=True):
                    st.success(f"✅ Added {meal['name']} to {selected_day}'s {meal_type}!")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("## 📊 Daily Nutrition Summary")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🔥 Calories", "1,800", "+200 vs target")
with col2:
    st.metric("🥩 Protein", "120g", "Target: 150g")
with col3:
    st.metric("🍞 Carbs", "200g", "Target: 220g")
with col4:
    st.metric("🥑 Fats", "60g", "Target: 70g")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <p style='font-size: 1em; color: rgba(255, 255, 255, 0.9);'>🍽️ You are what you eat. Make it count!</p>
</div>
""", unsafe_allow_html=True)
