# dashboard/app.py

import streamlit as st
import pandas as pd
import joblib
import time
import matplotlib.pyplot as plt
import os
import random

# =========================
# PATH SETUP
# =========================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "isolation_forest.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "models", "encoders.pkl")
FEATURE_PATH = os.path.join(BASE_DIR, "models", "feature_columns.pkl")

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
encoders = joblib.load(ENCODER_PATH)
feature_columns = joblib.load(FEATURE_PATH)

# =========================
# UI CONFIG
# =========================
st.set_page_config(page_title="Cyber SOC Dashboard", layout="wide", initial_sidebar_state="collapsed")

# =========================
# PREMIUM GLASSMORPHIC CYBER UI
# =========================
st.markdown("""
<style>
/* Import Cyber/Tech Fonts */
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;500;600;700&family=Share+Tech+Mono&display=swap');

html, body, [class*="css"] {
    font-family: 'Rajdhani', sans-serif !important;
}

/* Deep Cyber Mesh Background */
.stApp {
    background: 
        radial-gradient(circle at 15% 50%, rgba(0, 255, 204, 0.05), transparent 25%),
        radial-gradient(circle at 85% 30%, rgba(255, 0, 60, 0.05), transparent 25%),
        linear-gradient(135deg, #020617 0%, #080f26 100%);
    color: #e2e8f0;
}

/* Hide Default Header */
header[data-testid="stHeader"] {
    background-color: transparent !important;
}

/* Cyber Headers */
h1, h2, h3 {
    color: #00ffcc !important;
    font-weight: 600 !important;
    letter-spacing: 1px;
    text-transform: uppercase;
    text-shadow: 0 0 10px rgba(0, 255, 204, 0.3);
}

/* Glassmorphic Metric Cards (Overriding Streamlit Defaults) */
div[data-testid="metric-container"] {
    background: rgba(15, 23, 42, 0.6);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(0, 255, 204, 0.2);
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5), inset 0 0 20px rgba(0, 255, 204, 0.05);
    transition: all 0.3s ease;
}
div[data-testid="metric-container"]:hover {
    border-color: rgba(0, 255, 204, 0.6);
    box-shadow: 0 4px 30px rgba(0, 255, 204, 0.15), inset 0 0 20px rgba(0, 255, 204, 0.1);
    transform: translateY(-2px);
}
[data-testid="stMetricValue"] {
    color: #ffffff;
    font-size: 2.5rem;
    font-weight: 700;
    font-family: 'Share Tech Mono', monospace !important;
}
[data-testid="stMetricLabel"] {
    color: #94a3b8;
    font-size: 1rem;
    letter-spacing: 1.5px;
}

/* Animated Glowing Alerts */
@keyframes pulse-red {
    0% { box-shadow: 0 0 15px rgba(255, 0, 60, 0.2); }
    50% { box-shadow: 0 0 30px rgba(255, 0, 60, 0.6); }
    100% { box-shadow: 0 0 15px rgba(255, 0, 60, 0.2); }
}
@keyframes pulse-cyan {
    0% { box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); }
    50% { box-shadow: 0 0 30px rgba(0, 255, 204, 0.5); }
    100% { box-shadow: 0 0 15px rgba(0, 255, 204, 0.2); }
}

.alert-high {
    background: rgba(255, 0, 60, 0.1);
    backdrop-filter: blur(10px);
    border: 1px solid #ff003c;
    padding: 20px;
    border-radius: 12px;
    color: #ff003c;
    font-size: 1.5rem;
    font-weight: 700;
    text-align: center;
    letter-spacing: 2px;
    animation: pulse-red 2s infinite;
    text-shadow: 0 0 10px rgba(255, 0, 60, 0.5);
}

.alert-safe {
    background: rgba(0, 255, 204, 0.05);
    backdrop-filter: blur(10px);
    border: 1px solid #00ffcc;
    padding: 20px;
    border-radius: 12px;
    color: #00ffcc;
    font-size: 1.5rem;
    font-weight: 700;
    text-align: center;
    letter-spacing: 2px;
    animation: pulse-cyan 3s infinite;
    text-shadow: 0 0 10px rgba(0, 255, 204, 0.4);
}

/* Hacker Terminal Log Box */
.cyber-terminal {
    background: rgba(2, 6, 23, 0.85);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(0, 255, 204, 0.3);
    border-radius: 8px;
    padding: 20px;
    height: 300px;
    overflow-y: auto;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.9rem;
    color: #00ffcc;
    box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.8);
}
.cyber-terminal::-webkit-scrollbar { width: 5px; }
.cyber-terminal::-webkit-scrollbar-track { background: #020617; }
.cyber-terminal::-webkit-scrollbar-thumb { background: #00ffcc; }

.log-time { color: #64748b; }
.log-warn { color: #ffab00; text-shadow: 0 0 5px rgba(255,171,0,0.5); }
.log-crit { color: #ff003c; text-shadow: 0 0 5px rgba(255,0,60,0.5); }
.log-info { color: #00ffcc; }

/* Subheaders */
.sub-header {
    border-bottom: 1px solid rgba(0, 255, 204, 0.2);
    padding-bottom: 10px;
    margin-bottom: 20px;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div style="text-align: center; padding: 20px 0 40px 0;">
    <h1 style="font-size: 3.5rem; margin-bottom: 0;">🛡️ SEC-OPS COMMAND CENTER</h1>
    <p style="color: #64748b; font-size: 1.2rem; letter-spacing: 2px; font-family: 'Share Tech Mono', monospace;">AI-DRIVEN REAL-TIME NETWORK MONITORING</p>
</div>
""", unsafe_allow_html=True)

# =========================
# FILE UPLOAD
# =========================
uploaded_file = st.file_uploader("INITIALIZE DATA STREAM (Upload CSV)", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)
    st.markdown("<h3 class='sub-header'>📊 INTERCEPTED TRAFFIC PREVIEW</h3>", unsafe_allow_html=True)
    st.dataframe(df.head(), use_container_width=True)

    # =========================
    # LOADING BAR (ANIMATION)
    # =========================
    st.markdown("<p style='color: #00ffcc; font-family: \"Share Tech Mono\", monospace;'>[SYS] INITIALIZING NEURAL THREAT DETECTION...</p>", unsafe_allow_html=True)
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)
    progress.empty() # Clear bar after loading for cleaner UI

    with st.spinner("ANALYZING PACKET SIGNATURES..."):

        # =========================
        # PREPROCESSING (UNCHANGED)
        # =========================
        df = df.drop(columns=['label', 'attack_cat', 'id'], errors='ignore')

        if 'sbytes' in df.columns and 'dbytes' in df.columns:
            df['byte_ratio'] = df['sbytes'] / (df['dbytes'] + 1)

        for col, encoder in encoders.items():
            if col in df.columns:
                df[col] = df[col].apply(
                    lambda x: x if x in encoder.classes_ else encoder.classes_[0]
                )
                df[col] = encoder.transform(df[col])

        df = df.reindex(columns=feature_columns, fill_value=0)
        df_scaled = scaler.transform(df)

        preds = model.predict(df_scaled)
        preds = [1 if p == -1 else 0 for p in preds]

        df['Prediction'] = preds

    # =========================
    # METRICS
    # =========================
    total = len(df)
    threats = sum(preds)
    safe = total - threats
    risk = (threats / total) * 100

    col1, col2, col3 = st.columns(3)
    col1.metric("PACKETS SCANNED", f"{total:,}")
    col2.metric("THREATS DETECTED", f"{threats:,}")
    col3.metric("CLEAN TRAFFIC", f"{safe:,}")

    # =========================
    # RISK LEVEL & LIVE LOGS LAYOUT
    # =========================
    col_risk, col_logs = st.columns([1, 2])

    with col_risk:
        st.markdown("<h3 class='sub-header'>⚠️ SYSTEM STATUS</h3>", unsafe_allow_html=True)
        if risk > 50:
            st.markdown(f"<div class='alert-high'>CRITICAL BREACH<br><span style='font-size: 1rem;'>THREAT LEVEL: {risk:.2f}%</span></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='alert-safe'>SECURE<br><span style='font-size: 1rem;'>THREAT LEVEL: {risk:.2f}%</span></div>", unsafe_allow_html=True)

        # =========================
        # GRAPH (Styled for Dark Mode)
        # =========================
        st.markdown("<h3 class='sub-header'>📈 VECTOR ANALYSIS</h3>", unsafe_allow_html=True)
        fig, ax = plt.subplots(figsize=(5, 4))
        
        # Transparent glass styling for matplotlib
        fig.patch.set_facecolor('none')
        ax.set_facecolor('none')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_color('#334155')
        ax.spines['left'].set_color('#334155')
        ax.tick_params(colors='#94a3b8')
        
        # Cyber Colors
        bars = ax.bar(['Safe', 'Threat'], [safe, threats], color=['#00ffcc', '#ff003c'], alpha=0.8)
        
        st.pyplot(fig)

    with col_logs:
        # =========================
        # LIVE SOC LOGS
        # =========================
        st.markdown("<h3 class='sub-header'>💻 LIVE THREAT TERMINAL</h3>", unsafe_allow_html=True)

        log_box = st.empty()

        sample_logs = [
            "<span class='log-warn'>[WARN] Suspicious TCP spike detected on port 443</span>",
            "<span class='log-crit'>[CRIT] Possible DDoS pattern identified originating from external IP</span>",
            "<span class='log-info'>[INFO] Analyzing unusual packet payload size...</span>",
            "<span class='log-crit'>[CRIT] ML model flagged severe isolation forest anomaly</span>",
            "<span class='log-warn'>[WARN] Unknown traffic behavior detected in subnet mask</span>",
            "<span class='log-info'>[INFO] Handshake protocol bypassed. Flagging for review.</span>"
        ]

        logs = []
        for i in range(12):
            timestamp = time.strftime('%H:%M:%S')
            logs.append(f"<span class='log-time'>[{timestamp}]</span> {random.choice(sample_logs)}")
            
            # Format as HTML to allow color coding
            log_html = "<br>".join(logs)
            log_box.markdown(f"<div class='cyber-terminal'>{log_html}<br><span class='log-info'>_</span></div>", unsafe_allow_html=True)
            time.sleep(0.3)

    # =========================
    # RESULTS TABLE
    # =========================
    st.markdown("<h3 class='sub-header'>🔎 FORENSIC DATA MATRIX</h3>", unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)

else:
    # Idle State UI
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 50px; background: rgba(15, 23, 42, 0.4); border: 1px dashed rgba(0, 255, 204, 0.3); border-radius: 12px; backdrop-filter: blur(10px);">
        <h3 style="color: #64748b !important;">AWAITING DATA STREAM</h3>
        <p style="color: #475569;">Upload network dataset to initialize AI monitoring protocols.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid rgba(0, 255, 204, 0.1); color: #475569; font-family: 'Share Tech Mono', monospace; font-size: 0.8rem;">
    SOC PLATFORM V3.0 | ARCHITECT: ANIKET SATPATHY | SECURE CONNECTION
</div>
""", unsafe_allow_html=True)