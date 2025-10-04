import streamlit as st

# ----- PAGE CONFIG -----
st.set_page_config(page_title="My Resume", page_icon="📄", layout="centered")

# ----- HEADER -----
col1, col2 = st.columns([1, 3], gap="large")

with col1:
    st.image("FOTO (3) (1).jpeg/150", caption="Betran Ramadhan P", use_container_width=True)  

with col2:
    st.subheader("📄 Resume")
    st.title("Your Full Name")
    st.markdown("""
    - 📍 Location: City, Country  
    - ✉ Email: your.email@example.com  
    - 📞 Phone: +6012-3456789  
    - 🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)  
    """)

st.divider()

# ----- EDUCATION -----
st.header("🎓 Education")
st.markdown("""
**Bachelor of Computer Science**, University Name (2020 – 2024)  
- Major in Artificial Intelligence  
- Dean’s List Award (2021, 2022)  
""")

st.divider()

# ----- WORK EXPERIENCE -----
st.header("💼 Work Experience")
st.markdown("""
**Software Intern**, Tech Company (Jun 2023 – Aug 2023)  
- Developed internal dashboard using Python and Streamlit  
- Automated data processing tasks, reducing manual work by 40%  
- Collaborated with the data team to deploy ML models  

**Freelance Web Developer** (2022 – Present)  
- Built personal and business websites using HTML, CSS, and JavaScript  
- Customized WordPress themes and improved SEO performance  
""")

st.divider()

# ----- SKILLS -----
st.header("🧠 Skills")
colA, colB = st.columns(2)

with colA:
    st.markdown("""
    - Python  
    - HTML / CSS / JavaScript  
    - Streamlit  
    """)

with colB:
    st.markdown("""
    - Machine Learning  
    - SQL  
    - Git & GitHub  
    """)

st.divider()

# ----- PROJECTS -----
st.header("🚀 Projects & Achievements")
st.markdown("""
**Water Leakage Detection IoT System**  
- Designed an IoT-based system using ESP8266 to detect water leakage in real time  
- Integrated with a mobile app for instant notifications  

**Twitter Hate Speech Detection**  
- Adapted a Transformer model to detect hate speech using PyTorch  
- Achieved 90% accuracy on test data  
""")

st.divider()

# ----- FOOTER -----
st.markdown(
    """
    <div style='text-align: center; color: grey; font-size: 0.9em;'>
        © 2025 Your Name | Built with ❤ using Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
