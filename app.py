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
# LIGHT THEME
# =========================================================

st.html(
    """
    <style>
    .stApp {
        background: #f7f9fc;
    }

    .main .block-container {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    [data-testid="stSidebar"] {
        background: #ffffff;
        border-right: 1px solid #e5eaf2;
    }

    .hero {
        background: linear-gradient(135deg, #ffffff, #f2f6ff, #f8f3ff);
        border: 1px solid #dfe7f5;
        border-radius: 26px;
        padding: 2.5rem 2rem;
        text-align: center;
        box-shadow: 0 12px 35px rgba(30, 55, 90, 0.08);
        margin-bottom: 2rem;
    }

    .hero-title {
        font-size: clamp(2rem, 4vw, 3rem);
        font-weight: 800;
        color: #2563eb;
        margin-bottom: 0.7rem;
    }

    .hero-subtitle {
        max-width: 850px;
        margin: auto;
        color: #64748b;
        font-size: 1rem;
        line-height: 1.7;
    }

    .card {
        background: #ffffff;
        border: 1px solid #e3e8f0;
        border-radius: 20px;
        padding: 1.4rem;
        box-shadow: 0 8px 25px rgba(30, 55, 90, 0.06);
    }

    .agent-card {
        min-height: 190px;
    }

    .agent-number {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background: #eff6ff;
        color: #2563eb;
        font-weight: 800;
    }

    .agent-icon {
        font-size: 2rem;
        margin-top: 0.6rem;
    }

    .agent-name {
        color: #172033;
