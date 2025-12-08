import streamlit as st

st.title("💡 AI-based Heart Health Suggestions")

st.markdown("""
### ❤️ Daily Health Tips  
✔ Exercise 30 minutes daily  
✔ Reduce salt intake  
✔ Avoid smoking & alcohol  
✔ Maintain healthy weight  
✔ Monitor BP and cholesterol  
✔ Reduce stress and practice yoga  
✔ Sleep at least 7 hours  
""")

st.write("---")

st.subheader("💬 Personalized Advice")
age = st.slider("Your Age", 18, 100, 40)
bp = st.slider("Your Blood Pressure", 80, 200, 120)

if st.button("Get Advice"):
    if bp > 140:
        st.error("⚠ High BP detected! Reduce salt and consult a doctor.")
    else:
        st.success("✔ Your BP looks normal. Continue a healthy lifestyle.")
