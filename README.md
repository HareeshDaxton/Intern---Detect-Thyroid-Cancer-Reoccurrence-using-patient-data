# 🩺 Thyroid Cancer Recurrence Prediction App

This project presents an end-to-end **clinical decision support tool** built with `Streamlit`, aimed at **predicting the recurrence of thyroid cancer** in patients based on clinical, pathological, and demographic features.

> 🧠 Powered by Machine Learning (XGBoost) and designed to aid doctors in identifying high-risk patients with a user-friendly web interface.

---

## 🔍 Problem Statement

Thyroid cancer is one of the most common endocrine malignancies. While the prognosis is usually excellent, recurrence is not uncommon and requires careful monitoring. The objective of this project is to **predict recurrence risks** in patients using historical clinical and pathological data. Early prediction enables tailored treatment planning and more effective patient care.

---

## 📁 Project Structure

```bash
├── app.py                  # Streamlit app frontend
├── MAIN.ipynb             # Main notebook for model training
├── EDA_and_FE.ipynb       # EDA & Feature Engineering notebook
├── dataset.csv            # Raw data file
├── Cleaned_dataset.csv    # Processed/cleaned dataset
├── recurrence_model.pkl   # Trained XGBoost model
└── README.md              # Project overview and documentation
```

---

## 🧪 Technologies Used

- **Python 3.11.5**
- **Pandas** & **NumPy** — Data handling
- **Matplotlib** & **Seaborn** — Data visualization
- **XGBoost** — Classification Model
- **Scikit-learn** — Preprocessing & Evaluation
- **Streamlit** — Web-based User Interface
- **Joblib** — Model Serialization

---

## 📊 Features

- Interactive sidebar input for patient clinical data
- Real-time recurrence prediction using trained model
- Shows predicted risk along with confidence score
- Elegant user interface with color-coded feedback
- Expandable section to display model input for transparency

---

## 🧬 Input Features Used

The model takes in a combination of **demographics**, **tumor staging**, **pathology**, **thyroid function**, and **radiotherapy history**. Key features include:

- Age, Gender, Smoking History
- Tumor Stages (T, N, M)
- Overall Stage, Risk level
- Thyroid Function Status
- Physical Examination Results
- Pathological Type
- Response to Initial Therapy
- Presence of Adenopathy

---
## 📈 Model Details

- **Model**: XGBoost Classifier
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-Score, ROC-AUC
- **Performance**: Achieved high predictive confidence on test data with effective handling of categorical inputs via one-hot encoding

---

## 📌 Future Improvements

- Add user authentication and patient data history
- Integrate clinical deployment on Heroku or AWS
- Enable support for more advanced visual analytics for physicians
- Build REST API endpoints for EHR system integration

-

## 📄 License

This project is open-source and available under the MIT License

---

## 🧠 Ethical Note

This tool is intended for **research and educational purposes**. It should **not** be used as a replacement for professional medical diagnosis or treatment. Always consult a certified healthcare provider.


