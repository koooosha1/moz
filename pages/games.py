import streamlit as st

st.title("🎮 بازی‌ها")

st.write("### ❌ دوز ⭕")

if "board" not in st.session_state:
    st.session_state.board = [""] * 9

if "turn" not in st.session_state:
    st.session_state.turn = "❌"

if "winner" not in st.session_state:
    st.session_state.winner = None

def check_winner():
    b = st.session_state.board

    wins = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, c, d in wins:
        if b[a] != "" and b[a] == b[c] == b[d]:
            return b[a]

    if "" not in b:
        return "مساوی"

    return None

def play(i):
    if st.session_state.board[i] == "" and st.session_state.winner is None:
        st.session_state.board[i] = st.session_state.turn

        result = check_winner()

        if result:
            st.session_state.winner = result
        else:
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

if st.session_state.winner == "❌":
    st.success("🏆 برنده: ضربدر ❌")

elif st.session_state.winner == "⭕":
    st.success("🏆 برنده: دایره ⭕")

elif st.session_state.winner == "مساوی":
    st.info("🤝 بازی مساوی شد!")

if st.button("🔄 شروع دوباره"):
    st.session_state.board = [""] * 9
    st.session_state.turn = "❌"
    st.session_state.winner = None
    st.rerun()

if st.button("⬅️ برگشت"):
    st.switch_page("moz.py")
