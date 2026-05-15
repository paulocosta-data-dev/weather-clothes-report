import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv

load_dotenv()


def send_email(subject, body):

    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))

    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")

    email_from = os.getenv("EMAIL_FROM")

    recipients = [
        os.getenv("EMAIL_TO"),
        os.getenv("EMAIL_TO_2")
    ]

    recipients = [email for email in recipients if email]

    message = MIMEMultipart()

    message["From"] = email_from
    message["To"] = ", ".join(recipients)
    message["Subject"] = subject

    message.attach(
        MIMEText(body, "plain", "utf-8")
    )

    with smtplib.SMTP(smtp_server, smtp_port) as server:

        server.starttls()

        server.login(
            smtp_username,
            smtp_password
        )

        server.sendmail(
            email_from,
            recipients,
            message.as_string()
        )