import streamlit as st
import streamlit.components.v1 as components
st.title("sait man!")

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

if st.button("🎈clik kon!🎈"):
    st.balloons()
    st.write("badkonaaakkk")


if st.button("❄clik kon!❄"):
    st.snow()
if st.button("🎉 کلیک کن! 🎉"):
    components.html("""
    <script>
        const colors = ["red", "blue", "yellow", "green", "purple", "orange"];

        for (let i = 0; i < 80; i++) {
            let confetti = document.createElement("div");

            confetti.innerHTML = "●";
            confetti.style.position = "fixed";
            confetti.style.left = Math.random() * 100 + "vw";
            confetti.style.top = "-20px";
            confetti.style.fontSize = "20px";
            confetti.style.color =
                colors[Math.floor(Math.random() * colors.length)];
            confetti.style.zIndex = "9999";

            document.body.appendChild(confetti);

            let speed = 2000 + Math.random() * 3000;

            confetti.animate(
                [
                    { transform: "translateY(0) rotate(0deg)" },
                    { transform: "translateY(100vh) rotate(720deg)" }
                ],
                {
                    duration: speed,
                    easing: "linear"
                }
            );

            setTimeout(() => confetti.remove(), speed);
        }
    </script>
    """, height=0)   
