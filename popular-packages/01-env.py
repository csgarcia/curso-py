import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into environment

api_key = os.environ.get("SENDGRID_API_KEY")
email = os.environ.get("SENDGRID_EMAIL")
print(api_key)
print(email)

message = Mail(
    from_email=email,
    to_emails='sendTo@example.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>Curso de Python</strong>'
)

try:
    sg = SendGridAPIClient(api_key)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e)
