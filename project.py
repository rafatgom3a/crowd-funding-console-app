from datetime import datetime

def create_project(email):
    title = input("Enter project title: ")
    details = input("Enter project details: ")

    while True:
        target_input = input("Enter total target (e.g. 250000): ")
        try:
            target = float(target_input)
        except ValueError:
            print("Invalid target amount. Please enter a number.")
            continue

        start_date = input("Enter project start date (YYYY-MM-DD): ")
        end_date = input("Enter project end date (YYYY-MM-DD): ")

        try:
            start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
            end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

            if end_datetime >= start_datetime:
                break
            else:
                print("End date must be after start date. Please try again.")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    with open("projects.txt", "a") as file:
        file.write(f"{email}:{title}:{details}:{target}:{start_date}:{end_date}\n")

    print("Project created successfully!")
    input("\nPress Enter to continue...")



def view_all_projects():
        
    with open("projects.txt", "r") as file:
        projects = file.readlines()
        
    if not projects:
        print("\nNo projects available.")
    else:
        print("\n-- All Projects --")
        for i, line in enumerate(projects, 1):
            parts = line.strip().split(":", 5)
            if len(parts) >= 6:
                email, title, details, target, start, end = parts
                print(f"\nProject {i}")
                print(f"Owner: {email}")
                print(f"Title: {title}")
                print(f"Details: {details}")
                print(f"Target: {target} EGP")
                print(f"Duration: {start} to {end}")

    input("\nPress Enter to continue...")


def edit_my_projects(email):
    try:
        with open("projects.txt", "r") as file:
            projects = file.readlines()
        
        user_projects = []
        for i, project in enumerate(projects):
            if project.startswith(f"{email}:"):
                parts = project.strip().split(":", 5)
                if len(parts) >= 6:
                    _, title, _, _, _, _ = parts
                    user_projects.append((i, title))
        
        if not user_projects:
            print("You don't have any projects.")
            input("Press Enter to continue...")  
            return
            
        print("\nYour projects:")
        for i, (_, title) in enumerate(user_projects, 1):
            print(f"{i}. {title}")
            
        choice = int(input("\nSelect project to edit (0 to cancel): "))
        if choice == 0 or choice > len(user_projects):
            return
            
        project_index = user_projects[choice-1][0]
        
        print("\nEnter new details (press Enter to keep current):")
        old_parts = projects[project_index].strip().split(":", 5)
        
        title = input(f"Title [{old_parts[1]}]: ") or old_parts[1]
        details = input(f"Details [{old_parts[2]}]: ") or old_parts[2]
        target = input(f"Target [{old_parts[3]}]: ") or old_parts[3]
        start = input(f"Start date [{old_parts[4]}]: ") or old_parts[4]
        end = input(f"End date [{old_parts[5]}]: ") or old_parts[5]
        
        projects[project_index] = f"{email}:{title}:{details}:{target}:{start}:{end}\n"
        
        with open("projects.txt", "w") as file:
            file.writelines(projects)
            
        print("Project updated successfully!")
        input("Press Enter to continue...")
            
    except FileNotFoundError:
        print("No projects file found.")
        input("Press Enter to continue...")
    except (ValueError, IndexError):
        print("Invalid input. Please try again.")
        input("Press Enter to continue...")


def delete_my_project(email):
    try:

        with open("projects.txt", "r") as file:
            projects = file.readlines()
        
        user_projects = []
        for i, project in enumerate(projects):
            if project.startswith(f"{email}:"):
                parts = project.strip().split(":", 5)
                if len(parts) >= 6:
                    _, title, _, _, _, _ = parts
                    user_projects.append((i, title))
        
        if not user_projects:
            print("You don't have any projects.")
            input("Press Enter to continue...")
            return
            
        print("\nYour projects:")
        for i, (_, title) in enumerate(user_projects, 1):
            print(f"{i}. {title}")
            
        choice = int(input("\nSelect project to delete (0 to cancel): "))
        if choice == 0 or choice > len(user_projects):
            return
            
        project_index = user_projects[choice-1][0]
        
        confirm = input("Are you sure you want to delete this project? (y/n): ")
        if confirm.lower() != 'y':
            print("Deletion cancelled.")
            input("Press Enter to continue...")
            return
            
        del projects[project_index]
        with open("projects.txt", "w") as file:
            file.writelines(projects)
            
        print("Project deleted successfully!")
        input("Press Enter to continue...") 
            
    except FileNotFoundError:
        print("No projects file found.")
        input("Press Enter to continue...")   
    except (ValueError, IndexError):
        print("Invalid input. Please try again.")
        input("Press Enter to continue...")  