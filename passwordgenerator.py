import random
import string

print("This is a password generator, numbers, lower and upper case letters are included by default.")
pwlength = 0
password = ""
generator = list(string.ascii_letters) + list(string.digits)

while pwlength < 4 or pwlength > 100:
    pwlength = int(input("How long do you want your password to be? "))

print("Do you want to include special characters?")
preference = input("Y/N? ").lower()
if preference == "y" or preference == "yes":
    generator = generator + list(string.punctuation)

passwordlist = random.choices(generator, k = pwlength)

for i in range(pwlength):
    password += passwordlist[i]

print("Your random", pwlength, "character long password is:", password)