# 🏏 IPL Win Predictor

An end-to-end machine learning application that predicts the **live win probability** of the batting team during an IPL T20 match. The project combines **XGBoost** for prediction with **SHAP explainability**, allowing users to understand the key factors influencing each prediction.

---

## 🚀 Features

- Live win probability prediction for ongoing IPL matches
- Built using an **XGBoost** classification model
- **SHAP-based explainability** highlighting the top factors influencing each prediction
- Input validation to prevent unrealistic match scenarios
- Interactive Streamlit interface with a scoreboard-inspired design
- FastAPI backend serving predictions through REST APIs

---

## 🛠️ Tech Stack

- Python
- XGBoost
- SHAP
- FastAPI
- Streamlit
- Pandas
- NumPy
- Joblib

---

## 📂 Project Structure

```
IPL-Win-Predictor/
│
├── app/
│   ├── api.py               # FastAPI backend
│   └── streamlit_app.py     # Streamlit frontend
│
├── data/
│   ├── matches.csv
│   └── deliveries.csv
│
├── notebooks/
│   └── ipl.ipynb            # Model training notebook
│
├── model.joblib             # Trained XGBoost model
├── columns.joblib           # Saved feature columns
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/IPL-Win-Predictor
