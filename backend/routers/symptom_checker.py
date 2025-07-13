from fastapi import APIRouter
from model.request_model import SymptomInput
from utils.load_model import get_prediction

router = APIRouter(prefix="/predict", tags=["Symptom Checker"])

@router.post("/")
async def predict_disease(input_data: SymptomInput):
    if not input_data.symptoms:
        return {"error": "Please provide symptoms."}

    combined_symptoms = " ".join(input_data.symptoms).lower()
    prediction = get_prediction(combined_symptoms)
    return {"predicted_disease": prediction}
