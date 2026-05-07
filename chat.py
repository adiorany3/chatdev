import streamlit as st
import random
import time
from datetime import datetime

# ========================================
# INISIALISASI CHAT
# ========================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ========================================
# UI HEADER
# ========================================
st.title("💬 Chat Sederhana")
st.markdown("---")

# ========================================
# TAMPILKAN HISTORY CHAT
# ========================================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        st.caption(message["time"])

# ========================================
# INPUT CHAT
# ========================================
if prompt := st.chat_input("Ketik pesan Anda disini... 👇"):
    
    # 1. TAMBAH PESAN USER
    user_message = {
        "role": "user", 
        "content": prompt,
        "time": datetime.now().strftime("%H:%M")
    }
    st.session_state.messages.append(user_message)
    
    with st.chat_message("user"):
        st.markdown(prompt)
        st.caption(datetime.now().strftime("%H:%M"))

    # 2. GENERATE RESPONSE BOT (Loading animation)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simulasi typing effect
        responses = [
            f"Halo! 👋 Terima kasih sudah chat jam {datetime.now().strftime('%H:%M')}",
            "Pesan Anda: **" + prompt + "** ✅ Diterima!",
            "Saya mengerti! 😊 Apa lagi yang bisa saya bantu?",
            "Wah keren! 🚀 Python emang juara buat chat app!",
            "Mantap! 💪 Chat ini dibuat pake Streamlit aja!",
            random.choice(["Yes!", "Sip!", "Oke!", "Mantap!", "Keren!"])
        ]
        
        # Pilih random response
        bot_response = random.choice(responses)
        
        # Typing effect
        for chunk in bot_response.split(" "):
            full_response += chunk + " "
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.05)
        
        message_placeholder.markdown(full_response)
        
        # Simpan response ke history
        bot_message = {
            "role": "assistant",
            "content": full_response,
            "time": datetime.now().strftime("%H:%M")
        }
        st.session_state.messages.append(bot_message)

# ========================================
# FOOTER
# ========================================
st.markdown("---")
with st.expander("ℹ️ Info"):
    st.info("""
    **Fitur:**
    - 💾 History tersimpan otomatis
    - ⏱️ Timestamp real-time
    - ✨ Typing effect
    - 🎲 Response random
    """)