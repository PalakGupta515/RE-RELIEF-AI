import streamlit as st

# ==============================================
# PAGE CONFIGURATION
# ==============================================
st.set_page_config(page_title="Login - Lifestyle Changer", page_icon="🔐", layout="centered")

# ==============================================
# CSS STYLING
# ==============================================
st.markdown("""
<style>
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

    .login-container {
        background: rgba(255,255,255,0.1);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        text-align: center;
        width: 380px;
        margin: auto;
        margin-top: 12vh;
        color: #fff;
    }

    input {
        color: black !important;
    }

    div[data-testid="stButton"] button {
        background: linear-gradient(90deg, #1E3C72, #2A5298);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 0.6rem 2rem;
        font-size: 1rem;
        transition: all 0.3s ease;
    }

    div[data-testid="stButton"] button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #2A5298, #1E3C72);
    }

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
# USER STORAGE USING SESSION STATE
# ==============================================
if "users" not in st.session_state:
    st.session_state["users"] = {"palak": "1234", "test": "pass"}

users = st.session_state["users"]

# ==============================================
# LOGIN / SIGNUP LOGIC
# ==============================================
st.markdown("<div class='login-container'>", unsafe_allow_html=True)
st.title("Welcome to Lifestyle Changer! ")

# Tabs for Sign In / Sign Up
tab1, tab2 = st.tabs(["🔑 Sign In", "🆕 Sign Up"])

with tab1:
    username = st.text_input("Username", key="login_user")
    password = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login"):
        if not username or not password:
            st.warning("⚠️ Please fill in all fields.")
        elif username not in users:
            st.error("❌ Username not found. Please sign up first.")
        elif users[username] != password:
            st.error("❌ Incorrect password. Try again.")
        else:
            st.success(f"✅ Welcome, {username}! Redirecting...")
            st.session_state["username"] = username
            st.switch_page("pages/info.py")  # 🔹 Redirects after login

with tab2:
    new_user = st.text_input("New Username", key="signup_user")
    new_pass = st.text_input("New Password", type="password", key="signup_pass")

    if st.button("Create Account"):
        if not new_user or not new_pass:
            st.warning("⚠️ All fields are required!")
        elif new_user in users:
            st.error("⚠️ Username already exists.")
        else:
            st.session_state["users"][new_user] = new_pass
            st.success("🎉 Account created successfully! Please go to Sign In tab.")

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Made with 💙</div>", unsafe_allow_html=True)
