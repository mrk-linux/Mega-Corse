import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    """ابتدا باید تایید دو مرحله‌ای ایمیل خود را فعال کنید.
    سپس به بخش رمز برنامه (app password) بروید.
    به برنامه‌تان یک اسم بدهید، بعد رمز ساخته‌شده را کپی و پیست کنید.»"""

    username = "ایمل شما"
    password = os.getenv("PASSWORD")
    """برای ایجاد متغیرهای محیطی (Environment Variables):
    کلید Win را بزنید → جستجو کنید Environment → وارد Advanced شوید → روی Environment Variables کلیک کنید.
    در بخش User Variables → گزینه New را بزنید → رمز عبور خود را وارد کنید و نام دلخواهی برای آن متغیر محیطی انتخاب کنید.
    به عنوان مثال: PASSWORD»
    """
    
    receiver = "ایمل شما"
    context = ssl.create_default_context()

    message = ""

    with smtplib.SMTP_SSL(host, port ,context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)