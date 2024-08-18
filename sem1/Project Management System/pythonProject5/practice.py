import random


def menu(): # menu for user to choose the option to perform
    print('''Please select an option:
    1: 'Add project details'
    2: 'Update project details'
    3: 'Delete project details'
    4: 'View project details'
    5: 'Save project details to text file'
    6: 'Random Spotlight selection'
    7: 'Record Awards and Recognitions'
    8: 'Visualize award-winning projects'
    9: 'Exit the program' ''')
    entered_number = input('Choose a number? ')
    return entered_number


# creating adding project details
def adding_project_details(projects):   # function to add project details
    project_id = input('Insert project ID: ')
    if project_id in projects:  # validating if the project id to be added already exists
        print("Error: Project ID already exists.")
        return

    new_project_name = input("Project Name: ")  # entering the new details
    new_category = input("Category: ")
    new_team_members = input("Team Members (separate each name by comma): ").split(',')
    new_description = input("Description: ")
    new_country = input("Country: ")

    if not all([new_project_name, new_category, new_team_members, new_description, new_country]):
        print("Error: Please provide all details for the project.")  # if the details are not provided to all the fields
        return

    projects[project_id] = {  # adding the added project details to the project dictionary
        "Project Name": new_project_name,
        "Category": new_category,
        "Team Members": new_team_members,
        "Description": new_description,
        "Country": new_country
    }
    print("Project successfully added.")


# updating the existing project details
def updating_project_details(projects):
    project_id = input("Enter the project ID to update: ")
    if project_id not in projects:  # Validating if the project id to be updated exists in the dictionary
        print("Error: Project ID not found.")
        return

    new_project_name = input("Project Name: ")  # enter the new project details to be updated
    new_category = input("Category: ")
    new_team_members = input("Team Members (separate each name by comma): ").split(',')
    new_description = input("Description: ")
    new_country = input("Country: ")

    if not all([new_project_name, new_category, new_team_members, new_description, new_country]):
        print("Error: Please provide all details for the project.")  # if all the fields are not provided
        return

    projects[project_id].update({  # updating the corresponding the details to the dictionary
        "Project Name": new_project_name,
        "Category": new_category,
        "Team Members": new_team_members,
        "Description": new_description,
        "Country": new_country
    })
    print("Project details updated successfully.")

# Deleting the project details function


def deleting_project_details(projects):
    project_id = input('Enter the ID of the project to delete: ')
    if project_id in projects:  # validating if the project id to be deleted exists.
        del projects[project_id]
        print("Project successfully deleted.")
    else:
        print("Project ID not found.")

# View function to view the projects


def view_project_details(projects):
    sorted_projects = sorted(projects.items(), key=lambda x: x[0])  # Sort projects by project ID
    for project_id, details in sorted_projects:  # To iterate through all the projects
        print(f"Project ID: {project_id}")  # Printing each project details
        print(f"Project Name: {details['Project Name']}")
        print(f"Category: {details['Category']}")
        print(f"Team Members: {', '.join(details['Team Members'])}")
        print(f"Description: {details['Description']}")
        print(f"Country: {details['Country']}")


# Save function to save dictionary into a text file


def save_project_details_to_text_file(projects):
    try:
        with open('project_details.txt', 'w') as file:  # Opening a file with write permission
            for project_id, project_details in projects.items():  # iterate through all projects
                file.write(f"Project ID: {project_id}\n")  # writing the project details into the file
                file.write(f"Project Name: {project_details['Project Name']}\n")
                file.write(f"Category: {project_details['Category']}\n")
                file.write(f"Team Members: {', '.join(project_details['Team Members'])}\n")
                file.write(f"Description: {project_details['Description']}\n")
                file.write(f"Country: {project_details['Country']}\n")
        print("Project details saved to 'project_details.txt' successfully.")
    except Exception as e:
        print(f"An error occurred while saving project details: {e}")


# function to load the contents from the text file


def load_project_details_from_text_file():
    projects = {}
    try:
        with open('project_details.txt', 'r') as file:  # opening the desired file with read permission
            current_project_id = None  # initialising the current_project_id to None
            current_project_details = {}  # creating an empty dictionary to hold the values of current project
            for line in file:  # iterating through each line
                if "Project ID:" in line:  # if line begins with project ID s the key
                    if current_project_id:  # if the project id is not null
                        projects[current_project_id] = current_project_details  # add details of current project id to projects
                    current_project_id = line.split(":")[1].strip()
                    current_project_details = {}
                elif current_project_id:  # else if the line starts with the key-value pairs
                    key, value = line.strip().split(":", 1)  # seperate key value pairs and store it to the variables
                    if key == "Team Members":
                        value = value.strip().split(", ")
                    else:
                        value = value.strip()
                    current_project_details[key] = value  # adding the key value pairs to current_project_details
            if current_project_id:
                projects[current_project_id] = current_project_details  # Don't forget to add the last project
        print("Project details loaded from 'project_details.txt' successfully.")
    except FileNotFoundError:
        print("Project details file not found. Starting with an empty project list.")
    except Exception as e:
        print(f"An error occurred while loading project details: {e}")
    return projects


# function to randomly select projects for spotlight
def random_spotlight_selection(projects):
    if not projects:  # checking if there are projects
        print("No projects available.")
        return

    categories = set(project['Category'] for project in projects.values())  # choosing the categories in projects
    selected_projects = {}

    for category in categories:
        projects_in_category = [pid for pid, pdetails in projects.items() if pdetails['Category'] == category]
        if not projects_in_category:
            continue
        selected_project_id = random.choice(projects_in_category)  # selecting a random project from each category
        selected_projects[category] = selected_project_id  # creating a dictionary where all selected projects stored

    print("Randomly Selected Project Details:")
    for category, project_id in selected_projects.items():  # iterating through all selected projects to prints them
        details = projects[project_id]
        print(f"{category} - Project ID: {project_id}, Project Name: {details['Project Name']}")


# function to choose award winners


def award_winning_projects(projects):
    if not projects:  # validating if there are projects
        print("No projects to evaluate.")
        return {}

    projects_points = {}
    for project_id, details in projects.items():  # iterating through all the projects
        print(f"Enter points for {project_id}:")  # entering the points for each chosen project
        points = [int(input(f"Judge {i + 1}: ")) for i in range(4)]
        projects_points[project_id] = sum(points)  # storing the sum of each project in a dictionary

    sorted_projects = sorted(projects_points.items(), key=lambda x: x[1], reverse=True) # sorting

    print("Award-Winning Projects:")
    award_results = {}
    for idx, (project_id, total_points) in enumerate(sorted_projects[:3]):
        place = ['1st', '2nd', '3rd'][idx] # assigning places
        print(f"{place} Place: Project ID {project_id}, Total Points: {total_points}")
        award_results[project_id] = 4 - idx  # Store 3 for 1st, 2 for 2nd, 1 for 3rd

    return award_results

def visualize_award_winning_projects(projects, award_results):
    if not award_results:  # validating if the chose projects have places
        print("No award data available.")
        return

    print("Visualizing Award-Winning Projects:")
    max_stars = 3  # max no of stars are 3
    star_lines = [[] for _ in range(max_stars)]

    project_names = []
    for project_id, place in award_results.items():  # iterates through all 3rd,2nd,1st projects
        num_stars = place  # number of stars to be printed
        project_names.append(projects[project_id]['Project Name'])  # adds their project names
        for i in range(max_stars):
            star_lines[i].append('*' if i < num_stars else ' ')  # appends the number of stars for each project

    for line in star_lines:
        print('   '.join(line))  # joins the lines with stars
    print('   '.join(project_names))  # joins the lines with project names

def main():
    projects = load_project_details_from_text_file()

    while True:
        option = menu()
        if option == '1':
            adding_project_details(projects)
        elif option == '2':
            updating_project_details(projects)
        elif option == '3':
            deleting_project_details(projects)
        elif option == '4':
            view_project_details(projects)
        elif option == '5':
            save_project_details_to_text_file(projects)
        elif option == '6':
            random_spotlight_selection(projects)
        elif option == '7':
            award_results = award_winning_projects(projects)
        elif option == '8':
            if 'award_results' in locals():
                visualize_award_winning_projects(projects, award_results)
            else:
                print("No award results available. Please record awards first.")
        elif option == '9':
            print("Exiting program...")
            break
        else:
            print("Invalid option! Please choose a number from 1 to 9.")



main()






