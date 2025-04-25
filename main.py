import login
import registeration
import project
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    print("============================")
    print("Welcome to Crowdfunding App!")
    print("============================")

def menu():
    print("1. Register")
    print("2. Login")
    print("3. Exit")

def project_menu():
    print("1. Create a Project")
    print("2. View All Projects")
    print("3. Edit My Projects")
    print("4. Delete My Project")
    print("5. Exit")

while True:
    clear_screen()
    welcome()
    menu()

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        registeration.register()

    elif choice == "2":
        user_email = login.login()
        
        if user_email:  # Only proceed if login was successful
            while True:
                clear_screen()
                welcome()
                project_menu()

                project_choice = input("Enter your choice (1-5): ")

                if project_choice == "1":
                    clear_screen()
                    project.create_project(user_email)
                elif project_choice == "2":
                    clear_screen()
                    project.view_all_projects()
                elif project_choice == "3":
                    clear_screen()
                    project.edit_my_projects(user_email)
                elif project_choice == "4":
                    clear_screen()
                    project.delete_my_project(user_email)
                elif project_choice == "5":
                    print("Returning to main menu...")
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
                    input("Press Enter to continue...")
        else:
            input("Press Enter to continue...")

    elif choice == "3":
        print("Exiting the Crowdfunding App. Goodbye!")
        print("--------------------------------------")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
        input("Press Enter to continue...")
