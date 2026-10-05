import streamlit as st

st.set_page_config(
    page_title="چت با ربات",
    page_icon="🤖"
)

st.title("🤖 چت با ربات")
st.caption("با ربات صحبت کن!")

# حافظه چت
if "messages" not in st.session_state:
    st.session_state.messages = []

# نمایش پیام‌های قبلی
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


def bot_reply(text):
    text = text.lower().strip()

    # سلام و اسم
    if not st.session_state.get("name"):
        st.session_state.name = text
        return f"سلام {text}! 👋\n\nاز آشنایی باهات خوشحالم!\n\nاسمت خیلی قشنگه! 😊"

    # وضعیت
    if "حالت" in text or "خوبی" in text:
        return "خوبم! 😄 تو چطوری؟"

    if text in ["خوب", "خوبم", "خوبم ممنون"]:
        return "خداروشکر! 😊"

    if text in ["بد", "خوب نیستم", "بدم"]:
        return "چرا؟ اگه حالت بده می‌تونیم بعداً صحبت کنیم 💔"

    # شغل
    if text in ["دانش آموز", "دانشاموز", "دانش آموزم"]:
        return "اوه! پس هنوز داری درس می‌خونی! 📚\n\nدرس مورد علاقه‌ات چیه؟"

    if text in ["دانشجو", "دانشجو هستم"]:
        return "اوه! پس هنوز داری درس می‌خونی! 🎓\n\nرشته‌ات چیه؟"

    if text in ["معلم", "موالم"]:
        return "شغل ارزشمندی داری! 👨‍🏫"

    if text in ["مهندس عمران", "مندس عمران"]:
        return "اوه! پس ساختمان می‌سازی! 🏗️ خیلی شغل باحالی داری!"

    if text in ["دکتر", "پزشک"]:
        return f"{st.session_state.name}، خیلی ارزشمنده که به مردم کمک می‌کنی! ❤️"

    if text in ["مترجم", "متارجم"]:
        return "پس یعنی زبان بلدی! 🌎 چه زبانی بلدی؟"

    # زبان
    if text in ["انگلیسی", "english", "engilisi", "engelisi"]:
        return "اوه چه باحال! زبان بین‌المللی بلدی! 🌎🇬🇧"

    # سرگرمی
    if text in ["ورزش", "ورزش کردن"]:
        return "ورزش کردن هم تفریح باحالیه و هم برای سلامتی مفیده! 🏐⚽"

    if text in [
        "مسافرت",
        "مسافرت رفتن",
        "مسافرت کردن",
        "سفر",
        "سفر رفتن",
        "سفر کردن"
    ]:
        return "آره منم عاشق مسافرتم! ✈️🌍"

    # غذا
    if text == "پیتزا":
        return "به‌به! منم عاشق پیتزام! 🍕🍕"

    if text == "همبرگر":
        return "همبرگر هم که عالیه! 🍔🍔"

    # زبان دیگر
    if text in ["نه", "نا"]:
        return "OK 👍"

    if text in ["آره", "اره"]:
        return "چه زبانی؟ 🌎"

    # پاسخ پیش‌فرض
    return f"{text}\n\nچه جالب! 😄"


# دریافت پیام جدید
if prompt := st.chat_input("پیامت رو بنویس..."):

    # پیام کاربر
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    # پاسخ ربات
    answer = bot_reply(prompt)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.write(answer)
