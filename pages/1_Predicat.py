import streamlit as st
import pandas as pd
import joblib
import time

model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("colunms.pkl")

st.title("🔍 Predict Your Heart Disease Risk")

st.write("Fill the details below:")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 100, 40)
    sex = st.selectbox("Sex", ["M", "F"])
    chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
    resting_bp = st.number_input("Resting BP", 80, 200, 120)
    cholesterol = st.number_input("Cholesterol", 100, 600, 200)

with col2:
    fasting_bs = st.selectbox("Fasting Sugar > 120 mg/dl", [0, 1])
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    max_hr = st.slider("Max Heart Rate", 60, 220, 150)
    exercise_angina = st.selectbox("Exercise Angina", ["Y", "N"])
    oldpeak = st.slider("Oldpeak", 0.0, 6.0, 1.0)
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict Risk"):

    raw_input = {
        "Age": age, "RestingBP": resting_bp, "Cholesterol": cholesterol,
        "FastingBS": fasting_bs, "MaxHR": max_hr, "Oldpeak": oldpeak,
        f"Sex_{sex}": 1,
        f"ChestPainType_{chest_pain}": 1,
        f"RestingECG_{resting_ecg}": 1,
        f"ExerciseAngina_{exercise_angina}": 1,
        f"ST_Slope_{st_slope}": 1
    }

    df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[expected_columns]

    scaled = scaler.transform(df)

    # ---- Animated progress bar ----
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    prediction = model.predict(scaled)[0]

    # ---- Probability Gauge ----
    prob = model.predict_proba(scaled)[0][1] * 100
    st.write("---")
    st.subheader("📊 Risk Probability Gauge")
    st.progress(int(prob))

    # ----- Result -----
    if prediction == 1:
        st.error(f"⚠ High Risk! ({prob:.2f}% probability)")
    else:
        st.success(f"✅ Low Risk ({prob:.2f}% probability)")
        
