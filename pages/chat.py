import streamlit as st

st.set_page_config(
    page_title="Chat ba Robot",
    page_icon="🔵"
)

st.title("🔵 Chat ba Robot")
st.caption("Ba robot sohbat kon!")

# ==============================
# Hafeze chat
# ==============================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "name" not in st.session_state:
    st.session_state.name = None

if "waiting_for_name" not in st.session_state:
    st.session_state.waiting_for_name = False

if "waiting_for_job" not in st.session_state:
    st.session_state.waiting_for_job = False


# ==============================
# Tabdil horoof va kalamat Farsi
# ==============================

def normalize_text(text):
    text = text.lower().strip()

    replacements = {
        "ی": "ی",
        "ي": "ی",
        "ک": "ک",
        "ك": "ک",
        "ۀ": "ه",
        "ة": "ه",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    fa_words = {
        "سلام": "salam",
        "سلاممم": "salam",
        "خوب": "khub",
        "خوبم": "khubam",
        "خوبم ممنون": "khubam mamnoon",
        "بد": "bad",
        "بدم": "badam",
        "خوب نیستم": "khub nistam",
        "آره": "are",
        "اره": "are",
        "نه": "na",
        "نا": "na",
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
        "همبرگر": "hamburger",
    }

    if text in fa_words:
        return fa_words[text]

    return text


# ==============================
# Finglish kardan matn
# ==============================

def to_finglish(text):
    table = {
        "ا": "a",
        "آ": "a",
        "ب": "b",
        "پ": "p",
        "ت": "t",
        "ث": "s",
        "ج": "j",
        "چ": "ch",
        "ح": "h",
        "خ": "kh",
        "د": "d",
        "ذ": "z",
        "ر": "r",
        "ز": "z",
        "ژ": "zh",
        "س": "s",
        "ش": "sh",
        "ص": "s",
        "ض": "z",
        "ط": "t",
        "ظ": "z",
        "ع": "'",
        "غ": "gh",
        "ف": "f",
        "ق": "gh",
        "ک": "k",
        "گ": "g",
        "ل": "l",
        "م": "m",
        "ن": "n",
        "و": "v",
        "ه": "h",
        "ی": "y",
        "ئ": "y",
        "ء": "",
        "‌": " ",
    }

    result = ""

    for char in text:
        result += table.get(char, char)

    return result


# ==============================
# Bot reply
# ==============================

def bot_reply(text):
    text = normalize_text(text)

    # Salam
    if text in ["salam", "salaam", "hello", "hi"]:
        if not st.session_state.name:
            st.session_state.waiting_for_name = True
            return """Salam! 👋

Khoshhalam az ashnaei bahet!

Esmet chie?"""

    # Gereftan esm
    if st.session_state.waiting_for_name:
        st.session_state.name = text
        st.session_state.waiting_for_name = False
        st.session_state.waiting_for_job = True

        return f"""Salam {text}! 👋

Az ashnaei bahet khoshhalam!

Esmet kheili ghashange! 😊

Shoghelet chie?"""

    # Gereftan shoghl
    if st.session_state.waiting_for_job:
        st.session_state.waiting_for_job = False

        if text in ["danesh amuz", "daneshamuz", "danesh amuzam"]:
            return """Oh! Pas hanuz dari dars mikhuni! 📚

Darse more alaghet chie?"""

        if text in ["daneshju", "daneshju hastam"]:
            return """Oh! Pas hanuz dari dars mikhuni! 🎓

Reshteat chie?"""if text in ["moalem", "moallem"]:
            return "Shoghle arzeshmandi dari! 👨‍🏫"

        if text in ["mohandes omran", "mohandes emran"]:
            return "Oh! Pas sakhteman misazi! 🏗️ Kheyli shoghle bahali dari!"

        if text in ["doctor", "pezeshk"]:
            return f"{st.session_state.name}, kheyli arzeshmende ke be mardom komak mikoni! ❤️"

        if text in ["motarjem"]:
            return "Pas yani zaban baladi! 🌎 Che zaban baladi?"

    # Vaziat
    if "halat" in text or "khubi" in text:
        return "Khubam! 😄 To chetori?"

    if text in ["khub", "khubam", "khubam mamnoon"]:
        return "Khodaro shokr! 😊"

    if text in ["bad", "khub nistam", "badam"]:
        return "Chera? Age halet bade mitunim baadan sohbat konim 💔"

    # Shoghl
    if text in ["danesh amuz", "daneshamuz", "danesh amuzam"]:
        return """Oh! Pas hanuz dari dars mikhuni! 📚

Darse more alaghet chie?"""

    if text in ["daneshju", "daneshju hastam"]:
        return """Oh! Pas hanuz dari dars mikhuni! 🎓

Reshteat chie?"""

    if text in ["moalem", "moallem"]:
        return "Shoghle arzeshmandi dari! 👨‍🏫"

    if text in ["mohandes omran", "mohandes emran"]:
        return "Oh! Pas sakhteman misazi! 🏗️ Kheyli shoghle bahali dari!"

    if text in ["doctor", "pezeshk"]:
        return f"{st.session_state.name}, kheyli arzeshmende ke be mardom komak mikoni! ❤️"

    if text in ["motarjem"]:
        return "Pas yani zaban baladi! 🌎 Che zaban baladi?"

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
    return f"{to_finglish(text)}\n\nChe jaleb! 😄"


# ==============================
# Daryaft payam jadid
# ==============================

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


# ==============================
# Rang avatar ha
# ==============================

st.markdown("""
<style>

[data-testid="stChatMessageAvatarUser"] {
    background-color: #22c55e !important;
}

[data-testid="stChatMessageAvatarAssistant"] {
    background-color: #3b82f6 !important;
}

button {
    transition: transform 0.2s ease-in-out;
}

button:hover {
    transform: scale(1.08);
}

</style>
""", unsafe_allow_html=True)
