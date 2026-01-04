username = "inoplanetyanka24"
password = "ino1234"

enter_username = (input("Enter your username: "))
enter_password = (input("Enter your password: "))
if (enter_username == "inoplanetyanka24"):
    if (enter_password == "ino1234"):
        print("Welcome!")
    else:
        print("Password is wrong.")
else:
    print("Username is wrong.")