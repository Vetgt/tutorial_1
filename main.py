import streamlit as st

# ----- PAGE SETUP -----
st.set_page_config(page_title="My Resume", page_icon="📄", layout="centered")

# ----- CUSTOM CSS -----
st.markdown(
    """
    <style>
    body {
        font-family: 'Segoe UI', sans-serif;
        color: #2c3e50;
        background-color: #f7f9fc;
    }
    .section-title {
        font-size: 1.5em;
        font-weight: bold;
        color: #1a5276;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .card {
        background-color: #ffffff;
        padding: 15px 20px;
        border-radius: 8px;
        border-left: 4px solid #1a5276;
        margin-bottom: 15px;
    }
    .footer {
        text-align: center;
        color: grey;
        font-size: 0.85em;
        margin-top: 30px;
    }
    a {
        text-decoration: none;
        color: #1a5276;
    }
    a:hover {
        color: #0e6655;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----- HEADER -----
col1, col2 = st.columns([1, 3])

with col1:
    st.image("https://via.placeholder.com/150", use_container_width=True)

with col2:
    st.markdown("## Your Full Name")
    st.write("📍 City, Country")
    st.write("✉ your.email@example.com | 📞 +6012-3456789")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)")

st.markdown("---")

# ----- EDUCATION -----
st.markdown("<div class='section-title'>🎓 Education</div>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="card">
        <b>Bachelor of Computer Science</b>, University Name (2020 – 2024)<br>
        - Major in Artificial Intelligence<br>
        - Dean’s List Award (2021, 2022)
    </div>
    """, unsafe_allow_html=True
)

# ----- EXPERIENCE -----
st.markdown("<div class='section-title'>💼 Work Experience</div>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="card">
        <b>Software Intern</b>, Tech Company (Jun 2023 – Aug 2023)<br>
        - Developed internal dashboard using Python and Streamlit<br>
        - Automated data processing tasks (reduced manual work by 40%)<br>
        - Collaborated with data team to deploy ML models
    </div>
    <div class="card">
        <b>Freelance Web Developer</b> (2022 – Present)<br>
        - Built websites using HTML, CSS, JavaScript<br>
        - Customized WordPress themes & improved SEO
    </div>
    """, unsafe_allow_html=True
)

# ----- SKILLS -----
st.markdown("<div class='section-title'>🧠 Skills</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        <div class="card">
            - Python<br>
            - HTML / CSS / JavaScript<br>
            - Streamlit
        </div>
        """, unsafe_allow_html=True)
with col2:
    st.markdown(
        """
        <div class="card">
            - Machine Learning<br>
            - SQL<br>
            - Git & GitHub
        </div>
        """, unsafe_allow_html=True)

# ----- PROJECTS -----
st.markdown("<div class='section-title'>🚀 Projects & Achievements</div>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="card">
        <b>Water Leakage Detection IoT System</b><br>
        - Designed IoT system using ESP8266 for real-time detection<br>
        - Integrated with mobile app for instant notifications
    </div>
    <div class="card">
        <b>Twitter Hate Speech Detection</b><br>
        - Adapted Transformer model using PyTorch<br>
        - Achieved 90% accuracy on test data
    </div>
    """, unsafe_allow_html=True
)

# ----- FOOTER -----
st.markdown(
    """
    <div class="footer">
        © 2025 Your Name | Built with ❤ using Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
