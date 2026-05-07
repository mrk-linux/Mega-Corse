import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    """ابتدا باید تایید دو مرحله‌ای ایمیل خود را فعال کنید.
    سپس به بخش رمز برنامه (app password) بروید.
    به برنامه‌تان یک اسم بدهید، بعد رمز ساخته‌شده را کپی و پیست کنید.»"""

    username = "ایمل شما"
    password = "رمز تولید شده "

    """ذخیره کردن رمز عبور به این روش امن یا صحیح نیست؛ باید به صورت رمزگذاری‌شده (هش‌شده) ذخیره شود."""
    receiver = "ایمل شما"
    context = ssl.create_default_context()

    message = ""

    with smtplib.SMTP_SSL(host, port ,context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)