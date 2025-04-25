import re

def first_name_validation():
    while True:
        first_name = input("Enter your first name: ")

        if not first_name.isalpha():
            print("First name should only contain letters. Please try again.")
        else:
            return first_name

def last_name_validation():
    while True:
        last_name = input("Enter your last name: ")

        if not last_name.isalpha():
            print("Last name should only contain letters. Please try again.")
        else:
            return last_name

def email_validation():
    while True:
        email = input("Enter your email : ")
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, email):
            break
        else:
            print("Invalid email format")
    return email

def password_validation():
    while True:
        password = input("Enter your password: ")
        if 8 <= len(password) <= 20:
            confirm_password = input("Please confirm your password: ")
            if confirm_password != password:
                print("Passwords do not match. Please try again.")
            else:
                return password
        else:
            print("Password must be between 8 and 20 characters.")

def phone_validation():
    while True:
        phone = input('Enter your phone number: ')
        pattern = r'^01[0125][0-9]{8}$'
        if re.match(pattern, phone):
            break
        else:
            print("Invalid phone number")
    return phone


def register():
    first_name = first_name_validation()
    last_name = last_name_validation()
    email = email_validation()
    password = password_validation()
    phone = phone_validation()

    with open('users.txt', 'a') as file:
        file.write(f'"{first_name}:{last_name}:{email}:{password}:{phone}"\r')

    print("User registered successfully.")
