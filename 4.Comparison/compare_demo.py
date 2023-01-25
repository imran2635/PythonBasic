def login():
    username = input("enter your username: ")
    password = int(input("enter your password: "))

    if username == "abc" and password == 123456:
        print("Login successful")
    else:
        print("Error")


login()
