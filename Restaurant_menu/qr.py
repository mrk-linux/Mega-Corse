import qrcode

image = qrcode.make("https://192.168.1.1")
image.save(r"D:\porgram\code\mega corse\Restaurant_menu\qr.png")