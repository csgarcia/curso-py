import os
from twilio.rest import Client

from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into environment

sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
sender_phone = os.environ.get("TWILIO_SENDER_PHONE")

client = Client(sid, auth_token)
message = client.messages.create(
    body='Curso de Python con Twilio',
    from_=sender_phone,
    to='+50366667777'
)
