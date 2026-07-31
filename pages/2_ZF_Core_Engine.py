import streamlit as st
import json
import time
import websocket

st.set_page_config(page_title="ZF Core Engine", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #FFFFFF; }
    .appbar {
        background-color: #b71c1c;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        margin-bottom: 25px;
    }
    .predator-card {
        background-color: #1E1E1E;
        border: 1px solid #ff5252;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        margin-bottom: 25px;
    }
    .pair-text { color: #B0BEC5; font-weight: bold; font-size: 18px; }
    .price-text { color: #69F0AE; font-weight: bold; font-size: 42px; margin: 10px 0; }
    .badge-connected {
        background-color: #4CAF50;
        color: white;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    .badge-disconnected {
        background-color: #F44336;
        color: white;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='appbar'>ZF-CORE V16.7 PREDATOR</div>", unsafe_allow_html=True)

if 'is_connected' not in st.session_state:
    st.session_state.is_connected = False

card_placeholder = st.empty()
button_placeholder = st.empty()

def render_ui(pair, price, status, is_conn):
    badge_class = "badge-connected" if is_conn else "badge-disconnected"
    card_placeholder.markdown(f"""
        <div class="predator-card">
            <div class="pair-text">PAIR: {pair}</div>
            <div class="price-text">{price}</div>
            <div class="{badge_class}">{status}</div>
        </div>
    """, unsafe_allow_html=True)

if not st.session_state.is_connected:
    render_ui("EURUSD", "0.0000", "STANDBY", False)
    if button_placeholder.button("START PREDATOR", type="primary", use_container_width=True):
        st.session_state.is_connected = True
        st.rerun()

if st.session_state.is_connected:
    if button_placeholder.button("STOP PREDATOR", use_container_width=True):
        st.session_state.is_connected = False
        render_ui("EURUSD", "0.0000", "STANDBY", False)
        st.rerun()

    market_pair = "EURUSD"
    render_ui(market_pair, "0.0000", "ANALYZING MARKET...", True)

    try:
        ws = websocket.create_connection("wss://ws.binaryws.com/websockets/v3?app_id=1089")
        req = json.dumps({"ticks": f"frx{market_pair}", "subscribe": 1})
        ws.send(req)

        while st.session_state.is_connected:
            result = ws.recv()
            data = json.loads(result)

            if 'tick' in data and data['tick'] is not None:
                current_price = str(data['tick']['quote'])
                price_val = float(current_price)
                signal_status = "READY TO EXECUTE" if price_val > 0 else "ANALYZING MARKET..."
                render_ui(market_pair, current_price, signal_status, True)
                time.sleep(0.1)

    except Exception as e:
        st.session_state.is_connected = False
        render_ui(market_pair, "0.0000", "ERROR CONNECTING", False)
