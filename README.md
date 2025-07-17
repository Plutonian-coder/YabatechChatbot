# 🎓 Yabatech FAQ Assistant

**Yabatech FAQ Assistant** is an intelligent chatbot built with [Streamlit](https://streamlit.io/) that helps Yaba College of Technology (Yabatech) students and applicants get quick answers to frequently asked questions — from admissions to hostels to payments and more.

![Chatbot Demo](assets/img.webp)

## 🔍 Features

- ✅ Clean and intuitive UI with custom Yabatech-themed styling
- ✅ Ask any question related to Yabatech and get instant answers
- ✅ Rapidfuzz-powered fuzzy matching for flexible question handling
- ✅ Built-in memory (chat history) per session
- ✅ Easy to update FAQs via Google Sheets

---

## 🚀 Live Demo (Optional)
> If deployed, insert Streamlit sharing or other deployment link here.

---

## 🛠️ How It Works

1. **Data Source**  
   Questions and answers are pulled directly from a public [Google Sheet CSV export](https://docs.google.com/spreadsheets/d/1iuMdndmSVkq8JR6Ir42s29-_3QHcGOX6/export?format=csv).

2. **Matching Logic**  
   Uses `rapidfuzz` to match the user’s question with the closest question in the dataset using `token_sort_ratio`.

3. **Custom UI**  
   Styled with embedded CSS to reflect Yabatech’s color scheme (green + yellow).

---

## 📦 Installation

```bash
git clone https://github.com/Plutonian-coder/YabatechChatbot.git
cd YabatechChatbot
pip install -r requirements.txt
streamlit run app.py
📁 Project Structure
bash
Copy code
YabatechChatbot/
├── assets/
│   └── img.webp          # Yabatech logo or assistant image
├── app.py                # Main chatbot code
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
🧠 Libraries Used
Streamlit

Pandas

Rapidfuzz

✨ Future Improvements
Add GPT-style fallback for unknown questions

Admin dashboard to manage questions/answers

Mobile-friendly UI adjustments

Add multilingual support

🙌 Acknowledgments
Designed with love for Yabatech students ❤️

Powered by open-source tools and public contributions

