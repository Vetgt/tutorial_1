import streamlit as st

# ----- PAGE SETUP -----
st.set_page_config(page_title="My Resume", page_icon="📄", layout="wide")

# ----- CUSTOM CSS -----
st.markdown(
    """
    <style>
    /* General page style */
    body {
        background-color: #f9f9f9;
        font-family: 'Segoe UI', sans-serif;
    }
    /* Header styling */
    .main-title {
        font-size: 2.5em;
        font-weight: bold;
        color: #2E86C1;
    }
    .subtitle {
        font-size: 1.2em;
        color: #555;
    }
    /* Card style */
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    /* Footer */
    .footer {
        text-align: center;
        color: grey;
        font-size: 0.9em;
        padding: 15px;
    }
    a {
        text-decoration: none;
        color: #1A5276;
    }
    a:hover {
        color: #117864;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----- HEADER -----
col1, col2 = st.columns([1, 3])

with col1:
    st.image("https://via.placeholder.com/150", caption="", use_container_width=True)

with col2:
    st.markdown("<div class='main-title'>Your Full Name</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>📍 City, Country</div>", unsafe_allow_html=True)
    st.write("✉ your.email@example.com | 📞 +6012-3456789")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourusername)")

st.markdown("---")

# ----- EDUCATION -----
st.markdown("### 🎓 Education")
st.markdown(
    """
    <div class="card">
        <b>Bachelor of Computer Science</b>, University Name (2020 – 2024)<br>
        - Major in Artificial Intelligence<br>
        - Dean’s List Award (2021, 2022)
    </div>
    """,
    unsafe_allow_html=True
)

# ----- EXPERIENCE -----
st.markdown("### 💼 Work Experience")
st.markdown(
    """
    <div class="card">
        <b>Software Intern</b>, Tech Company (Jun 2023 – Aug 2023)<br>
        - Developed internal dashboard using Python and Streamlit<br>
        - Automated data processing tasks (reduced manual work by 40%)<br>
        - Collaborated with the data team to deploy ML models
    </div>
    <div class="card">
        <b>Freelance Web Developer</b> (2022 – Present)<br>
        - Built personal and business websites using HTML, CSS, and JavaScript<br>
        - Customized WordPress themes and improved SEO performance
    </div>
    """,
    unsafe_allow_html=True
)

# ----- SKILLS -----
st.markdown("### 🧠 Skills")
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
st.markdown("### 🚀 Projects & Achievements")
st.markdown(
    """
    <div class="card">
        <b>Water Leakage Detection IoT System</b><br>
        - Designed IoT system using ESP8266 for real-time detection<br>
        - Integrated with a mobile app for instant notifications
    </div>
    <div class="card">
        <b>Twitter Hate Speech Detection</b><br>
        - Adapted a Transformer model to detect hate speech using PyTorch<br>
        - Achieved 90% accuracy on test data
    </div>
    """,
    unsafe_allow_html=True
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
