import streamlit as st
import streamlit.components.v1 as components
st.title("moz")
st.markdown("""
<style>
div.stButton > button {
    width: 200px;
    height: 50px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.08);
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

if st.button("افکت ها"):
   st.switch_page("pages/effects.py")
if st.button("بازی ها"):
     st.switch_page("games.py")



