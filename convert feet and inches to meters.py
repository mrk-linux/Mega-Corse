feet_inches = input("Enter feet and inches:")


def perse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.254
    return meters

f, i = perse(feet_inches)
print("fi", f, i)
result = convert(f, i)


if result < 1:
    print("kid is too small.")
else:
    print("kid can use the slide")