import string
import random

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation

password = []
a = 1
while a <= 10 :
    password.extend(uppercase)
    password.extend(lowercase)
    password.extend(digits)
    password.extend(symbols)
    random.shuffle(password)
    a = a + 1


length = int(input("Enter what should be your password length : "))

real_password = []

index = 1
while index <= length :
    real_password.append(password[index])
    index = index + 1

print("".join(real_password))
