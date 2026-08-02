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
    .metric-value-neon {
        font-size: 1.6rem;
        font-weight: 800;
        color: #DEFF9A;
        margin-top: 2px;
    }
    .metric-value {
        font-size: 1.6rem;
        font-weight: 800;
        color: #FFFFFF;
        margin-top: 2px;
    }
    
    /* Styling Khusus Modul Darurat / Emergency */
    .emergency-card {
        background-color: #1E1213;
        border: 1px solid #5A1E22;
        border-radius: 10px;
        padding: 16px;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    
    /* Custom Styling Tombol Streamlit Merah Kaku */
    div.stButton > button:first-child {
        background-color: #D32F2F !important;
        color: #FFFFFF !important;
        font-weight: 800 !important;
        letter-spacing: 1px !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 12px 20px !important;
        width: 100% !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #B71C1C !important;
        box-shadow: 0 0 10px #D32F2F !important;
    }
    
    /* Garis Pemisah */
    hr {
        border-color: #2C2C30;
        margin: 18px 0;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. STATE APLIKASI & SIMULASI DATA
# -----------------------------------------------------------------------------
if 'emergency_triggered' not in st.session_state:
    st.session_state['emergency_triggered'] = False

base_balance = 10000.00

if not st.session_state['emergency_triggered']:
    floating_change = random.uniform(-45.0, 85.0)
    current_equity = base_balance + floating_change
    drawdown_pct = abs((floating_change / base_balance) * 100) if floating_change < 0 else 0.0
else:
    floating_change = 0.0
    current_equity = base_balance
    drawdown_pct = 0.0

# -----------------------------------------------------------------------------
# 3. HEADER & STATUS CLOUD
# -----------------------------------------------------------------------------
st.markdown('<div class="main-header">ZF MASTER <span class="neon-text">CORE APP</span></div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Arsitektur Fondasi Antarmuka Visual & Monitoring Dana Real-time</div>', unsafe_allow_html=True)

# Status Server
status_color = "#DEFF9A" if not st.session_state['emergency_triggered'] else "#FF5252"
status_text = "CONNECTED" if not st.session_state['emergency_triggered'] else "EMERGENCY CUT-OFF"

st.markdown(f"""
    <div class="status-card">
        <div>
            <span style="font-weight: 700; font-size: 0.85rem; color: #FFF;">SERVER EA CLOUD</span><br>
            <span style="font-size: 0.72rem; color: #8E8E93;">Metatrader 5 • Terminal #01</span>
        </div>
        <div>
            <span class="status-dot" style="background-color: {status_color}; box-shadow: 0 0 8px {status_color};"></span>
            <span style="font-size: 0.8rem; font-weight: 700; color: {status_color}; margin-left: 5px;">{status_text}</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. MONITORING DANA LIVE
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
# 5. MODUL KONTROL DARURAT (PANIC CUT-OFF)
# -----------------------------------------------------------------------------
st.markdown('<h4 style="font-weight: 700; color: #FF5252; margin-bottom: 12px;">🚨 Modul Kontrol Darurat</h4>', unsafe_allow_html=True)

st.markdown("""
    <div class="emergency-card">
        <div style="font-weight: 700; color: #FF5252; font-size: 0.95rem; margin-bottom: 4px;">PROTEKSI MUTLAK DANA KELOMPOK</div>
        <div style="color: #A1A1A6; font-size: 0.78rem; line-height: 1.35;">
            Gunakan tombol di bawah untuk menutup seluruh posisi trading aktif secara instan dan mematikan perintah EA di server cloud.
        </div>
    </div>
""", unsafe_allow_html=True)

pin_input = st.text_input("Masukkan PIN Otorisasi (Default PIN: 8888)", type="password", key="pin_code")

if st.button("🚨 CLOSE ALL POSITIONS (PANIC CUT-OFF)"):
    if pin_input == "8888":
        st.session_state['emergency_triggered'] = True
        st.error("⚠️ PERINTAH DARURAT DIEKSEKUSI! Seluruh posisi trading telah ditutup mutlak.")
    else:
        st.warning("❌ PIN Otorisasi Salah! Akses ditolak.")

if st.session_state['emergency_triggered']:
    if st.button("🔄 RESET SISTEM MONITORING (NORMAL)"):
        st.session_state['emergency_triggered'] = False
        st.rerun()

# Auto-refresh interval (jika kondisi normal)
if not st.session_state['emergency_triggered']:
    time.sleep(3)
    st.rerun()
