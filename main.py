import funct

while not funct.EXIT:
    choice = input("1. Sign up\n 2. Log in\n 3. Exit\n")

    if choice == '1':
        _id = input("Enter ID: ")
        if funct.check_id(_id):
            print("The ID exists!")
        else:
            password = input("Enter password: ")
            funct.sign_up(_id, password)
            print("Sign up complete.")

    elif choice == '2':
        _id = input("Enter ID: ")
        password = input("Enter password: ")
        if funct.check_id_password(_id, password):
            print("Valid password and ID.")
        else:
            if not funct.check_id(_id):
                print("ID does not exist.")
            else:
                print("ID and password do not match")

    elif choice == '3':
         print("Bye!")
         funct.EXIT = True

    else:
        print("Input is invalid. Choose from 1, 2, 3")