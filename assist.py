import streamlit as st
import re
from streamlit_option_menu import option_menu

def validate_name(name):
    return bool(re.match(r'^[A-Za-z ]+$', name))

def validate_email(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

def validate_contact(contact):
    return bool(re.match(r'^[0-9]{10}$', contact))

def get_user_details():
    st.set_page_config(page_title="MVG Innovations", page_icon="🚀")
    st.markdown(
        """
        <style>
            .main-title {
                text-align: center;
                font-size: 36px;
                color: #4A90E2;
            }
            .sub-title {
                text-align: center;
                font-size: 20px;
                color: #555;
            }
            .stTextInput>div>div>input {
                border-radius: 10px;
                border: 1px solid #4A90E2;
                padding: 10px;
            }
            .stButton>button {
                background-color: #4A90E2;
                color: white;
                border-radius: 10px;
                font-size: 18px;
                padding: 10px 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown("<h1 class='main-title'>Welcome to MVG Innovations</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='sub-title'>Please provide us with your details to proceed.</h3>", unsafe_allow_html=True)
    
    if "details_filled" not in st.session_state:
        st.session_state.details_filled = False
    
    if not st.session_state.details_filled:
        name = st.text_input("Name:")
        email = st.text_input("Email ID:")
        contact_number = st.text_input("Contact Number:")
        
        if st.button("Submit"):
            if not validate_name(name):
                st.error("Please enter a valid name (only alphabets and spaces).")
            elif not validate_email(email):
                st.error("Please enter a valid email address.")
            elif not validate_contact(contact_number):
                st.error("Please enter a valid 10-digit contact number.")
            else:
                st.session_state.details_filled = True
                st.session_state.name = name
                st.session_state.email = email
                st.session_state.contact_number = contact_number
                st.success(f"Hello {name}, Welcome to MVG Innovations! 🎉")
                st.rerun()

    
def display_section(section):
    if section == "Home":
        st.title("Welcome to MVG Innovations")
        st.write("MVG Innovations is an IT company focused on consulting, product/project development, IT services, digital transformation, and more.")
    elif section == "About":
        st.title("About Us")
        st.write("MVG Innovations is a next-generation digital, consulting, and technology company based in Hyderabad, Telangana. We leverage advanced \
        technologies such as Artificial Intelligence (AI), Big Data, Business Analytics, Cloud Solutions, and the Internet of Things (IoT) to address\
         our clients' business challenges. Our services include Digital Transformation, Digital Marketing, and Professional Training, enabling firms \
            to adapt to the rapidly changing world. Recognized as a startup by the Department for Promotion of Industry and Internal Trade (DPIIT), \
                Ministry of Commerce & Industry, Government of India, we have been honored with awards such as the Top Placer in Information Technology \
                    by the GoGlobal Awards 2021 and named one of the Top Global Businesses of the Year 2022 in the IT Consulting Category by Great Companies.")
    elif section == "Services":
        st.title("Our Services")
        st.write("We offer a wide range of services including:")
        st.write("- Analytics and AI")
        st.write("- Consulting")
        st.write("- Digital Transformation")
        st.write("- Infrastructure")
        st.write("MVG Innovations provides a comprehensive range of services to cater to diverse business needs. Our Consulting services help strategize solutions across technology, \
        management, and operations to meet business objectives. We specialize in App Development & Maintenance, designing, developing, modifying, and maintaining software applications tailored to specific requirements. \
            Leveraging AI & Deep Learning, we implement advanced technologies to solve complex business challenges. Our Aviation Analytics solutions are designed specifically for the aviation industry, \
                while Restaurant Analytics provides data-driven insights to optimize restaurant operations and enhance customer experiences. Through Digital Marketing Services, we offer marketing solutions to boost leads and revenue.\
                     Additionally, we provide Training programs to equip individuals and organizations with the latest technological skills. Our Help & Support team ensures 24/7 assistance to resolve issues and maintain seamless business operations.")
    elif section == "Products":
        st.title("Our Products")
        st.write("Explore our products:")
        st.write("- Restaurant Analytics")
        st.write("- Retail Analytics")
        st.write("- Attendance System")
        st.write("- ChatBot")
    elif section == "Careers":
        st.title("Careers")
        st.write("Join our team and be a part of our innovative journey.")
    elif section == "Achievements":
        st.title("Achievements")
        st.write("MVG Innovations has been recognized for excellence in IT services, winning the **Global Award for IT Services 2022** by Great Companies. With a strong commitment to innovation and quality, \
        we have built a reputation for delivering cutting-edge solutions in AI, analytics, and digital transformation. Our dedicated team of expert data scientists and senior consultants from top IT firms and institutions drive our success. \
            We take pride in our **outstanding employee satisfaction**, being highly rated for work-life balance and professional growth. These achievements reflect our continuous pursuit of excellence, innovation, and customer success.")
    elif section == "Contact":
        st.title("Contact Us")
        st.write("Get in touch with us:")
        st.write("Email: info@mvg-innovations.com")
        st.write("Phone: +91 88019 33416")
        st.write("Address: T-Hub Phase 2, Inorbit Mall Rd, Vittal Rao Nagar, Madhapur, Hyderabad, Telangana 500081")
    elif section == "Learning":
        st.title("Learning")
        st.write("MVG Innovations offers a range of professional courses designed to equip individuals with in-demand skills. Our **Python Programming** course provides hands-on training in coding, automation, and software development.\
          The Data Science program covers key methodologies, including machine learning, statistical analysis, and predictive modeling, using industry-standard tools like Python and R. \
            Our Data Analysis course focuses on extracting meaningful insights from data, utilizing visualization tools and techniques for informed decision-making. \
                The Artificial Intelligence (AI) course delves into deep learning, neural networks, and AI-driven solutions, helping learners master advanced AI technologies. \
                    Additionally, our Digital Marketing course provides expertise in SEO, social media marketing, and online advertising strategies to enhance business growth. \
                        Each course includes live projects, mentorship, and certification to ensure a practical and career-oriented learning experience.")

def main():
    if "details_filled" not in st.session_state:
        st.session_state.details_filled = False
    
    if not st.session_state.details_filled:
        get_user_details()
    else:
        
        st.sidebar.title("Navigation")
        
        menu_options = ["Home", "About", "Services", "Products", "Careers", "Achievements", "Contact", "Learning"]
        choice = st.sidebar.selectbox("Main Menu", menu_options)
        
        display_section(choice)

if __name__ == "__main__":
    main()
