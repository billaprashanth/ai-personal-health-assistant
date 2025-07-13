import joblib
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
from datetime import datetime

base_path = os.path.dirname(os.path.dirname(__file__))
log_path = os.path.join(base_path, "logs", "chat_log.json")


# File paths
vectorizer_path = os.path.join(base_path, "models", "faq_vectorizer.pkl")
vector_path = os.path.join(base_path, "models", "faq_vectors.pkl")
data_path = os.path.join(base_path, "models", "faq_data.pkl")

# Load models
vectorizer = joblib.load(vectorizer_path)
faq_vectors = joblib.load(vector_path)
faq_df = joblib.load(data_path)

def find_best_answer(user_input: str) -> str:
    user_vector = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vector, faq_vectors)
    
    best_idx = similarity.argmax()
    best_score = similarity[0, best_idx]

    if best_score < 0.5:
        return "I'm not sure. Please consult a medical professional."
    
    return faq_df.iloc[best_idx]['answer']

def add_faq(question: str, answer: str) -> str:
    global faq_df, vectorizer, faq_vectors

    # Add to DataFrame
    new_row = pd.DataFrame({"question": [question], "answer": [answer]})
    faq_df = pd.concat([faq_df, new_row], ignore_index=True)

    # Refit vectorizer
    vectorizer = TfidfVectorizer()
    faq_vectors = vectorizer.fit_transform(faq_df['question'])

    # Save everything
    joblib.dump(faq_df, data_path)
    joblib.dump(vectorizer, vectorizer_path)
    joblib.dump(faq_vectors, vector_path)

    return "✅ FAQ added and model updated"

def log_chat(user_q: str, bot_a: str):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "question": user_q,
        "answer": bot_a
    }

    # Create logs dir/file if not exist
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    if not os.path.exists(log_path):
        with open(log_path, 'w') as f:
            json.dump([], f)

    # Load, append, and save
    with open(log_path, 'r') as f:
        data = json.load(f)

    data.append(log_entry)

    with open(log_path, 'w') as f:
        json.dump(data, f, indent=2)