import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model/emotion_model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

emojis = {
    'happy': '😊',
    'sad': '😢',
    'angry': '😡',
    'fear': '😨',
    'surprise': '😲',
    'love': '❤️'
}

st.set_page_config(page_title="Emotion Detector", layout="centered")
st.title("🧠 AI Emotion Detector from Text")
st.markdown("Enter a sentence and the AI will detect the **emotion**.")

text_input = st.text_area("Your Text", height=150)

if st.button("Detect Emotion"):
    if text_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        vec = vectorizer.transform([text_input])
        prediction = model.predict(vec)[0]
        emoji = emojis.get(prediction, "")
        st.success(f"**Detected Emotion:** {prediction.capitalize()} {emoji}")
