from fastapi import APIRouter, BackgroundTasks
from model.reminder_model import Reminder
from utils.reminder_store import save_reminder, get_all_reminders, delete_reminder_from_storage, update_reminder_in_storage
from apscheduler.schedulers.background import BackgroundScheduler
import time as time_module
from datetime import datetime, timedelta

router = APIRouter(tags=["Medication Reminder"])

scheduler = BackgroundScheduler()
scheduler.start()

def reminder_job(medicine_name):
    print(f"🔔 Reminder: Time to take your medicine - {medicine_name}")

@router.post("/reminders")
def add_reminder(reminder: Reminder):
    save_reminder(reminder.dict())

    # Extract time and schedule job
    hour, minute = map(int, reminder.time.split(":"))
    scheduler.add_job(
        reminder_job,
        "cron",
        hour=hour,
        minute=minute,
        args=[reminder.medicine_name],
        id=f"{reminder.medicine_name}-{reminder.time}",
        replace_existing=True
    )
    return {"message": f"Reminder for {reminder.medicine_name} set at {reminder.time}"}

@router.get("/get/reminder")
def list_reminders():
    return get_all_reminders()

# DELETE Reminder
@router.delete("/reminders/{medicine_name}/{time}")
def delete_reminder(medicine_name: str, time: str):
    return delete_reminder_from_storage(medicine_name, time)

# PATCH Reminder
@router.patch("/reminders/{medicine_name}/{time}")
def update_reminder(medicine_name: str, time: str, new_data: Reminder):
    return update_reminder_in_storage(medicine_name, time, new_data.dict())
