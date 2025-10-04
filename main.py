import streamlit as st

# ----- PAGE CONFIG -----
st.set_page_config(page_title="My Resume", page_icon="📄", layout="centered")

# ----- HEADER -----
col1, col2 = st.columns([1, 3], gap="large")

with col1:
    st.image("foto_pp.jpeg", caption="Betran Ramadhan Prasetyo", use_container_width=True)  

with col2:
    st.subheader("📄 Resume")
    st.title("BETRAN RAMADHAN PRASETYO")
    st.markdown("""
    - 📍 JATIASIH: KOTA BEKASI, INDONESIA 
    - ✉ Email: betranwork@gmail.com  
    - 📞 Phone: +62895327717859  
    - 🔗 [LinkedIn](https://linkedin.com/in/) | [GitHub](https://github.com/Vetgt)  
    """)

st.divider()

# ----- EDUCATION -----
st.header("🎓 Education")
st.markdown("""
**Bachelor of AI**, University Malaysia Kelantan (2025-2026)  
- Major in Artificial Intelligence  
""")

st.divider()

# ----- WORK EXPERIENCE -----
st.header("💼 Work Experience")
st.markdown("""
**Software Developer**,(Feb 2025 – June 2025)  
- Developed internal dashboard using flutter and python with firebase database
- Automated data processing tasks, reducing manual work by 50%  
- Collaborated with the data team to deploy ML models  

**Design 3d Using Blender** (2021 – 2022)  
- Built 3d animation 
- Consult Design Model 3d
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
    - Java
    - Flask
    """)

with colB:
    st.markdown("""
    - Machine Learning  
    - SQL  
    - Git & GitHub
    - Flutter
    - Deep learning
    """)

st.divider()

# ----- PROJECTS -----
st.header("🚀 Projects & Achievements")
st.markdown("""
**AUTOMATED SMART SPRINK WATER**  
- Designed an IoT-based system using ESP32 to detect soil and automation spring real time  
- Integrated with a mobile app for instant notifications  

**Twitter emotion  Detection**  
- Adapted a Transformer model to detect emotion comment using PyTorch  
- Achieved 93% accuracy on test data  
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
