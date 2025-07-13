import os
import json

REMINDER_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "reminders.json")

# Ensure directory exists
os.makedirs(os.path.dirname(REMINDER_FILE), exist_ok=True)

def load_reminders():
    if not os.path.exists(REMINDER_FILE):
        return []
    with open(REMINDER_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_reminder(data):
    reminders = load_reminders()
    reminders.append(data)
    with open(REMINDER_FILE, "w") as file:
        json.dump(reminders, file, indent=2)

def get_all_reminders():
    return load_reminders()

def delete_reminder_from_storage(medicine_name, time):
    reminders = load_reminders()
    updated = [r for r in reminders if not (r["medicine_name"] == medicine_name and r["time"] == time)]

    if len(reminders) == len(updated):
        return {"message": "Reminder not found."}

    with open(REMINDER_FILE, "w") as file:
        json.dump(updated, file, indent=2)
    return {"message": f"Deleted reminder for {medicine_name} at {time}"}

def update_reminder_in_storage(medicine_name, time, new_data):
    reminders = load_reminders()
    found = False
    for i, r in enumerate(reminders):
        if r["medicine_name"] == medicine_name and r["time"] == time:
            reminders[i] = new_data
            found = True
            break

    if not found:
        return {"message": "Reminder not found."}

    with open(REMINDER_FILE, "w") as file:
        json.dump(reminders, file, indent=2)

    return {"message": f"Updated reminder to {new_data['medicine_name']} at {new_data['time']}"}


