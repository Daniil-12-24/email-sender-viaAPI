import smtplib
import ssl
import os


def email_sender(text):
    host = 'smtp.gmail.com'
    port = 465

    user_name = 'danikponomarev59@gmail.com'
    password = os.getenv('PASSWORD')

    receiver = 'danikponomarev59@gmail.com'
    context = ssl.create_default_context()

    message = text

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)