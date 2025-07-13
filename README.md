
# 💊 AI Personal Health Assistant

An AI-powered health assistant that helps users with:

- ✅ Symptom Checker (Disease Prediction)
- 🤖 GPT-Style Health Chatbot
- ❓ FAQ Viewer + Dynamic Updates
- ⏰ Reminder System & Alerts
- Toast Alerts

Built using **React.js + Tailwind CSS (Frontend)** and **FastAPI + ML (Backend)**.

---

## 📸 UI Preview

### 🔷 Landing Page
![Landing Page](ai-checker\public\screenshots\landing.png)

### 💡 Symptom Checker
![Symptom Checker](ai-checker\public\screenshots\symptom_checker.png)

### 🤖 Chatbot
![Chatbot](ai-checker\public\screenshots\chatbot.png)

### 💬 FAQ System
![FAQ](ai-checker\public\screenshots\faq.png)

### ⏰ Reminder System
![Reminder](ai-checker\public\screenshots\reminders.png)

---

## ⚙️ Tech Stack

### 👨‍💻 Frontend
- React.js
- Tailwind CSS
- Axios, Toastify
- React Router

### 🧠 Backend
- FastAPI (Python)
- Machine Learning (scikit-learn)
- pyttsx3 / gTTS + playsound
- APScheduler

---

## 🚀 How to Run Locally

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Setup
```bash
cd ai-checker
npm start
```

---

## 🔁 Features Summary

| Feature           | Description                                                   |
|------------------|---------------------------------------------------------------|
| Symptom Checker  | Predicts disease using ML based on user symptoms              |
| Chatbot          | GPT-style health assistant with keyword fallbacks             |
| FAQ System       | View FAQs + Admin adds new Q&A dynamically                    |
| Reminder System  | Add/View/Edit/Delete reminders + Email & Voice notification   |
| UI Polish        | Responsive UI, GSAP, Dark Mode, Toast Notifications           |

---

## 🛠 Folder Structure

```
ai-personal-health-assistant/
├── backend/
│   ├── main.py
│   ├── routers/
│   ├── model/
│   ├── utils/
│   └── data/
├── frontend/
│   ├── src/components/
│   └── public/screenshots/
```

---

## 🌐 Deployment

- Frontend:  Vercel
- Backend: Render 

---

## 📬 Contact

Made by **B Prashanth**  
📧 Contact: [prashanthbilla590@gmail.com]  
🔗 GitHub: [github.com/prashanthbilla](https://github.com/prashanthbilla)

---

## 📄 License

MIT License © 2025
