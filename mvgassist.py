import streamlit as st
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(override=True)

# Define chatbot responses
MENU_RESPONSES = {
    
    "home": "MVG Innovations is a leader in AI-driven solutions, providing cutting-edge technology and innovative services across industries.",
    "about": "MVG Innovations is a next-generation digital, consulting, and technology company based in Hyderabad, Telangana. We leverage advanced \
        technologies such as Artificial Intelligence (AI), Big Data, Business Analytics, Cloud Solutions, and the Internet of Things (IoT) to address\
         our clients' business challenges. Our services include Digital Transformation, Digital Marketing, and Professional Training, enabling firms \
            to adapt to the rapidly changing world. Recognized as a startup by the Department for Promotion of Industry and Internal Trade (DPIIT), \
                Ministry of Commerce & Industry, Government of India, we have been honored with awards such as the Top Placer in Information Technology \
                    by the GoGlobal Awards 2021 and named one of the Top Global Businesses of the Year 2022 in the IT Consulting Category by Great Companies.",
    "services": "MVG Innovations provides a comprehensive range of services to cater to diverse business needs. Our Consulting services help strategize solutions across technology, \
        management, and operations to meet business objectives. We specialize in App Development & Maintenance, designing, developing, modifying, and maintaining software applications tailored to specific requirements. \
            Leveraging AI & Deep Learning, we implement advanced technologies to solve complex business challenges. Our Aviation Analytics solutions are designed specifically for the aviation industry, \
                while Restaurant Analytics provides data-driven insights to optimize restaurant operations and enhance customer experiences. Through Digital Marketing Services, we offer marketing solutions to boost leads and revenue.\
                     Additionally, we provide Training programs to equip individuals and organizations with the latest technological skills. Our Help & Support team ensures 24/7 assistance to resolve issues and maintain seamless business operations.",
    "products": "MVG Innovations offers a range of technology-driven products designed to enhance business operations. \
        Restaurant Analytics platform provides data-driven insights to optimize operations, manage inventory, and enhance customer experiences. \
            Retail Analytics delivers actionable insights into sales trends, customer behavior, and inventory management, helping retailers make informed decisions. \
                The Attendance System offers a reliable way to track employee attendance, streamline payroll processes, and ensure compliance. \
                    Additionally, their AI-powered ChatBot enhances customer engagement by providing instant responses to inquiries and improving user experience on digital platforms.",
    "achievements": "MVG Innovations has been recognized for excellence in IT services, winning the **Global Award for IT Services 2022** by Great Companies. With a strong commitment to innovation and quality, \
        we have built a reputation for delivering cutting-edge solutions in AI, analytics, and digital transformation. Our dedicated team of expert data scientists and senior consultants from top IT firms and institutions drive our success. \
            We take pride in our **outstanding employee satisfaction**, being highly rated for work-life balance and professional growth. These achievements reflect our continuous pursuit of excellence, innovation, and customer success.",
    "learning": "MVG Innovations offers a range of professional courses designed to equip individuals with in-demand skills. Our **Python Programming** course provides hands-on training in coding, automation, and software development.\
          The Data Science program covers key methodologies, including machine learning, statistical analysis, and predictive modeling, using industry-standard tools like Python and R. \
            Our Data Analysis course focuses on extracting meaningful insights from data, utilizing visualization tools and techniques for informed decision-making. \
                The Artificial Intelligence (AI) course delves into deep learning, neural networks, and AI-driven solutions, helping learners master advanced AI technologies. \
                    Additionally, our Digital Marketing course provides expertise in SEO, social media marketing, and online advertising strategies to enhance business growth. \
                        Each course includes live projects, mentorship, and certification to ensure a practical and career-oriented learning experience.",
    "contact": "Address: T-Hub Phase 2, Inorbit Mall Rd, Vittal Rao Nagar, Madhapur, Hyderabad, Telangana 500081\
        Email: info@mvg-innovations.com\
            Phone: +91 88019 33416"
}


# Function to get a greeting based on the time of day
def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning!"
    elif hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

# Streamlit app
def main():
    st.set_page_config(page_title="MVGAI ChatBot", layout="centered")

    # Sidebar with branding
    with st.sidebar:
        st.image("C://Users//abhir//OneDrive//Desktop//mvg_innovations_logo.jpg", width=200)
        st.markdown("### MVG Innovations 🤖")
        st.markdown("AI-powered chatbot to assist you with queries.")
        st.divider()

    # Chat header
    st.title("💬 MVGAI ChatBot")
    st.markdown(f"**{get_greeting()}** Welcome to MVGAI! How can I assist you today?")
    
    # Display available topics
    st.markdown("""
        **You can ask about:**  
        - Home  
        - About  
        - Services  
        - Products  
        - Achievements  
        - Learning  
        - Contact  
    """)

    # Chat conversation
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input field
    user_query = st.chat_input("Type your question here...")

    if user_query:
        # Store user query
        st.session_state.messages.append({"role": "user", "content": f"{user_query}"})
        with st.chat_message("user"):
            st.markdown(f"{user_query}")

        # Process query
        matched_response = None
        for key, response in MENU_RESPONSES.items():
            if key in user_query.lower():
                matched_response = response
                break

        # Bot response
        bot_response = matched_response if matched_response else "⚠️ Sorry, I didn't understand. Please ask about one of the topics above."
        st.session_state.messages.append({"role": "assistant", "content": f"🤖 {bot_response}"})
        with st.chat_message("assistant"):
            st.markdown(f"🤖 {bot_response}")

if __name__ == "__main__":
    main()