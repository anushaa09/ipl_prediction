from fastapi import FastAPI
import joblib
import pandas as pd
import shap
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
model = joblib.load(os.path.join(ROOT_DIR, 'model.joblib'))
columns = joblib.load(os.path.join(ROOT_DIR, 'columns.joblib'))
explainer = shap.Explainer(model)

@app.get("/")
def home():
    return {"message": "IPL Prediction API is running"}

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])
    if df['balls_left'].iloc[0] == 0:
        df['balls_left'] = 1

    df['run_rate'] = df['current_score'] / (120 - df['balls_left'])
    df['req_run_rate'] = (df['target'] - df['current_score']) / df['balls_left'] * 6

    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)

    prob = model.predict_proba(df)[0][1]
    shap_values = explainer(df)
    prob = model.predict_proba(df)[0][1]
    shap_values = explainer(df)

    shap_dict = dict(zip(df.columns, shap_values.values[0]))
    value_dict = dict(zip(df.columns, df.values[0]))

    top_features = sorted(
    [(str(k), float(v), float(value_dict[k])) for k, v in shap_dict.items()],
    key=lambda x: abs(x[1]),
    reverse=True
)[:3]

    return {
        "win_probability": float(prob),
        "top_factors": top_features
    }