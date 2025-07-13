from pydantic import BaseModel
from datetime import time

class Reminder(BaseModel):
    medicine_name: str
    time: str
