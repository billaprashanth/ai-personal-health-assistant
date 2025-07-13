import joblib
import os

# Get base project directory
base_dir = os.path.dirname(os.path.dirname(__file__))

# Correct model paths
model_path = os.path.join(base_dir, "models", "symptom_checker_model.pkl")
encoder_path = os.path.join(base_dir, "models", "label_encoder.pkl")

# Load safely
try:
    model = joblib.load(model_path)
    label_encoder = joblib.load(encoder_path)
except Exception as e:
    raise RuntimeError(f"❌ Error loading model or encoder: {e}")

def get_prediction(symptom_text: str):
    pred_encoded = model.predict([symptom_text])[0]
    predicted_label = label_encoder.inverse_transform([pred_encoded])[0]
    return predicted_label
