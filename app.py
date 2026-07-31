import streamlit as st

st.set_page_config(
    page_title="ZF System Engine",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("⚡ ZF SYSTEM ENGINE")
st.caption("Versi 16.7 - Trading Suite Dashboard")

st.markdown("---")
st.markdown("""
Selamat datang di **ZF System Engine**. Silakan pilih modul engine melalui menu **Sidebar** di sebelah kiri layar HP Anda:

* 📈 **1. ZF Forex Engine**: Modul analisis & eksekusi pasar Forex.
* ⚡ **2. ZF Core Engine**: Modul real-time tick stream Predator (WebSocket).
""")
