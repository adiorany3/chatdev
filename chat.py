import streamlit as st
import random
import time
from datetime import datetime

# ========================================
# CONFIG SIMPLE
# ========================================
st.set_page_config(
    page_title="💬 Chat Sederhana",
    page_icon="💬",
    layout="wide"
)

# ========================================
# INIT STATE
# ========================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ========================================
# HEADER
# ========================================
st.title("💬 **Chat Bot Sederhana**")
st.markdown("---")

# ========================================
# SIDEBAR - SIMPLE CONTROLS
# ========================================
with st.sidebar:
    st.header("⚙️ Kontrol")
    
    if st.button("🗑️ Hapus Chat"):
        st.session_state.messages = []
        st.rerun()
    
    st.info(f"📊 Total Pesan: **{len(st.session_state.messages)}**")

# ========================================
# TAMPILKAN PESAN
# ========================================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        st.caption(message["time"])

# ========================================
# INPUT & RESPONSE
# ========================================
if prompt := st.chat_input("Ketik pesan Anda..."):
    
    # 1. Pesan USER
    with st.chat_message("user"):
        st.markdown(prompt)
        st.caption(datetime.now().strftime("%H:%M"))
    
    # 2. Loading
    with st.chat_message("assistant"):
        with st.spinner("🤔 Bot berpikir..."):
            time.sleep(1)
            
            # Response sederhana
            responses = [
                f"✅ Terima kasih! Pesan Anda: **{prompt}**",
                "🚀 Keren! Mau bikin apa lagi?",
                "😊 Bagus! Ada pertanyaan lain?",
                f"⏰ Jam {datetime.now().strftime('%H:%M')} - **{prompt}**",
                "✨ Chat ini pakai Streamlit!"
            ]
            
            response = random.choice(responses)
            st.markdown(response)
            st.caption(datetime.now().strftime("%H:%M"))

    # 3. Simpan ke history
    st.session_state.messages.append({
        "role": "user", 
        "content": prompt,
        "time": datetime.now().strftime("%H:%M")
    })
    st.session_state.messages.append({
        "role": "assistant", 
        "content": response,
        "time": datetime.now().strftime("%H:%M")
    })

# ========================================
# FOOTER
# ========================================
st.markdown("---")
st.caption("💡 **Ctrl+Enter** untuk kirim pesan")
