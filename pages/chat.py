import streamlit as st

st.set_page_config(
    page_title="Chat ba Robot",
    page_icon="🔵"
)

st.title("🔵 Chat ba Robot")
st.caption("Ba robot sohbat kon!")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "name" not in st.session_state:
    st.session_state.name = None

if "waiting_for_name" not in st.session_state:
    st.session_state.waiting_for_name = True

if "waiting_for_job" not in st.session_state:
    st.session_state.waiting_for_job = False


def normalize(text):
    text = text.lower().strip()

    words = {
        "سلام": "salam",
        "خوب": "khub",
        "خوبم": "khubam",
        "خوبم ممنون": "khubam mamnoon",
        "بد": "bad",
        "بدم": "badam",
        "خوب نیستم": "khub nistam",
        "آره": "are",
        "اره": "are",
        "نه": "na",
        "دانش آموز": "danesh amuz",
        "دانش‌آموز": "danesh amuz",
        "دانش آموزم": "danesh amuzam",
        "دانشجو": "daneshju",
        "دانشجو هستم": "daneshju hastam",
        "معلم": "moalem",
        "مهندس عمران": "mohandes omran",
        "دکتر": "doctor",
        "پزشک": "pezeshk",
        "مترجم": "motarjem",
        "انگلیسی": "englisi",
        "ورزش": "varzesh",
        "ورزش کردن": "varzesh kardan",
        "مسافرت": "mosafarat",
        "مسافرت رفتن": "mosafarat raftan",
        "مسافرت کردن": "mosafarat kardan",
        "سفر": "safar",
        "سفر رفتن": "safar raftan",
        "سفر کردن": "safar kardan",
        "پیتزا": "pizza",
        "همبرگر": "hamburger"
    }

    return words.get(text, text)


def bot_reply(text):
    text = normalize(text)

    if st.session_state.waiting_for_name:
        if text in ["salam", "salaam", "hello", "hi"]:
            return "Salam! 👋\n\nKhoshhalam az ashnaei bahet!\n\nEsmet chie?"

        st.session_state.name = text
        st.session_state.waiting_for_name = False
        st.session_state.waiting_for_job = True

        return f"Salam {text}! 👋\n\nAz ashnaei bahet khoshhalam!\n\nEsmet kheili ghashange! 😊\n\nShoghelet chie?"

    if st.session_state.waiting_for_job:
        st.session_state.waiting_for_job = False

        if text in ["danesh amuz", "daneshamuz", "danesh amuzam"]:
            return "Oh! Pas hanuz dari dars mikhuni! 📚\n\nDarse more alaghet chie?"

        if text in ["daneshju", "daneshju hastam"]:
            return "Oh! Pas hanuz dari dars mikhuni! 🎓\n\nReshteat chie?"

        if text in ["moalem", "moallem"]:
            return "Shoghle arzeshmandi dari! 👨‍🏫"

        if text in ["mohandes omran", "mohandes emran"]:
            return "Oh! Pas sakhteman misazi! 🏗️ Kheyli shoghle bahali dari!"

        if text in ["doctor", "pezeshk"]:
            return f"{st.session_state.name}, kheyli arzeshmende ke be mardom komak mikoni! ❤️"

        if text == "motarjem":
            return "Pas yani zaban baladi! 🌎 Che zaban baladi?"

    if "halat" in text or "khubi" in text:
        return "Khubam! 😄 To chetori?"

    if text in ["khub", "khubam", "khubam mamnoon"]:
        return "Khodaro shokr! 😊"

    if text in ["bad", "khub nistam", "badam"]:
        return "Chera? Age halet bade mitunim baadan sohbat konim 💔"

    if text in ["danesh amuz", "daneshamuz", "danesh amuzam"]:
        return "Oh! Pas hanuz dari dars mikhuni! 📚\n\nDarse more alaghet chie?"

    if text in ["daneshju", "daneshju hastam"]:
        return "Oh! Pas hanuz dari dars mikhuni! 🎓\n\nReshteat chie?"

    if text in ["moalem", "moallem"]:
        return "Shoghle arzeshmandi dari! 👨‍🏫"

    if text in ["mohandes omran", "mohandes emran"]:
        return "Oh! Pas sakhteman misazi! 🏗️ Kheyli shoghle bahali dari!"

    if text in ["doctor", "pezeshk"]:
        return f"{st.session_state.name}, kheyli arzeshmende ke be mardom komak mikoni! ❤️"

    if text == "motarjem":
        return "Pas yani zaban baladi! 🌎 Che zaban baladi?"

    if text in ["englisi", "english", "engilisi", "engelisi"]:
        return "Oh che bahal! Zaban beynolmelali baladi! 🌎🇬🇧"

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

    if text == "pizza":
        return "Be-be! Manam asheghe pizzam! 🍕🍕"

    if text == "hamburger":
        return "Hamburger ham ke alie! 🍔🍔"

    if text in ["na", "nah"]:
        return "OK 👍"

    if text == "are":
        return "Che zabani? 🌎"

    return text + "\n\nChe jaleb! 😄"


if prompt := st.chat_input("Payamet ro benevis..."):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user", avatar="🟢"):
        st.write(prompt)

    answer = bot_reply(prompt)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant", avatar="🔵"):
        st.write(answer)


st.markdown(
    """
    <style>
    button {
        transition: transform 0.2s ease-in-out;
    }

    button:hover {
        transform: scale(1.08);
    }
    </style>
    """,
    unsafe_allow_html=True
)
