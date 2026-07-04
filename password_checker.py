password = input("Enter your password: ")

has_upper = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in "!@#$%^&*" for char in password)
has_length = len(password) >= 8

score = 0

if has_upper:
    score = score + 1
if has_digit:
    score = score + 1
if has_symbol:
    score = score + 1
if has_length:
    score = score + 1

if score == 4:
    print("Strong Password! 💪")
elif score >= 2:
    print("Medium Password! 🟡")
else:
    print("Weak Password! 🔴")