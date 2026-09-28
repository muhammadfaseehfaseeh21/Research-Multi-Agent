import os
import streamlit as st

from crew import build_crew


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Research Multi-Agent Team",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# LIGHT / WHITE PRESENTATION LAYER
# =========================================================
# IMPORTANT:
# - Use st.html() for custom HTML/CSS.
# - Do NOT use st.markdown() for HTML UI components.
# This prevents HTML tags from appearing as plain text.


st.html(
    """
    <style>
        /* ---------- APP ---------- */
        .stApp {
            background: #f7f9fc;
        }

        .main .block-container {
            max-width: 1450px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        /* ---------- SIDEBAR ---------- */
        [data-testid="stSidebar"] {
            background: #ffffff;
            border-right: 1px solid #e7ebf2;
        }

        [data-testid="stSidebar"] * {
            color: #172033;
        }

        /* ---------- HERO ---------- */
        .hero {
            padding: 2.6rem 3rem;
            margin-bottom: 2rem;
            background: linear-gradient(
                135deg,
                #ffffff 0%,
                #f3f7ff 55%,
                #f7f1ff 100%
            );
            border: 1px solid #e1e8f5;
            border-radius: 28px;
            box-shadow: 0 12px 35px rgba(30, 55, 90, 0.08);
            text-align: center;
        }

        .hero-title {
            font-size: clamp(2rem, 4vw, 3rem);
            font-weight: 800;
            letter-spacing: -0.04em;
            color: #2563eb;
            margin-bottom: 0.8rem;
        }

        .hero-subtitle {
            max-width: 850px;
            margin: 0 auto;
            color: #64748b;
            font-size: 1.05rem;
            line-height: 1.7;
        }

        /* ---------- HEADINGS ---------- */
        .section-title {
            font-size: 1.55rem;
            font-weight: 800;
            color: #172033;
            margin-bottom: 1rem;
        }

        /* ---------- CARDS ---------- */
        .settings-card,
        .agent-card,
        .status-card,
        .report-card {
