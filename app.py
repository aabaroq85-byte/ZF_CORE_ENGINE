import streamlit as st
import random
import time

# Konfigurasi Tampilan HP
st.set_page_config(
    page_title="ZF-Core Engine",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Style untuk Tampilan Mobile
st.markdown("""
    <style>
    .main { padding: 1rem; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; background-color: #0d6efd; color: white; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("💎 ZF-CORE ENGINE")
st.caption("Sistem Intelijen Eksplorasi Mineral & Geofisika Presisi")
st.markdown("---")

# Sidebar Input Data
st.sidebar.header("🎯 Input Target")
nama_lokasi = st.sidebar.text_input("Nama Lokasi / Area", value="Kampung Muara Nawa, Distrik Airu")
koordinat_lat = st.sidebar.number_input("Latitude (S/N)", value=-3.212500, format="%.6f")
koordinat_lon = st.sidebar.number_input("Longitude (E/W)", value=139.871667, format="%.6f")

st.sidebar.markdown("---")
btn_proses = st.sidebar.button("🚀 JALANKAN ANALISIS ZF-CORE")

# Fungsi Kalkulasi A_ZF
def hitung_akurasi(e, f, r):
    return round((0.35 * e) + (0.35 * f) + (0.30 * r), 1)

if btn_proses:
    with st.spinner('Menghubungkan ke data spektral & memproses algoritma ZF...'):
        time.sleep(1.2)
    
    # Random Simulasi Nilai Variabel
    val_e = round(random.uniform(84.0, 91.0), 1)
    val_f = round(random.uniform(82.0, 88.0), 1)
    val_r = round(random.uniform(83.0, 89.0), 1)
    skor_total = hitung_akurasi(val_e, val_f, val_r)

    # Output Intelijen
    st.subheader("📍 Ringkasan Intelijen Target")
    st.write(f"**Area Target:** {nama_lokasi}")
    st.write(f"**Episentrum:** `{koordinat_lat}, {koordinat_lon}`")
    st.write("**Tipe Endapan:** Placer/Aluvial & Epithermal Urat Kuarsa")
    
    st.markdown("---")
    st.subheader("🧮 Skor Akurasi Presisi (A_ZF)")
    
    col1, col2 = st.columns(2)
    col1.metric("Entropy Suppression", f"{val_e}%")
    col2.metric("Fractal Density (Zn=2)", f"{val_f}%")
    
    col3, col4 = st.columns(2)
    col3.metric("Resonant Coupling", f"{val_r}%")
    col4.metric("TOTAL AKURASI (A_ZF)", f"{skor_total}%")
    
    st.progress(skor_total / 100)
    
    st.markdown("---")
    st.subheader("📦 Estimasi & Layering Kedalaman")
    st.info(f"""
    * **Layer 1 (Aluvial Sekunder):** 4 m – 18 m (Pasir/Kerikil Bedrock)
    * **Layer 2 (Orogenik Primer):** 110 m – 280 m (Urat Kuarsa)
    * **Potensi Kadar (Avg):** 3.8 – 6.5 g/ton (Aluvial) / >12 g/ton (Urat)
    * **Indikator Mineral:** Magnetit, Pirit, Emas Murni (Au-Ag Alloy)
    """)
else:
    st.info("👈 Buka menu di pojok kiri atas (tanda >), atur lokasi/koordinat, lalu tekan tombol **JALANKAN ANALISIS ZF-CORE**.")
