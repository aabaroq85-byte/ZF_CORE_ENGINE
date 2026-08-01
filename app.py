import streamlit as st
import pandas as pd
import time
import math

# -----------------------------------------------------------------------------
# 1. KONFIGURASI HALAMAN & TEMA DARK KAKU
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="ZF MASTER CORE APP",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk Meniru Gaya Visual Dokumen (Dark Mode + Hijau Neon #DEFF9A)
st.markdown("""
    <style>
    /* Background Utama & Font */
    .stApp {
        background-color: #0E0E10;
        color: #E0E0E0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Judul Utama dengan Akson Neon Green */
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: 1.5px;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 5px;
    }
    .neon-text {
        color: #DEFF9A;
    }
    .sub-header {
        font-size: 0.9rem;
        color: #8E8E93;
        text-align: center;
        margin-bottom: 25px;
    }
    
    /* Kartu / Box Fitur Kaku (Prinsip Desain Kaku) */
    .kaku-card {
        background-color: #1A1A1E;
        border: 1px solid #2C2C30;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
        transition: border 0.3s ease;
    }
    .kaku-card:hover {
        border: 1px solid #DEFF9A;
    }
    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 8px;
    }
    .card-desc {
        font-size: 0.85rem;
        color: #A1A1A6;
        line-height: 1.4;
    }
    
    /* Stat / Highlight Angka Besar */
    .big-number-box {
        background: linear-gradient(135deg, #1A1A1E 0%, #121214 100%);
        border: 1px solid #DEFF9A;
        border-radius: 16px;
        padding: 30px;
        text-align: center;
        margin: 20px 0;
    }
    .big-number {
        font-size: 3.5rem;
        font-weight: 900;
        color: #DEFF9A;
        line-height: 1;
    }
    .big-number-sub {
        font-size: 0.9rem;
        color: #8E8E93;
        margin-top: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Garis Pemisah (Divider) */
    hr {
        border-color: #2C2C30;
        margin: 30px 0;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. HEADER UTAMA (ZF MASTER CORE APP)
# -----------------------------------------------------------------------------
st.markdown('<div class="main-header">ZF MASTER <span class="neon-text">CORE APP</span></div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Arsitektur Fondasi Antarmuka Visual: Integrasi Monitoring Kaku & Kontrol Darurat Real-time untuk Dana Kelompok.</div>', unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 3. SEKSI VISI & ARSITEKTUR (PRINSIP DESAIN KAKU)
# -----------------------------------------------------------------------------
st.markdown('<h3 style="text-align: center; font-weight: 700;">Prinsip Desain <span class="neon-text">Kaku</span></h3>', unsafe_allow_html=True)
st.write("")

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
# 4. SEKSI BATAS RISIKO KAKU & PILAR NAVIGASI
# -----------------------------------------------------------------------------
col_left, col_right = st.columns([1, 1.2])

with col_left:
    st.markdown('<h3 style="font-weight: 700;">Batas <span class="neon-text">Risiko Kaku</span></h3>', unsafe_allow_html=True)
    st.markdown("""
        <div class="big-number-box">
            <div class="big-number">1.5%</div>
            <div class="big-number-sub">Per Sesi Trading (Proteksi Mutlak)</div>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown('<h3 style="font-weight: 700;">Efisiensi <span class="neon-text">Monitoring</span></h3>', unsafe_allow_html=True)
    st.markdown("""
        <div class="kaku-card">
            <div class="card-title">⏱️ Respon App (Otomatis): <span class="neon-text">0.5 Detik</span></div>
            <div class="card-desc">Menghilangkan faktor 'keraguan manusia' saat harus menutup posisi dalam kondisi pasar ekstrem.</div>
        </div>
        <div class="kaku-card">
            <div class="card-title">🛡️ Keamanan Prioritas Utama</div>
            <div class="card-desc">Bukan sekadar aplikasi trading, melainkan instrumen perlindungan modal kelompok yang menjaga setiap sen dari risiko yang tidak terukur.</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 5. SPESIFIKASI TEKNIS UI (TABEL STYLED)
# -----------------------------------------------------------------------------
st.markdown('<h3 style="font-weight: 700;">Spesifikasi <span class="neon-text">Teknis UI</span></h3>', unsafe_allow_html=True)

data_spec = {
    "Komponen": ["Library UI", "Font Style", "Aksen Warna", "Update Rate"],
    "Teknologi / Nilai": ["Streamlit / Custom CSS", "Urbanist / Inter (Sans-Serif)", "#DEFF9A (Neon Green)", "1000ms (1 Detik)"],
    "Fungsi Utama": [
        "Antarmuka modern & responsif di HP",
        "Keterbacaan angka finansial tinggi",
        "Identitas 'Status Aktif & Profit'",
        "Sinkronisasi presisi data bursa"
    ]
}

df_spec = pd.DataFrame(data_spec)
st.dataframe(df_spec, use_container_width=True, hide_index=True)

# Footer Presentasi
st.markdown("<br><p style='text-align: center; color: #8E8E93; font-size: 0.8rem;'>ZF Master Core App • Keamanan Prioritas Utama</p>", unsafe_allow_html=True)
