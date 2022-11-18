import random
import string

def add_a_password(name, password):
    password_dict = {"Website": name, "Password": password}
    password_list.append(password_dict)

def change_a_password(item, new_password):
    item["Password"] = new_password

def check_password(namesearch):
    for item in password_list:
        if item["Website"] == namesearch:
            return item
    print("Password for {0} not found.".format(namesearch))
    return None

def find_a_password(namesearch):
    item = check_password(namesearch)
    if item != None:
        print("Your password for {0} is: {1}".format(namesearch, item["Password"]))

def generate_password():
    generator = list(string.ascii_letters) + list(string.digits)
    pwlength = 0
    password = ""
    while pwlength < 4 or pwlength > 100:
        pwlength = int(input("How long do you want your password to be? "))
        if pwlength < 4 or pwlength > 100:
            print("Password too short/long! Please type a password length between 4-100")

    preference = input("Do you want to include special characters? ").lower()
    if preference == "y" or preference == "yes":
        generator = generator + list(string.punctuation)

    passwordlist = random.choices(generator, k = pwlength)
    for i in range(pwlength):
        password += passwordlist[i]

    name = input("Which website is this password for? ")
    password_dict = {"Website": name, "Password": password}
    password_list.append(password_dict)
    print("Your random", pwlength, "character long password is:", password)

def list_password():
    pos = 1
    if password_list == []:
        print("Password list is empty.")
    else:
        for item in password_list:
            print("{0}. {1}: {2}".format(pos, item["Website"], item["Password"]))
            pos += 1

def save_as(filename):
    file = open(filename, "w")
    for line in password_list:
        newline = "{0},{1}\n".format(line["Website"], line["Password"])
        file.write(newline)
    file.close()


print("This is a password generator, numbers, lower and upper case letters are included by default.")
password_list = []

program = True
while program == True:
    next_input = input("(a)dd a password, (c)hange a password, (f)ind a password, (g)enerate a new password, (l)ist passwords, (s)ave as, (q)uit: ")

    if next_input == "a":
        name = input("Which website is this password for? ")
        password = input("Enter the password you would like to add: ")
        add_a_password(name, password)
        
    elif next_input == "c":
        namesearch = input("Which password would you like to change? ")
        item = check_password(namesearch)
        if item != None:
            new_password = input("Enter the password you would like to change to: ")
            change_a_password(item, new_password)

    elif next_input == "f":
        namesearch = input("Which password would you like to find? ")
        find_a_password(namesearch)

    elif next_input == "g":
        generate_password()

    elif next_input == "l":
        list_password()
    
    elif next_input == "s":
        filename = input("Enter the name of the new file(with .txt at the end): ")
        save_as(filename)

    elif next_input == "q":
        program = False
