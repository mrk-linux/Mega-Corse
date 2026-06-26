import smtplib
import imghdr
from email.message import EmailMessage


PASSWORD = "your password geting your gmail"
SENDER = "app8flask@gmail.com"
RECEIVER = "app8flask@gmail.com"

def send_email(image_path):
    email_massage = EmailMessage()
    email_massage["subject"] = "New customer showed up!"
    email_massage.sent_content("Hey, we just a new  customer!")

    with open(image_path, "rb") as file:
        content = file.read()
        email_massage.add_alternative(content, maintype= "image",
                                    subtype= imghdr.what(None, content))
        
        gmail = smtplib.SMTP("smtp.gmail.com", 587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(SENDER, PASSWORD)
        gmail.sendmail(SENDER, RECEIVER, email_massage.as_string())
        gmail.quit()

if __name__ == "__main__":
    send_email(image_path= "images/19.png")