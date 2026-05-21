import requests
from send_mail import send_email


api_key = "your api key"
url = "The URL of the news you want to read" 

#ارسال درخواست
request = requests.get(url)

#تبدیل پاسخ دریافتی به دیکشنری (JSON)
content = request.json()

#دسترسی به عنوان و توضیحات
for article in content["articles"][:20]:
    if article["title"]is not None:
        body = "subject: Today's news" + "/n" + body +article["title"] + "/n" + article["description"] + 2*"/n"

body = body.encode("utf-8")
send_email(body)
