import streamlit as st

st.set_page_config(
    page_title="Chat ba Robot",
    page_icon="🤖"
)

st.title("🤖 Chat ba Robot")
st.caption("Ba robot sohbat kon!")

# Hafeze chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Hafeze esm
if "name" not in st.session_state:
    st.session_state.name = None

# Namayesh payam haye ghabli
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


def bot_reply(text):
    text = text.lower().strip()

    # Salam va esm
    if text in ["salam", "salaam", "hello", "hi"]:
        if not st.session_state.name:
            return "Salam! 👋\n\nKhoshhalam az ashnaei bahet!\n\nEsmet chie?"

    if not st.session_state.name:
        st.session_state.name = text
        return f"Salam {text}! 👋\n\nAz ashnaei bahet khoshhalam!\n\nEsmet kheili ghashange! 😊"

    # Vaziat
    if "halat" in text or "khubi" in text:
        return "Khubam! 😄 To chetori?"

    if text in ["khub", "khubam", "khubam mamnoon"]:
        return "Khodaro shokr! 😊"

    if text in ["bad", "khub nistam", "badam"]:
        return "Chera? Age halet bade mitunim baadan sohbat konim 💔"

    # Shoghl
    if text in ["danesh amuz", "daneshamuz", "danesh amuzam"]:
        return "Oh! Pas hanuz dari dars mikhuni! 📚\n\n
