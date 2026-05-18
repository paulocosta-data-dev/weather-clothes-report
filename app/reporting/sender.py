import os
import smtplib

from email.mime.text import MIMEText


SMTP_SERVER = os.getenv("SMTP_SERVER")

SMTP_PORT = int(
    os.getenv("SMTP_PORT", 587)
)

SMTP_USERNAME = os.getenv(
    "SMTP_USERNAME"
)

SMTP_PASSWORD = os.getenv(
    "SMTP_PASSWORD"
)

EMAIL_FROM = os.getenv(
    "EMAIL_FROM"
)

EMAIL_TO = os.getenv(
    "EMAIL_TO"
)

EMAIL_TO_2 = os.getenv(
    "EMAIL_TO_2"
)


def send_email(
    subject,
    body
):

    recipients = [
        EMAIL_TO,
        EMAIL_TO_2
    ]

    recipients = [
        email
        for email in recipients
        if email
    ]

    message = MIMEText(
        body,
        "plain",
        "utf-8"
    )

    message["Subject"] = subject

    message["From"] = EMAIL_FROM

    message["To"] = ", ".join(recipients)

    with smtplib.SMTP(
        SMTP_SERVER,
        SMTP_PORT
    ) as server:

        server.starttls()

        server.login(
            SMTP_USERNAME,
            SMTP_PASSWORD
        )

        server.sendmail(
            EMAIL_FROM,
            recipients,
            message.as_string()
        )