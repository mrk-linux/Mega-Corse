import requests
from send_mail import send_email


api_key = "your api key"
url = "The URL of the news you want to read" 

#Make request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Access the article titles description
for article in content["articles"][:20]:
    if article["title"]is not None:
        body = "subject: Today's news" + "/n" + body +article["title"] + "/n" + article["description"] + 2*"/n"

body = body.encode("utf-8")
send_email(body)
