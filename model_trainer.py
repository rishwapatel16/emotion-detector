import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

# Load dataset
df = pd.read_csv('data/emotion_dataset.csv')
print("🧪 Columns:", df.columns.tolist())
X = df['Text']
y = df['Emotion']

# Vectorize text
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vec, y)

# Save model and vectorizer
os.makedirs("model", exist_ok=True)
pickle.dump(model, open("model/emotion_model.pkl", "wb"))
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

print("✅ Model training complete and saved.")
