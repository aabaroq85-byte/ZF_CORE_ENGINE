import streamlit as st
import pandas as pd
import time
import random

# -----------------------------------------------------------------------------
# 1. KONFIGURASI HALAMAN & TEMA DARK KAKU
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="ZF MASTER CORE APP",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS Optimasi Layar HP & Laptop
st.markdown("""
    <style>
    .block-container {
        padding-top: 3.5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 0.8rem !important;
        padding-right: 0.8rem !important;
    }
    .stApp {
        background-color: #0E0E10;
        color: #E0E0E0;
        font-family: 'Inter', sans-serif;
    }
    .main-header {
        font-size: 1.7rem;
        font-weight: 800;
        letter-spacing: 1px;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 4px;
        line-height: 1.2;
    }
    .neon-text {
        color: #DEFF9A;
    }
    .sub-header {
        font-size: 0.78rem;
        color: #8E8E93;
        text-align: center;
        margin-bottom: 18px;
    }
    
    /* Box Indikator Status Server */
    .status-card {
        background-color: #1A1A1E;
        border: 1px solid #2C2C30;
        border-radius: 10px;
        padding: 12px 16px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 15px;
    }
    .status-dot {
        height: 10px;
        width: 10px;
        background-color: #DEFF9A;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 8px #DEFF9A;
    }
    
    /* Modul Kartu & Metric Kaku */
    .kaku-card {
        background-color: #1A1A1E;
        border: 1px solid #2C2C30;
        border-radius: 10px;
        padding: 14px;
        margin-bottom: 10px;
    }
    .metric-label {
        font-size: 0.75rem;
        color: #8E8E93;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }
    .metric-value {
        font-size: 1.6rem;
        font-weight: 800;
        color: #FFFFFF;
        margin-top: 2px;
    }
    .metric-value-neon {
        font-size: 1.6rem;
        font-weight: 800;
        color: #DEFF9A;
        margin-top: 2px;
    }
    
    /* Garis Pemisah */
    hr {
        border-color: #2C2C30;
        margin: 18px 0;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. SIMULASI DATA REAL-TIME (STUB UNTUK METATRADER / API)
# -----------------------------------------------------------------------------
# Menggenerasi angka dinamis untuk mensimulasikan koneksi aktif
base_balance = 10000.00
floating_change = random.uniform(-45.0, 85.0)
current_equity = base_balance + floating_change
drawdown_pct = abs((floating_change / base_balance) * 100) if floating_change < 0 else 0.0

# -----------------------------------------------------------------------------
# 3. HEADER & STATUS CLOUD REAL-TIME
# -----------------------------------------------------------------------------
st.markdown('<div class="main-header">ZF MASTER <span class="neon-text">CORE APP</span></div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Arsitektur Fondasi Antarmuka Visual & Monitoring Dana Real-time</div>', unsafe_allow_html=True)

# Widget Indikator Status Server
st.markdown(f"""
    <div class="status-card">
        <div>
            <span style="font-weight: 700; font-size: 0.85rem; color: #FFF;">SERVER EA CLOUD</span><br>
            <span style="font-size: 0.72rem; color: #8E8E93;">Metatrader 5 • Terminal #01</span>
        </div>
        <div>
            <span class="status-dot"></span>
            <span style="font-size: 0.8rem; font-weight: 700; color: #DEFF9A; margin-left: 5px;">CONNECTED</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. METRIC DASBOR MONITORING REAL-TIME
# -----------------------------------------------------------------------------
st.markdown('<h4 style="font-weight: 700; margin-bottom: 12px;">Monitoring <span class="neon-text">Ekuitas Live</span></h4>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
        <div class="kaku-card">
            <div class="metric-label">Total Ekuitas</div>
            <div class="metric-value-neon">${current_equity:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="kaku-card">
            <div class="metric-label">Floating P/L</div>
            <div class="metric-value" style="color: {'#DEFF9A' if floating_change >= 0 else '#FF5252'};">
                {'+' if floating_change >= 0 else ''}${floating_change:,.2f}
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="kaku-card">
            <div class="metric-label">Balance Awal</div>
            <div class="metric-value">${base_balance:,.2f}</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="kaku-card">
            <div class="metric-label">Drawdown Saat Ini</div>
            <div class="metric-value" style="color: {'#DEFF9A' if drawdown_pct < 1.0 else '#FF5252'};">
                {drawdown_pct:.2f}% <span style="font-size: 0.75rem; color: #8E8E93;">/ Max 1.5%</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 5. DOKUMENTASI PRINSIP DESAIN & SPESIFIKASI
# -----------------------------------------------------------------------------
st.markdown('<h4 style="text-align: center; font-weight: 700; margin-bottom: 12px;">Prinsip Desain <span class="neon-text">Kaku</span></h4>', unsafe_allow_html=True)

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
        <div class="kaku-card">
            <div class="card-title" style="color: #FFF; font-size: 0.9rem; font-weight: 700;">Minimalis & Terarah</div>
            <div class="card-desc" style="color: #A1A1A6; font-size: 0.78rem;">Fokus utama pada pergerakan Ekuitas dan proteksi risiko tanpa distraksi indikator teknis berlebih.</div>
        </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
        <div class="kaku-card">
            <div class="card-title" style="color: #FFF; font-size: 0.9rem; font-weight: 700;">Batas Risiko Kaku</div>
            <div class="card-desc" style="color: #A1A1A6; font-size: 0.78rem;">Sistem otomatis memproteksi modal jika persentase drawdown mendekati ambang batas 1.5%.</div>
        </div>
    """, unsafe_allow_html=True)

# Refresh otomatis setiap 3 detik untuk mensimulasikan data live
time.sleep(3)
st.rerun()
