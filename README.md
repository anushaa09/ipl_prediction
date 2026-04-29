IPL Win Predictor
A machine learning web app that predicts the win probability of a batting team during a live IPL T20 match, with explainability powered by SHAP.


#Tech Stack

Python
XGBoost
SHAP
FastAPI
Streamlit

#Project Structure
IPL Prediction/
├── app/
│   ├── api.py          # FastAPI backend
│   └── streamlit_app.py  # Streamlit frontend
├── data/
│   ├── matches.csv
│   └── deliveries.csv
├── notebooks/
│   └── ipl.ipynb       # Model training notebook
├── model.joblib        # Trained XGBoost model
├── columns.joblib      # Feature columns
└── requirements.txt
How to Run
1. Install dependencies
bashpip install -r requirements.txt
2. Start the FastAPI backend
bashuvicorn app.api:app --reload
3. Start the Streamlit frontend
bashstreamlit run app/streamlit_app.py
Open your browser at http://localhost:8501
Features

Predicts win probability based on live match state (score, balls left, wickets, target)
Input validation to catch unrealistic match scenarios
Top 3 SHAP factors shown per prediction, with actual feature values
Dark scoreboard-style UI

#Model
Trained on IPL match data using XGBoost. Features used:

Batting team and bowling team
City
Current score
Balls left
Wickets lost
Target
Current run rate
Required run rate