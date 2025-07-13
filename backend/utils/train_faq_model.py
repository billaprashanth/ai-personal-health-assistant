import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

# Load FAQ data
faq_df = pd.read_csv("data/faqs.csv")

# Fit TF-IDF on questions
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(faq_df['question'])

# Save models
model_path = os.path.join("backend/models", "faq_vectorizer.pkl")
index_path = os.path.join("backend/models", "faq_vectors.pkl")
data_path = os.path.join("backend/models", "faq_data.pkl")

os.makedirs("models", exist_ok=True)

joblib.dump(vectorizer, model_path)
joblib.dump(question_vectors, index_path)
joblib.dump(faq_df, data_path)

print("✅ FAQ model saved to 'models/' folder")
