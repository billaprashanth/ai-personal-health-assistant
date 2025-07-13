import json
import os
import sys
from fastapi import APIRouter
from pydantic import BaseModel
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.faq_bot import find_best_answer, add_faq, log_chat
from typing import List
import pandas as pd

router = APIRouter(tags=["Local FAQ Bot"])

class FAQInput(BaseModel):
    question: str

class NewFAQ(BaseModel):
    question: str
    answer: str

class ChatLogEntry(BaseModel):
    timestamp: str
    question: str
    answer: str

class ChatLogResponse(BaseModel):
    history: List[ChatLogEntry]

@router.get("/all")
def get_all_faqs():
    csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "Mental_Health_FAQ.csv")
    print(f"✅ Loading CSV from: {csv_path}")
    if not os.path.exists(csv_path):
        print("❌ File does not exist.")
        return {"faqs": []}
    try:
        df = pd.read_csv(csv_path)
        print("✅ Raw columns:", list(df.columns))
        if "Questions" not in df.columns or "Answers" not in df.columns:
            return {"error": "CSV must contain 'Questions' and 'Answers' columns."}
        df = df.dropna(subset=["Questions", "Answers"])
        df.rename(columns={"Questions": "question", "Answers": "answer"}, inplace=True)
        print("✅ Sample data:", df.head())
        return {"faqs": df.to_dict(orient="records")}    

    except Exception as e:
        return {"error": f"Failed to load FAQs: {str(e)}"}

@router.post("/")  
def faq_chat(payload: FAQInput):
    answer = find_best_answer(payload.question)
    log_chat(payload.question, answer)
    return {"response": answer}

@router.post("/add")
def add_faq_entry(payload: NewFAQ):
    message = add_faq(payload.question, payload.answer)
    return {"message": message}

@router.get("/history", response_model=ChatLogResponse)
def get_chat_history():
    log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "chat_log.json")
    if not os.path.exists(log_path):
        return {"history": []}
    
    with open(log_path, 'r') as f:
        data = json.load(f)

    return {"history": data}
