import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# 1. KONFIGURASI HALAMAN & TEMA DARK KAKU (OPTIMAL UNTUK HP)
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
    /* Jarak atas disesuaikan agar header tidak terpotong tombol navigasi HP */
    .block-container {
        padding-top: 3.5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 0.8rem !important;
        padding-right: 0.8rem !important;
    }
    
    /* Latar Belakang Utama Gelap */
    .stApp {
        background-color: #0E0E10;
        color: #E0E0E0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Judul Utama */
    .main-header {
        font-size: 1.7rem;
        font-weight: 800;
        letter-spacing: 1px;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 6px;
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
        line-height: 1.35;
    }
    
    /* Modul Kartu Kaku */
    .kaku-card {
        background-color: #1A1A1E;
        border: 1px solid #2C2C30;
        border-radius: 10px;
        padding: 14px;
        margin-bottom: 10px;
    }
    .card-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 4px;
    }
    .card-desc {
        font-size: 0.78rem;
        color: #A1A1A6;
        line-height: 1.35;
    }
    
    /* Kotak Angka Besar (Highlight) */
    .big-number-box {
        background: linear-gradient(135deg, #1A1A1E 0%, #121214 100%);
        border: 1px solid #DEFF9A;
        border-radius: 12px;
        padding: 20px 10px;
        text-align: center;
        margin: 10px 0;
    }
    .big-number {
        font-size: 2.8rem;
        font-weight: 900;
        color: #DEFF9A;
        line-height: 1;
    }
    .big-number-sub {
        font-size: 0.75rem;
        color: #8E8E93;
        margin-top: 6px;
        text-transform: uppercase;
        letter-spacing: 0.8px;
    }
    
    /* Garis Pemisah Tipis */
    hr {
        border-color: #2C2C30;
        margin: 18px 0;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. HEADER UTAMA
# -----------------------------------------------------------------------------
st.markdown('<div class="main-header">ZF MASTER <span class="neon-text">CORE APP</span></div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Arsitektur Fondasi Antarmuka Visual: Integrasi Monitoring Kaku & Kontrol Darurat Real-time untuk Dana Kelompok.</div>', unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 3. SEKSI PRINSIP DESAIN KAKU
# -----------------------------------------------------------------------------
st.markdown('<h4 style="text-align: center; font-weight: 700; margin-bottom: 12px;">Prinsip Desain <span class="neon-text">Kaku</span></h4>', unsafe_allow_html=True)

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
        <div class="kaku-card">
            <div class="card-title">Minimalis & Terarah</div>
            <div class="card-desc">Menghilangkan distraksi grafik rumit. Fokus hanya pada angka Ekuitas dan status keamanan robot di server cloud.</div>
        </div>
        <div class="kaku-card">
            <div class="card-title">Aksesibilitas Awam</div>
            <div class="card-desc">Penggunaan bahasa yang tidak teknis. Mengubah istilah "Margin Call" menjadi "Batas Risiko" agar mudah dipahami anggota.</div>
        </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
        <div class="kaku-card">
            <div class="card-title">Hierarki Kontrol</div>
            <div class="card-desc">Informasi kritis (Minus %) diletakkan di tengah dengan kontras tertinggi agar saudara Aa langsung waspada jika terjadi drawdown.</div>
        </div>
        <div class="kaku-card">
            <div class="card-title">Keamanan Visual</div>
            <div class="card-desc">Mode gelap (Dark Mode) untuk mengurangi kelelahan mata saat pemantauan 24 jam dan meningkatkan visibilitas aksen neon.</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 4. SEKSI BATAS RISIKO & EFISIENSI
# -----------------------------------------------------------------------------
col_left, col_right = st.columns([1, 1.2])

with col_left:
    st.markdown('<h4 style="font-weight: 700; margin-bottom: 10px;">Batas <span class="neon-text">Risiko Kaku</span></h4>', unsafe_allow_html=True)
    st.markdown("""
        <div class="big-number-box">
            <div class="big-number">1.5%</div>
            <div class="big-number-sub">Per Sesi Trading (Proteksi Mutlak)</div>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown('<h4 style="font-weight: 700; margin-bottom: 10px;">Efisiensi <span class="neon-text">Monitoring</span></h4>', unsafe_allow_html=True)
    st.markdown("""
        <div class="kaku-card">
            <div class="card-title">⏱️ Respon App: <span class="neon-text">0.5 Detik</span></div>
            <div class="card-desc">Menghilangkan faktor 'keraguan manusia' saat harus menutup posisi dalam kondisi pasar ekstrem.</div>
        </div>
        <div class="kaku-card">
            <div class="card-title">🛡️ Keamanan Utama</div>
            <div class="card-desc">Instrumen perlindungan modal kelompok yang menjaga setiap sen dari risiko tidak terukur.</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 5. SPESIFIKASI TEKNIS UI
# -----------------------------------------------------------------------------
st.markdown('<h4 style="font-weight: 700; margin-bottom: 10px;">Spesifikasi <span class="neon-text">Teknis UI</span></h4>', unsafe_allow_html=True)

data_spec = {
    "Komponen": ["Library UI", "Font Style", "Aksen Warna", "Update Rate"],
    "Teknologi / Nilai": ["Streamlit / Custom CSS", "Urbanist / Inter", "#DEFF9A (Neon Green)", "1000ms (1 Detik)"],
    "Fungsi Utama": [
        "Antarmuka modern & responsif di HP",
        "Keterbacaan angka finansial tinggi",
        "Identitas 'Status Aktif & Profit'",
        "Sinkronisasi presisi data bursa"
    ]
}

df_spec = pd.DataFrame(data_spec)
st.dataframe(df_spec, use_container_width=True, hide_index=True)

st.markdown("<br><p style='text-align: center; color: #8E8E93; font-size: 0.75rem;'>ZF Master Core App • Keamanan Prioritas Utama</p>", unsafe_allow_html=True)
