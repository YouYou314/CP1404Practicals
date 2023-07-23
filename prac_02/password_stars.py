MINIMUM_LENGTH = 8


def main():
    password = get_password()
    print_password_asterisks(password)


def get_password():
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid input")
        password = input("Enter password: ")
    return password


def print_password_asterisks(password):
    print(len(password) * "*")


main()
