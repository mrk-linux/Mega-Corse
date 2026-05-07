import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    """Here is the English translation of your text:
    First, you need to activate your email's two-step verification. 
    Then, go to the app password section. Give your app a name, 
    then copy and paste the generated password."""

    username = "your email address"
    password = "The password provided by Gmail"

    """Storing the password in this way is not secure or correct; it must be stored in an encrypted (hashed) form."""
    receiver = "your email address"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port ,context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

