from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    question: str

@router.post("/chat/")
def chat_with_bot(payload: ChatRequest):
    question = payload.question.lower()
    # Basic local response logic
    if "fever" in question:
        return {"answer": "It sounds like you may have a fever. Stay hydrated and rest. If it persists, consult a doctor."}
    elif "headache" in question:
        return {"answer": "For a headache, consider drinking water and resting. If severe, seek medical advice."}
    elif "covid" in question:
        return {"answer": "If you suspect COVID-19, monitor for symptoms like fever, cough, and loss of smell. Consider getting tested."}
    elif "hi" in question or "hello" in question:
        return {"answer": "Hello! I'm your AI health assistant. How can I help you today?"}
    elif "fatigue" in question or "tired" in question:
        return {"answer": "Fatigue can have many causes—ensure proper rest, hydration, and nutrition."}
    elif "stomach pain" in question or "abdominal pain" in question:
        return {"answer": "Stomach pain can be due to indigestion or infection. If severe, visit a healthcare provider."}
    elif "acidity" in question:
        return {"answer": "Acidity may be relieved by avoiding spicy food and eating on time. Try antacids if needed."}
    elif "diarrhea" in question:
        return {"answer": "Drink ORS or fluids. Avoid outside food. See a doctor if it persists more than 2 days."}
    elif "constipation" in question:
        return {"answer": "Constipation can be improved with fiber-rich foods, water, and light exercise."}
    elif "back pain" in question:
        return {"answer": "For back pain, avoid long sitting, stretch regularly, and apply heat if needed."}
    elif "asthma" in question or "breathing" in question:
        return {"answer": "If you're facing breathing difficulty or asthma symptoms, use your inhaler and consult your physician."}
    elif "pimples" in question or "acne" in question:
        return {"answer": "Acne is common. Keep your skin clean, avoid oily foods, and consult a dermatologist if severe."}
    elif "menstrual" in question or "period" in question:
        return {"answer": "For menstrual cramps, try hot water bags, hydration, and rest. Consult if cycles are irregular."}
    elif "anxiety" in question or "stress" in question:
        return {"answer": "Managing stress through meditation, breathing exercises, and talking to someone can help a lot."}
    elif "covid" in question or "corona" in question:
        return {"answer": "Common COVID-19 symptoms include fever, cough, and loss of taste. Get tested and isolate if needed."}
    elif any(x in question for x in ["thanks", "thank you", "bye", "goodbye"]):
        return {"answer": "You're welcome! Take care and feel free to reach out if you need anything else."}
    else:
        return {"answer": "I'm not sure about that. Please ask a health-related question or consult a doctor."}
