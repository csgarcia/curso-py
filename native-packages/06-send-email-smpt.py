# I skipped this one in the video, but here it is for reference.
# import smtplib
# from email.mime.text import MIMEText

# def send_email(subject, body, to):
#     msg = MIMEText(body)
#     msg['Subject'] = subject
#     msg['From'] = 'your_email@example.com'
#     msg['To'] = to

#     with smtplib.SMTP('smtp.example.com', 587) as server:
#         server.starttls()
#         server.login('your_email@example.com', 'your_password')
#         server.send_message(msg)
#     print(f"Email sent to {to}")

# for more on this video watch Sending mails and use of templates
