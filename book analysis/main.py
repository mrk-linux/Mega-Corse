import re

with open("miracle-in-the-andes.txt", "r", encoding="utf-8") as file:
    book = file.read()

pattern = re.compile("Chapter [0-9]+")
findings = re.findall(pattern, book)
print(len(findings))
