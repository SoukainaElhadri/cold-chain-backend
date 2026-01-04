import smtplib
from email.mime.text import MIMEText


def send_email(subject, message, to_email):
    sender = "sou.elhadri@gmail.com"
    password = "ton_mot_de_passe"

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
