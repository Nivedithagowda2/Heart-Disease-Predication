import streamlit as st

st.set_page_config(
    page_title="Heart Stroke Prediction",
    page_icon="❤️",
    layout="centered"
)

st.markdown("""
    <h1 style='text-align:center; color:#d11a2a;'>❤️ Heart Stroke Prediction System</h1>
    <p style='text-align:center; font-size:20px;'>
        Welcome! Use this app to predict your heart disease risk, upload CSV files, 
        view health suggestions, and more.
    </p>
""", unsafe_allow_html=True)

st.image("https://cdn-icons-png.flaticon.com/512/4894/4894602.png", width=300)

st.markdown("---")

st.markdown("""
### 📌 Available Features  
✔ Heart Disease Risk Prediction  
✔ Upload CSV for Bulk Predictions  
✔ Gauge Meter for Probability  
✔ AI-Based Health Suggestions  
✔ Multi-Page Navigation  
✔ Contact & About Pages  

Use the sidebar to navigate between pages ➡  
""")

