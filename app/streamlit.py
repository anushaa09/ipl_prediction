import streamlit as st
import requests

st.set_page_config(page_title="IPL Win Predictor", layout="centered", page_icon="🏏")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;600;700&family=IBM+Plex+Mono:wght@400;600&display=swap');

/* ── Full-page dark background ── */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #070c17 !important;
}
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stMain"] { background-color: #070c17; }

/* ── Remove default padding ── */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    max-width: 780px;
}

/* ── Global font ── */
html, body, * {
    font-family: 'Rajdhani', sans-serif !important;
}

/* ── Header banner ── */
.header-banner {
    background: #0d1b2e;
    border: 1px solid #1e2d4a;
    border-bottom: 2px solid #f59e0b;
    border-radius: 12px 12px 0 0;
    padding: 18px 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0;
}
.header-title {
    font-size: 28px;
    font-weight: 700;
    color: #f59e0b;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin: 0;
}
.header-sub {
    font-size: 11px;
    color: #475569;
    font-family: 'IBM Plex Mono', monospace !important;
    letter-spacing: 2px;
    margin-top: 2px;
}
.live-badge {
    background: #dc2626;
    color: #fff;
    font-size: 11px;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 4px;
    letter-spacing: 2px;
    font-family: 'IBM Plex Mono', monospace !important;
    animation: blink 1.5s infinite;
}
@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
}

/* ── Card sections ── */
.card-section {
    background: #0a0e1a;
    border: 1px solid #1e2d4a;
    border-top: none;
    padding: 20px 28px;
}
.card-section-last {
    border-radius: 0 0 12px 12px;
}

/* ── Section labels ── */
.section-label {
    font-size: 10px;
    color: #475569;
    font-family: 'IBM Plex Mono', monospace !important;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

/* ── Selectbox and inputs ── */
[data-baseweb="select"] > div {
    background: #0f1e30 !important;
    border: 1px solid #1e3a5f !important;
    border-radius: 8px !important;
    color: #e2e8f0 !important;
}
[data-baseweb="select"] * { color: #e2e8f0 !important; }

[data-testid="stNumberInput"] input {
    background: #0f1e30 !important;
    border: 1px solid #1e3a5f !important;
    border-radius: 8px !important;
    color: #f59e0b !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 22px !important;
    font-weight: 600 !important;
    text-align: center !important;
}

/* ── Labels ── */
label, [data-testid="stWidgetLabel"] p {
    color: #64748b !important;
    font-size: 12px !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
}

/* ── Predict button ── */
[data-testid="stButton"] > button {
    background: #f59e0b !important;
    color: #070c17 !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 17px !important;
    font-weight: 700 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    padding: 12px 36px !important;
    width: 100%;
    transition: all 0.15s;
}
[data-testid="stButton"] > button:hover {
    background: #fbbf24 !important;
    transform: scale(1.02);
}

/* ── Metric (probability) ── */
[data-testid="stMetric"] {
    background: #0f1e30 !important;
    border: 1px solid #1e3a5f !important;
    border-radius: 10px !important;
    padding: 16px 20px !important;
}
[data-testid="stMetricValue"] {
    color: #f59e0b !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 48px !important;
    font-weight: 700 !important;
}
[data-testid="stMetricLabel"] {
    color: #475569 !important;
    font-size: 11px !important;
    letter-spacing: 2px !important;
}

/* ── Progress bar ── */
[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, #f59e0b, #ef4444) !important;
    border-radius: 4px !important;
}
[data-testid="stProgressBar"] > div {
    background: #1e2d4a !important;
    height: 8px !important;
    border-radius: 4px !important;
}

/* ── Success/Error boxes ── */
[data-testid="stSuccess"] {
    background: rgba(34, 197, 94, 0.08) !important;
    border: 1px solid rgba(34, 197, 94, 0.25) !important;
    border-radius: 8px !important;
    color: #4ade80 !important;
}
[data-testid="stError"] {
    background: rgba(239, 68, 68, 0.08) !important;
    border: 1px solid rgba(239, 68, 68, 0.25) !important;
    border-radius: 8px !important;
    color: #f87171 !important;
}

/* ── Divider ── */
hr {
    border-color: #1e2d4a !important;
    margin: 0 !important;
}

/* ── Spinner ── */
[data-testid="stSpinner"] { color: #f59e0b !important; }
</style>
""", unsafe_allow_html=True)

# ─── HEADER ───
st.markdown("""
<div class="header-banner">
    <div>
        <p class="header-title">🏏 IPL Predictor</p>
        <p class="header-sub">AI MATCH INTELLIGENCE</p>
    </div>
    <div class="live-badge">LIVE</div>
</div>
""", unsafe_allow_html=True)

# ─── TEAMS ───
teams = [
    'Mumbai Indians', 'Chennai Super Kings', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Delhi Capitals', 'Rajasthan Royals',
    'Sunrisers Hyderabad', 'Punjab Kings', 'Lucknow Super Giants', 'Gujarat Titans'
]

cities = ['Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Delhi', 'Hyderabad', 'Jaipur', 'Pune']

st.markdown('<div class="card-section"><div class="section-label">Teams</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox("🏏 Batting Team", teams)
with col2:
    bowling_team = st.selectbox("🎯 Bowling Team", teams)
st.markdown('</div>', unsafe_allow_html=True)

# ─── MATCH STATS ───
st.markdown('<div class="card-section"><div class="section-label">Match State</div>', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1:
    current_score = st.number_input("Score", min_value=0, value=0)
with c2:
    target = st.number_input("Target", min_value=1, value=150)
with c3:
    balls_left = st.number_input("Balls Left", min_value=1, value=60)
with c4:
    wickets = st.number_input("Wickets", min_value=0, max_value=10, value=0)
st.markdown('</div>', unsafe_allow_html=True)

# ─── CITY + PREDICT ───
st.markdown('<div class="card-section card-section-last"><div class="section-label">Venue</div>', unsafe_allow_html=True)
col_city, col_btn = st.columns([2, 1])
with col_city:
    city = st.selectbox("📍 City", cities)
with col_btn:
    st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)
    predict = st.button("PREDICT")
st.markdown('</div>', unsafe_allow_html=True)

# ─── RESULT ───
if predict:
    if batting_team == bowling_team:
        st.error(f"⚠️ Batting and bowling team cannot both be **{batting_team}** — a team cannot play against itself.")
        st.stop()

    balls_bowled = 120 - balls_left
    max_possible_score = balls_bowled * 6
    if current_score > max_possible_score:
        st.error(f"⚠️ Invalid input — only **{balls_bowled} balls** have been bowled, so the maximum possible score is **{max_possible_score}**. Current score of **{current_score}** is not possible.")
        st.stop()

    if current_score >= target:
        st.error(f"⚠️ Invalid input — the batting team has already reached or passed the target ({current_score} ≥ {target}). The match would already be over.")
        st.stop()

    input_data = {
        "batting_team": batting_team,
        "bowling_team": bowling_team,
        "city": city,
        "current_score": current_score,
        "balls_left": balls_left,
        "wickets": wickets,
        "target": target
    }
    with st.spinner("Crowd cheering... AI thinking..."):
        try:
            response = requests.post("http://127.0.0.1:8000/predict", json=input_data)

            if response.status_code == 200:
                data = response.json()
                prob = data['win_probability']
                factors = data['top_factors']

                st.markdown("---")
                st.markdown('<div class="section-label" style="color:#475569; letter-spacing:2px; font-size:10px;">WIN PROBABILITY</div>', unsafe_allow_html=True)
                st.metric(label="WIN PROBABILITY", value=f"{round(prob * 100, 1)}%")
                st.progress(prob)

                st.markdown('<div class="section-label" style="margin-top:16px; color:#475569; letter-spacing:2px; font-size:10px;">MATCH FACTORS</div>', unsafe_allow_html=True)
                col_a, col_b = st.columns(2)
                # new
                for i, (feature, shap_val, actual_val) in enumerate(factors):
                    label = f"{feature}: {round(float(actual_val), 2)}"
                    if i % 2 == 0:
                        with col_a:
                            if shap_val > 0:
                                st.success(f"▲ {label}")
                            else:
                                st.error(f"▼ {label}")
                    else:
                        with col_b:
                            if shap_val > 0:
                                st.success(f"▲ {label}")
                            else:
                                st.error(f"▼ {label}")
        except requests.exceptions.ConnectionError:
            st.error("🔌 Cannot connect to backend — is FastAPI running on port 8000?")
        except Exception as e:
                    st.error(f"❌ Unexpected error: {e}")

st.markdown("""
<p style='text-align:center; color:#1e2d4a; font-family: IBM Plex Mono, monospace;
   font-size:11px; letter-spacing:2px; margin-top:24px;'>
   ML · SHAP · FastAPI
</p>
""", unsafe_allow_html=True)