import streamlit as st
from datetime import datetime

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

# Function to get greeting based on time
def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning!"
    elif hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

# Streamlit App
def main():
    st.markdown(f"<h1 style='text-align: center; color: #003366;'>{get_greeting()}</h1>", unsafe_allow_html=True)
    st.subheader("Welcome to MVGAI! How can I assist you today?")

    # Dropdown menu for selection
    user_choice = st.selectbox("What would you like to explore?", ["Select an option..."] + list(MENU_OPTIONS.keys()))

    # Redirect automatically if an option is selected
    if user_choice != "Select an option...":
        url = MENU_OPTIONS[user_choice]
        st.markdown(f'<meta http-equiv="refresh" content="0;url={url}">', unsafe_allow_html=True)
        st.success(f"Redirecting to {user_choice}... 🚀")

if __name__ == "__main__":
    main()
