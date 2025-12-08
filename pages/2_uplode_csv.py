import streamlit as st
import pandas as pd
import joblib

st.title("📂 Upload Any File for Prediction")

model = joblib.load("KNN_heart.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("colunms.pkl")

uploaded = st.file_uploader("Upload your file", type=["csv", "xlsx", "xls", "txt", "json"])

if uploaded:
    file_type = uploaded.name.split(".")[-1]

    # ------------ Read different file types ------------
    if file_type == "csv":
        df = pd.read_csv(uploaded)

    elif file_type in ["xlsx", "xls"]:
        df = pd.read_excel(uploaded)

    elif file_type == "txt":
        df = pd.read_csv(uploaded, sep=None, engine="python")  # auto-detect separator

    elif file_type == "json":
        df = pd.read_json(uploaded)

    else:
        st.error("Unsupported file type!")
        st.stop()

    st.success(f"📄 File uploaded successfully: {uploaded.name}")
    st.write("### Preview:")
    st.dataframe(df.head())

    # ------------ Prepare Data for Prediction ------------
    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[expected_columns]

    scaled = scaler.transform(df)

    preds = model.predict(scaled)
    df["Prediction"] = preds

    # ------------ Display Result ------------
    st.write("### ✅ Predictions:")
    st.dataframe(df)

    # ------------ Download Output File ------------
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download Results (CSV)", csv, "heart_prediction_results.csv")
