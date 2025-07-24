import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and get feature columns
model = joblib.load('recurrence_model.pkl')
feature_col = model.get_booster().feature_names

# Configure page
st.set_page_config(page_title="Thyroid Cancer Recurrence Detector", layout="wide")

# Title section
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
    }
    .title {
        font-size: 48px;
        font-weight: 700;
        text-align: center;
        color: #4b0082;
        padding-bottom: 10px;
    }
    .subheader {
        font-size: 20px;
        text-align: center;
        color: #ffffff;
        padding-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🩺 Detect Thyroid Cancer Reoccurrence</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Predict whether a thyroid cancer patient is likely to experience recurrence using clinical data</div>', unsafe_allow_html=True)
st.write("---")

# Sidebar inputs
st.sidebar.header("📋 Patient Data Input")

def user_input_features():
    age = st.sidebar.slider("Age", 1, 100, 35)
    gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
    smoking = st.sidebar.selectbox("Smoking", ["Yes", "No"])
    hx_smoking = st.sidebar.selectbox("History of Smoking", ["Yes", "No"])
    hx_radiotherapy = st.sidebar.selectbox("History of Radiotherapy", ["Yes", "No"])
    focality = st.sidebar.selectbox("Focality", ["Unifocal", "Multifocal"])
    risk = st.sidebar.selectbox("Risk Level", ["Low", "Intermediate", "High"])
    t = st.sidebar.slider("Tumor size stage (T)", 1, 4, 1)
    n = st.sidebar.slider("Lymph node involvement stage (N)", 0, 1, 0)
    m = st.sidebar.slider("Metastasis stage (M)", 0, 1, 0)
    stage = st.sidebar.selectbox("Overall Stage", ["I", "II", "III", "IV"])

    thyroid_function = st.sidebar.selectbox("Thyroid Function", [
        "Clinical Hyperthyroidism", "Clinical Hypothyroidism", "Euthyroid",
        "Subclinical Hyperthyroidism", "Subclinical Hypothyroidism"
    ])

    physical_exam = st.sidebar.selectbox("Physical Examination", [
        "Diffuse goiter", "Multinodular goiter", "Normal",
        "Single nodular goiter-left", "Single nodular goiter-right"
    ])

    adenopathy = st.sidebar.selectbox("Adenopathy", [
        "Bilateral", "Extensive", "Left", "No", "Posterior", "Right"
    ])

    pathology = st.sidebar.selectbox("Pathology", [
        "Follicular", "Hurthel cell", "Micropapillary", "Papillary"
    ])

    response = st.sidebar.selectbox("Response", [
        "Biochemical Incomplete", "Excellent", "Indeterminate", "Structural Incomplete"
    ])

    data = {
        'Age': age,
        'Gender': 1 if gender == "Male" else 0,
        'Smoking': 1 if smoking == "Yes" else 0,
        'Hx Smoking': 1 if hx_smoking == "Yes" else 0,
        'Hx Radiothreapy': 1 if hx_radiotherapy == "Yes" else 0,
        'Focality': 1 if focality == "Multifocal" else 0,
        'Risk': {"Low": 0, "Intermediate": 1, "High": 2}[risk],
        'T': t,
        'N': n,
        'M': m,
        'Stage': {"I": 1, "II": 2, "III": 3, "IV": 4}[stage],
        f'Thyroid Function_{thyroid_function}': 1,
        f'Physical Examination_{physical_exam}': 1,
        f'Adenopathy_{adenopathy}': 1,
        f'Pathology_{pathology}': 1,
        f'Response_{response}': 1,
    }

    for col in feature_col:
        if col not in data:
            data[col] = 0

    return pd.DataFrame([data])[feature_col]

# Get input
input_df = user_input_features()

# Prediction
if st.button("🔍 Predict Recurrence"):
    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][prediction]

    if prediction == 1:
        st.markdown(f"""
            <div style='
                background-color: #fdecea;
                border-radius: 10px;
                padding: 20px;
                color: #611a15;
                font-size: 20px;
                font-weight: 500;
                '>
                ⚠️ <b>High Risk:</b> Cancer is likely to recur.<br><br>
                <i>Confidence:</i> <b>{prob*100:.2f}%</b>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style='
                background-color: #d4f4dd;
                border-radius: 10px;
                padding: 20px;
                color: #1b4332;
                font-size: 20px;
                font-weight: 500;
                '>
                ✅ <b>Good Prognosis:</b> Cancer is <b>not</b> likely to recur.<br><br>
                <i>Confidence:</i> <b>{prob*100:.2f}%</b>
            </div>
        """, unsafe_allow_html=True)

# Show input for reference
with st.expander("📊 See Input Data Used"):
    st.dataframe(input_df)
"AIzaSyBTaJz0gRurmYQ6xjpW0AqMcj83GrA0qBA"