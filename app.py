import streamlit as st
from utils import get_dummy_response

st.set_page_config(page_title="Yabatech Faq Assitant", page_icon="🎓", layout="centered")

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

if "page" not in st.session_state:
    st.session_state.page = "welcome"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def welcome_page():
    st.markdown("### 🎓 Welcome to Yabatech Faq Assistant")
    st.image("assets/img.webp", width=100)
    st.subheader("Your Digital Learning Assistant")
    st.markdown("""
        🚀 *Yabatech EduBot helps you with:*
        - School admissions and processes
        - Course guidance and academic support
        - FAQs about payments, hostels, resumption, etc.

        Just click the button below to start chatting!
    """)
    if st.button("Start Chatbot 💬"):
        st.session_state.page = "chatbot"
        st.rerun()


from utils import process_image_with_ocr
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def chatbot_page():
    lottie_url = "https://assets5.lottiefiles.com/packages/lf20_v1yudgjg.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        st_lottie(lottie_json, speed=1, width=100, height=100)

    st.markdown("<h1 style='text-align: center;'>Yabatech Faq Assistant</h1>", unsafe_allow_html=True)

    st.caption("Ask your question below or upload an image:")

    # Chat history display
    chat_container = st.container()
    with chat_container:
        for speaker, message in st.session_state.chat_history:
            bubble_class = "user-bubble" if speaker == "You" else "bot-bubble"
            st.markdown(f"<div class='chat-bubble {bubble_class}'>{message}</div>", unsafe_allow_html=True)

    user_input = st.text_input("You:", key="user_input", placeholder="Type your question here...")
    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if user_input:
        if user_input.lower() == "quit":
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("EduBot", "Goodbye! Stay curious! 👋"))
        else:
            reply = get_dummy_response(user_input)
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("EduBot", reply))
        st.rerun()

    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        if st.button("Process Image"):
            extracted_text = process_image_with_ocr(uploaded_image)
            st.session_state.chat_history.append(("You", "Uploaded an image"))
            st.session_state.chat_history.append(("EduBot", f"Extracted Text: {extracted_text}"))
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🔙 Return Home"):
        st.session_state.page = "welcome"
        st.rerun()


if st.session_state.page == "welcome":
    welcome_page()
else:
    chatbot_page()