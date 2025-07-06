# 🧠 Emotion Detector from Text

This project is an **AI-powered Emotion Detection Web App** that identifies the emotional tone (like joy, sadness, anger, etc.) from user-provided text using Machine Learning and NLP.

---

## 💡 Features

- Detects emotion from text input (joy, sadness, anger, love, surprise, fear)
- Built using **Scikit-learn**, **Pandas**, and **Streamlit**
- Easy and clean web UI
- Trained on labeled emotion dataset

---

## 🚀 Technologies Used

- Python
- Scikit-learn
- Pandas
- Streamlit
- Natural Language Processing (NLP)

---

---

## 📊 Dataset

- Dataset File: [`data/emotion_dataset.csv`](data/emotion_dataset.csv)
- Source: [Kaggle – Emotions Dataset for NLP](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp)

## 👩‍💻 Author

**Rishwa Patel** – [GitHub Profile](https://github.com/rishwapatel16)




## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/rishwapatel16/emotion-detector.git

# Navigate to the project directory
cd emotion-detector

# Create a virtual environment (optional but recommended)
python -m venv .venv

# Activate the virtual environment
# For Windows:
.venv\Scripts\activate
# For macOS/Linux:
source .venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Train the model
python model_trainer.py

# Run the web app
streamlit run app.py
