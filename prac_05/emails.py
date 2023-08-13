def extract_name(email):
    parts = email.split('@')
    name_parts = parts[0].split('.')
    name = ' '.join(name_parts).title()
    return name


def main():
    user_data = {}

    email = input("Email: ")
    while True:

        name = extract_name(email)
        correct_name = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if correct_name == '' or correct_name == 'y':
            user_data[email] = name
        else:
            name = input("Name: ")
            user_data[email] = name
        email = input("Email: ")

