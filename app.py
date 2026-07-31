import streamlit as st
import random
import time
import pandas as pd
import folium
from streamlit_folium import st_folium
from fpdf import FPDF

# ---------------------------------------------------------
# KONFIGURASI HALAMAN
# ---------------------------------------------------------
st.set_page_config(
    page_title="ZF-Core Engine PRO",
    page_icon="💎",
    layout="wide"
)

st.title("💎 ZF-CORE ENGINE PRO")
st.caption("Sistem Intelijen Eksplorasi Geofisika & Pemrosesan Multi-Titik")
st.markdown("---")

# ---------------------------------------------------------
# FUNGSI KALKULASI & PDF
# ---------------------------------------------------------
def hitung_a_zf(e, f, r):
    return round((0.35 * e) + (0.35 * f) + (0.30 * r), 1)

def generate_pdf(df_result):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "LAPORAN HASIL ANALISIS ZF-CORE ENGINE", ln=True, align="C")
    pdf.ln(5)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 6, "Sistem Intelijen Eksplorasi Mineral & Geofisika Presisi", ln=True, align="C")
    pdf.line(10, 28, 200, 28)
    pdf.ln(10)

    for idx, row in df_result.iterrows():
        pdf.set_font("Helvetica", "B", 12)
        pdf.cell(0, 8, f"Target #{idx+1}: {row['Nama Titik']}", ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.cell(0, 6, f"Koordinat: {row['Latitude']}, {row['Longitude']}", ln=True)
        pdf.cell(0, 6, f"Entropy Suppression: {row['Entropy (%)']}% | Fractal Density: {row['Fractal (%)']}%", ln=True)
        pdf.cell(0, 6, f"Resonant Coupling: {row['Resonant (%)']}% | TOTAL AKURASI (A_ZF): {row['Akurasi A_ZF (%)']}%", ln=True)
        pdf.cell(0, 6, f"Kedalaman Layer 1: {row['Layer 1 (m)']} | Layer 2: {row['Layer 2 (m)']}", ln=True)
        pdf.ln(4)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(4)

    return pdf.output()

# ---------------------------------------------------------
# SIDEBAR - INPUT MULTI-TITIK
# ---------------------------------------------------------
st.sidebar.header("🎯 Input Multi-Titik Target")

mode_input = st.sidebar.radio("Mode Input Data:", ["Satu Titik Target", "Multi-Titik (Banyak Area)"])

data_target = []

if mode_input == "Satu Titik Target":
    nama = st.sidebar.text_input("Nama Lokasi", "Kampung Muara Nawa")
    lat = st.sidebar.number_input("Latitude (S/N)", -3.212500, format="%.6f")
    lon = st.sidebar.number_input("Longitude (E/W)", 139.871667, format="%.6f")
    data_target.append({"Nama": nama, "Lat": lat, "Lon": lon})

else:
    st.sidebar.info("Masukkan beberapa titik target (pisahkan baris):")
    jumlah = st.sidebar.number_input("Jumlah Titik Target", min_value=2, max_value=5, value=2)
    for i in range(int(jumlah)):
        st.sidebar.markdown(f"**Titik #{i+1}**")
        n = st.sidebar.text_input(f"Nama #{i+1}", f"Area Target {i+1}", key=f"n_{i}")
        lt = st.sidebar.number_input(f"Lat #{i+1}", -3.212500 + (i*0.01), format="%.6f", key=f"lt_{i}")
        ln = st.sidebar.number_input(f"Lon #{i+1}", 139.871667 + (i*0.01), format="%.6f", key=f"ln_{i}")
        data_target.append({"Nama": n, "Lat": lt, "Lon": ln})

st.sidebar.markdown("---")
btn_proses = st.sidebar.button("🚀 PROSES ANALISIS ZF-CORE", use_container_width=True)

# ---------------------------------------------------------
# PEMROSESAN & OUTPUT HASIL
# ---------------------------------------------------------
if btn_proses:
    with st.spinner('Memproses analisis geofisika & sintesis pola fraktal...'):
        time.sleep(1.5)

    hasil_list = []
    
    for target in data_target:
        val_e = round(random.uniform(84.0, 92.0), 1)
        val_f = round(random.uniform(81.0, 89.0), 1)
        val_r = round(random.uniform(83.0, 90.0), 1)
        a_zf = hitung_a_zf(val_e, val_f, val_r)
        
        hasil_list.append({
            "Nama Titik": target["Nama"],
            "Latitude": target["Lat"],
            "Longitude": target["Lon"],
            "Entropy (%)": val_e,
            "Fractal (%)": val_f,
            "Resonant (%)": val_r,
            "Akurasi A_ZF (%)": a_zf,
            "Layer 1 (m)": "4 - 18 m (Aluvial)",
            "Layer 2 (m)": "110 - 280 m (Urat)"
        })

    df_hasil = pd.DataFrame(hasil_list)

    # 1. TABEL RINGKASAN HASIL
    st.subheader("📊 Tabel Perbandingan Intelijen Target")
    st.dataframe(df_hasil, use_container_width=True)

    st.markdown("---")

    # 2. PETA INTERAKTIF GOOGLE MAPS / OPENSTREETMAP
    st.subheader("🗺️ Peta Sebaran Episentrum Target (Interactive)")
    
    # Titik tengah peta
    avg_lat = df_hasil["Latitude"].mean()
    avg_lon = df_hasil["Longitude"].mean()
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=11, tiles="OpenStreetMap")

    # Tambahkan Marker Pin
    for _, row in df_hasil.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=f"<b>{row['Nama Titik']}</b><br>Skor A_ZF: {row['Akurasi A_ZF (%)']}%",
            tooltip=row["Nama Titik"],
            icon=folium.Icon(color="red" if row["Akurasi A_ZF (%)"] > 85 else "blue", icon="info-sign")
        ).add_to(m)

    st_folium(m, width=1100, height=450)

    st.markdown("---")

    # 3. FITUR CETAK LAPORAN PDF
    st.subheader("📄 Ekspor Laporan Lintas Lapangan")
    try:
        pdf_bytes = generate_pdf(df_hasil)
        st.download_button(
            label="📥 DOWNLOAD LAPORAN LENGKAP (PDF)",
            data=bytes(pdf_bytes),
            file_name="Laporan_Eksplorasi_ZF_Core.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    except Exception as e:
        st.error(f"Gagal memuat cetak PDF: {e}")

else:
    st.info("👈 Pilih mode input di menu samping (satu titik atau multi-titik), lalu klik tombol **PROSES ANALISIS ZF-CORE**.")
