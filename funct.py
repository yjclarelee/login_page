# boolean for exit of while loop
EXIT = False


# boolean of whether the ID exists
def check_id(_id):
    with open("./info.txt", "r") as file:
        if _id in file.read():
            return True
        else:
            return False


# boolean of whether the ID and password matches
def check_id_password(_id, password):
    with open("./info.txt", "r") as file:
        id_password = _id + "," + password
        if id_password in file.read():
            return True
        else:
            return False


# sign up with ID and password
def sign_up(_id, password):
    with open("./info.txt", "a") as file:
        id_password = _id + "," + password + "\n"
        file.write(id_password)
