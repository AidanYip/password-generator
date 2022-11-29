import random
import string

# appends the website and its password to the password_list
def add_a_password(name, password, password_list):
    password_dict = {"Website": name, "Password": password}
    password_list.append(password_dict)

# changes the password the user requests
def change_a_password(item, new_password):
    item["Password"] = new_password

# check if password exists
def check_password(namesearch, next_input, password_list):
    for item in password_list:
        if item["Website"] == namesearch:
            return item
    if next_input != "a":
        print("Password for {0} not found.".format(namesearch))
    return None

# deletes all the passwords the user requests
def delete_password(namesearch, password_list):
    i = 0
    while i < len(password_list):
        if password_list[i]["Website"] == namesearch:
            del password_list[i]
            print("Password for {0} deleted successfully.".format(namesearch))
            i += 1
        i += 1

# find the password the user requests
def find_a_password(namesearch, next_input, password_list):
    item = check_password(namesearch, next_input, password_list)
    if item != None:
        print("Your password for {0} is: {1}".format(namesearch, item["Password"]))

# generates a new password
def generate_password(password_list):
    generator = string.ascii_letters + string.digits
    pwlength = 0
    password = ""
    # password length is limited between 4-100
    while pwlength < 4 or pwlength > 100:
        pwlength = int(input("How long do you want your password to be? "))
        if pwlength < 4 or pwlength > 100:
            print("Password too short/long! Please type a password length between 4-100")

    # ask if user wants to include special characters
    preference = input("Do you want to include special characters? ").lower()
    if preference == "y" or preference == "yes":
        generator = generator + string.punctuation

    # generate a list with pwlength(provided by the user) characters and mutate it to an empty string
    passwordlist = random.choices(generator, k=pwlength)
    for i in range(pwlength):
        password += passwordlist[i]

    # ask user for the website that the password is for and append it the the password_list
    name = input("Which website is this password for? ")
    password_dict = {"Website": name, "Password": password}
    password_list.append(password_dict)
    print("Your generated", pwlength, "character long password is:", password)

# list all passwords in password_list
def list_password(password_list):
    pos = 1
    if password_list == []:
        print("Password list is empty.")
    else:
        for item in password_list:
            print("{0}. {1}: {2}".format(pos, item["Website"], item["Password"]))
            pos += 1

# reads passwords from a .txt file
def read_file(txt, password_list):
    file = open(txt)
    nextline = file.readline()
    nextline = file.readline()[:-1]
    while nextline != "":
        nextline = nextline.split(",")
        add_a_password(nextline[0], nextline[1], password_list)
        nextline = file.readline()[:-1]

# save the passwords to a new .txt file
def save_as(filename, password_list):
    file = open(filename, "w")
    file.write("Website,Password\n")
    for line in password_list:
        newline = "{0},{1}\n".format(line["Website"], line["Password"])
        file.write(newline)
    file.close()

# main program (password manager)
def main(password_list):
    program = True
    while program == True:
        next_input = input("(a)dd a password, (c)hange a password, (d)elete a password, (f)ind a password, (g)enerate a new password, (l)ist passwords, (r)ead in a file, (s)ave as, (q)uit: ")

        if next_input == "a":
            name = input("Which website is this password for? ")
            item = check_password(name, next_input, password_list)
            if item == None:
                password = input("Enter the password you would like to add: ")
                add_a_password(name, password, password_list)
            # ask if user would like to replace the old password if it already exists
            else:
                choice = input("Password for {0} already exists, do you want to replace instead? ".format(item["Website"])).lower()
                if choice == "y" or choice == "yes":
                    password = input("Enter your new password: ")
                    change_a_password(item, password)

        elif next_input == "c":
            namesearch = input("Which password would you like to change? ")
            item = check_password(namesearch, next_input, password_list)
            if item != None:
                # asks user to type in previous password for verification
                correct = False
                check = input("Please type in the last password for this website for verification: ")
                while not correct:
                    if item["Password"] == check:
                        correct = True
                        new_password = input("Enter your new password: ")
                        change_a_password(item, new_password)
                    else:
                        check = input("Previous password incorrect! Please try again: ")

        elif next_input == "d":
            namesearch = input("Which password would you like to delete? ")
            delete_password(namesearch, password_list)

        elif next_input == "f":
            namesearch = input("Which password would you like to find? ")
            find_a_password(namesearch, next_input, password_list)

        elif next_input == "g":
            print("This is a password generator, numbers, lower and upper case letters are included by default.")
            generate_password(password_list)

        elif next_input == "l":
            list_password(password_list)
        
        elif next_input == "r":
            txt = input("Type in the name of the .txt file: ")
            read_file(txt, password_list)

        elif next_input == "s":
            filename = input("Enter the name of the new file(with .txt at the end): ")
            save_as(filename, password_list)

        elif next_input == "q":
            print("See you next time!")
            program = False
        
        else:
            print("Invalid input/Not implemented yet. Please try again.")

# register a new user
def register(login):
    register_name = input("Type in your new username: ")
    register_password = input("Type in your new password: ")
    user = {register_name: [], "password": register_password}
    users.append(user)
    print("You are now logged in!")
    password_list = user[register_name]
    main(password_list)
    login = False
    return login

print("This is a password manager.")
users = []

# open a file called users.txt and read in all the users and their respective passwords to a list
f = open("users.txt")
nextline = f.readline()
while nextline != "":
    nextline = nextline[:-1]
    bits = nextline.split(sep=",")
    users.append({bits[0]: [], "password": bits[1]})
    nextline = f.readline()
f.close()

# register/login the user
login = True
while login == True:
    if users == []:
        # ask user to register if users.txt is empty
        print("Welcome! Register with a username and password to start using the manager.")
        login = register(login)
    else:
        # ask user to register or login if users.txt is not empty
        while login == True:
            decision = input("Would you like to (l)ogin or (r)egister? ")
            if decision == "l":
                login_name = input("Username: ")
                for user in users:
                    if login_name in user:
                        while login == True:
                            login_password = input("Password: ")
                            if login_password == user["password"]:
                                password_list = user[login_name]
                                print("Welcome back {0}!".format(login_name))
                                main(password_list)
                                login = False
                            else:
                                print("Incorrect Password. Please try again.")
                if login == True:
                    print("Username not found. Please try again.")
                
            elif decision == "r":
                login = register(login)

# save the new user's username and password to users.txt for next time
f = open("users.txt", "w")
for user in users:
    keys = list(user.keys())
    f.write("{0},{1}\n".format(keys[0], user["password"]))
f.close()
