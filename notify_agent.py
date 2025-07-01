from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

def send_whatsapp_notification(jobs):
    print("📦 Sending jobs:", jobs)

    if not jobs:
        print("ℹ️ No jobs to send.")
        return

    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_whatsapp = os.getenv("TWILIO_WHATSAPP_FROM")
    to_whatsapp = os.getenv("USER_WHATSAPP_TO")

    client = Client(account_sid, auth_token)

    message = "🧠 *Jobs Matched to Your CV:*\n\n"
    for job in jobs:
        message += f"*{job['title']}* at *{job['company']}*\n📍 {job['location']}\n🔗 {job['link']}\n\n"

    try:
        client.messages.create(
            from_=from_whatsapp,
            to=to_whatsapp,
            body=message
        )
        print("✅ WhatsApp message sent.")
    except Exception as e:
        print("❌ WhatsApp send failed:", e)
