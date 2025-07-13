import joblib

# Load model and encoder
model = joblib.load('models\symptom_checker_model.pkl')
encoder = joblib.load('models\label_encoder.pkl')

# Input symptoms (space-separated string)
input_symptoms = "headache fever fatigue"

# Predict
pred_encoded = model.predict([input_symptoms])[0]
predicted_disease = encoder.inverse_transform([pred_encoded])[0]

print("🩺 Predicted Disease:", predicted_disease)
