from fastapi import FastAPI
from backend.routers import symptom_checker, reminder, chatbot, faqbot
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="AI Personal Health Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(symptom_checker.router)
app.include_router(reminder.router)
app.include_router(faqbot.router, prefix="/faq")  
app.include_router(chatbot.router)

@app.get("/")
def home():
    return {"message": "Welcome to the AI Health Assistant API"}
