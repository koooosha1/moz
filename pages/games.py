import streamlit as st

st.title("🎮 بازی‌ها")

st.write("### ❌ دوز ⭕")

if "board" not in st.session_state:
    st.session_state.board = [""] * 9

if "turn" not in st.session_state:
    st.session_state.turn = "❌"

def play(i):
    if st.session_state.board[i] == "":
        st.session_state.board[i] = st.session_state.turn
        st.session_state.turn = "⭕" if st.session_state.turn == "❌" else "❌"

for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        i = row * 3 + col
        if cols[col].button(
            st.session_state.board[i] or " ",
            key=f"cell_{i}",
            use_container_width=True
        ):
            play(i)
            st.rerun()

if st.button("🔄 شروع دوباره"):
    st.session_state.board = [""] * 9
    st.session_state.turn = "❌"
    st.rerun()

if st.button("⬅️ برگشت"):
    st.switch_page("moz.py")
