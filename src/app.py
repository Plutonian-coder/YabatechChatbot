import streamlit as st
from src.utils import get_openai_response, load_api_key

# Load API key
load_api_key()

st.set_page_config(page_title="Yabatech Faq Assitant", page_icon="🎓", layout="centered")

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("src/style.css")

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


from src.utils import process_image_with_ocr

if "theme" not in st.session_state:
    st.session_state.theme = "light"

def chatbot_page():
    # Theme toggle
    if st.button("Toggle Theme", key="theme_toggle"):
        st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"
        st.rerun()

    st.markdown(f"<div class='{st.session_state.theme}-theme'>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 12])
    with col1:
        st.image("assets/img.webp", width=50)
    with col2:
        st.markdown("<h1 style='padding-top: 5px;'>Yabatech Faq Assistant</h1>", unsafe_allow_html=True)

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
            reply = get_openai_response(user_input)
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