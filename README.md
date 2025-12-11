❤️ Heart Disease Prediction (ML + Streamlit App)

A machine learning–powered web application that predicts Heart Disease Risk using clinical attributes.
This project supports multiple input formats (CSV, Excel, PDF) and automatically processes patient records to classify:

🟥 HIGH RISK

🟩 NORMAL RISK

This repository includes the trained ML model, preprocessing pipeline, feature scaler, and a complete Streamlit web app.

⭐ Overview

Heart disease is one of the world’s leading causes of death. Early identification can save lives.
This project uses Machine Learning (KNN Classifier) to predict a patient's likelihood of heart disease based on common medical parameters.

The app allows users to upload patient records in multiple file formats. The data is cleaned, transformed, and passed to a trained ML model to produce predictions.

🚀 Features
🔍 1. Multi-File Support
You can upload:

CSV

XLSX / XLS (Excel)

🤖 2. Automatic Data Processing
Missing columns handled

Columns arranged properly

Data scaled using saved scaler.pkl

Model loaded from KNN_heart.pkl

❤️ 3. ML-Based Prediction
Model predicts:

1 → HIGH RISK

0 → NORMAL

💾 5. Downloadable Results
Output predictions can be downloaded as CSV.

🧠 Technologies Used
Component	Technology
Language	Python 3
ML Model	KNN Classifier
Frontend	Streamlit
Numerical Processing	NumPy / Pandas
Model Saving	Joblib
Scaling	StandardScaler

📦 Project Structure
graphql
Copy code
Heart-Disease-Predication/
│
├── app.py                # Streamlit application
├── KNN_heart.pkl         # Trained ML model
├── scaler.pkl            # StandardScaler object
├── colunms.pkl           # Expected columns list
├── heart.xls             # Sample dataset
├── heart.ipynb           # Jupyter notebook training code
└── .gitignore

▶️ Running the application
bash
Copy code
streamlit run app.py

👤 Author

Name: Niveditha 
Project: Heart Disease Risk Prediction (KNN Model)
GitHub: https://github.com/Nivedithagowda2

* Contribute
  Want to improve the project?
  requests are welcome!
