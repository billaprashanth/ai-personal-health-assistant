import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyttsx3
import os

def send_email(to_email: str, message: str):
    try:
        # Configure your email credentials
        sender_email = "your_email@example.com"  # Replace with your email
        sender_password = "your_password"        # Replace with your password

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = "Health Reminder Notification"

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()

        print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def play_voice_alert(message: str):
    try:
        engine = pyttsx3.init()
        engine.say(message)
        engine.runAndWait()
        print("🔊 Voice alert played.")
    except Exception as e:
        print(f"❌ Failed to play voice alert: {e}")
