import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    """Here is the English translation of your text:
    First, you need to activate your email's two-step verification. 
    Then, go to the app password section. Give your app a name, 
    then copy and paste the generated password."""

    username = "your email address"
    password = os.getenv("PASSWORD")
    """ Press Win → search for Environment → go to Advanced → click Environment Variables.
    In the User Variables section → click New → enter your password and choose a name for the environment variable.
    For example: PASSWORD"
"""
    receiver = "your email address"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port ,context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

