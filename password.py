password = input("enter new password")
result = {}

if len(password) >= 8:
    result["length"] =True
else:
    result["length"] =False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

uppercase = False
for i in password :
    if i.upper():
        uppercase = True

result["upper-case"] = uppercase



if all(result.values()):
    print("strong Password")

else:
    print("weak Password")