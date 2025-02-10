import streamlit as st
import webbrowser
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(override=True)

# Define website URLs for direct navigation
MENU_OPTIONS = {
    "Home": "https://mvg-innovations.com/",
    "About MVG Innovations": "https://mvg-innovations.com/about/",
    "Services": "https://mvg-innovations.com/services/",
    "Products": "https://mvg-innovations.com/products/", 
    "Careers": "https://mvg-innovations.com/careers/",
    "Achievements": "https://mvg-innovations.com/achievements/",
    "Learning Resources": "https://mvg-innovations.com/learning/",
    "Contact": "https://mvg-innovations.com/contact/"
}

# Custom CSS for a professional look
st.markdown("""
    <style>
    .stApp {
        background-color: #f5f7fa;
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .main-title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #003366;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def get_greeting():
    """Returns a dynamic greeting based on the time of day."""
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning!"
    elif hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

def main():
    """
    Streamlit app for instant website navigation.
    """
    # Greet the user
    st.markdown(f"<h1 class='main-title'>{get_greeting()}</h1>", unsafe_allow_html=True)
    st.subheader("Welcome to MVGAI! How can I assist you today?")

    # Dropdown menu to select an option
    user_choice = st.selectbox("What would you like to explore?", list(MENU_OPTIONS.keys()), index=None, placeholder="Select an option...")

    # If an option is selected, navigate immediately
    if user_choice:
        st.success(f"Redirecting you to **{user_choice}** now... 🚀")
        webbrowser.open_new_tab(MENU_OPTIONS[user_choice])

if __name__ == "__main__":
    main()
