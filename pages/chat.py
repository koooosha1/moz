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

# Nam va shoghl
if "name" not in st.session_state:
    st.session_state.name = None

if "job" not in st.session_state:
    st.session_state.job = None

# Namayesh payam haye ghabli
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


def bot_reply(text):
    text = text.lower().strip()

    # Salam
    if text in ["salam", "salaam", "hello", "hi"]:
        if not st.session_state.name:
            return "Salam! 👋\n\nKhoshhalam az ashnaei bahet!\n\nEsmet chie?"

    # Sabt esm
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
        return "Oh! Pas hanuz dari dars mikhuni! 📚\n\nDarse more alaghet chie?"

    if text in ["daneshju", "daneshju hastam"]:
        return "Oh! Pas hanuz dari dars mikhuni! 🎓\n\nReshteat chie?"

    if text in ["moalem", "moallem"]:
        return "Shoghle arzeshmandi dari! 👨‍🏫"

    if text in ["mohandes omran", "mohandes emran"]:
        return "Oh! Pas sakhteman misazi! 🏗️ Kheyli shoghle bahali dari!"

    if text in ["doctor", "pezeshk"]:
        return f"{st.session_state.name}، kheyli arzeshmande ke be mardom komak mikoni! ❤️"

    if text in ["motarjem"]:
        return "Pas yani zaban baladi! 🌎 Che zabani baladi?"

    # Zaban
    if text in ["englisi", "english", "engilisi", "engelisi"]:
        return "Oh che bahal! Zaban beynolmelali baladi! 🌎🇬🇧"

    # Sargarmi
    if text in ["varzesh", "varzesh kardan"]:
        return "Varzesh kardan ham tafrihe bahalie va ham baraye salemati mofide! 🏐⚽"

    if text in [
        "mosafarat",
        "mosafarat raftan",
        "mosafarat kardan",
        "safar",
        "safar raftan",
        "safar kardan"
    ]:
        return "Are manam asheghe mosafartam! ✈️🌍"

    # Ghaza
    if text == "pizza":
        return "Be-be! Manam asheghe pizzam! 🍕🍕"

    if text == "hamburger":
        return "Hamburger ham ke alie! 🍔🍔"

    # Zaban digar
    if text in ["na", "nah"]:
        return "OK 👍"

    if text in ["are"]:
        return "Che zabani? 🌎"

    # Pasokh pishfarz
    return f"{text}\n\nChe jaleb! 😄"


# Daryaft payam jadid
if prompt := st.chat_input("Payamet ro benevis..."):

    # Payam karbar
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # Pasokh robot
    answer = bot_reply(prompt)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)


# ==============================
# Efekt bozorg shodan dokme hengam mouse
# ==============================

st.markdown("""
<style>

button {
    transition: transform 0.2s ease-in-out;
}

button:hover
