def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    found = False

    with open('users.txt', 'r') as file:
        for line in file:
            # Remove quotes if they exist
            line = line.strip().strip('"\'"')
            data = line.strip().split(":")
            if len(data) >= 4 and email == data[2] and password == data[3]:
                print("Login successful!")
                found = True
                return email
                
    if not found:
        print("Wrong email or password!")
        return None
