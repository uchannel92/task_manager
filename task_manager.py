# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""] # if the line for each file is NOT empty, append to this list.

# --------------- Menu Functions --------------- 
def options():
    
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    ds - Display statistics
    e - Exit
    : ''').lower()

    return menu     

# --------------- Register User Function --------------- 
def reg_user():

    while True:
        # Set a flag for finding a potential duplicate user
        duplicate_username = False
        new_username = input("New Username: ")
        new_username = new_username.strip()
        new_username = new_username.lower() # Add validation for the Password and make it more complex, can remove it here.

        if len(new_username) < 5:
            print("Usernames less than 5 characters will be rejected")
            continue

        # - Check if the new username has already been used
        if new_username in username_password.keys():
            duplicate_username = True
            print(f"{new_username} has already been used. Please choose a new username.")      

        if (not duplicate_username):
            # - Request input of a new password
            new_password = input("New Password: ") # Add validation for the Password and make it more complex, can remove it here.

            # - Request input of password confirmation.
            confirm_password = input("Confirm Password: ")

            # - Check if the new password and confirmed password are the same.
            if new_password == confirm_password:
                # - If they are the same, add them to the user.txt file,
                print("New user added")
                username_password[new_username] = new_password
                
                with open("user.txt", "w") as out_file:
                    user_data = []
                    for k in username_password:
                        user_data.append(f"{k};{username_password[k]}")
                    out_file.write("\n".join(user_data))

                    break # Once you has been created, break the loop.
            else:
                print("Your passwords do not match.. please try again.")


# --------------- Add Task Functions --------------- 
def add_task():
    '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
    
    while True:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        break

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")


# --------------- View All Tasks Functions --------------- 
def view_all():
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''

        for index, t in enumerate(task_list):
            disp_str = f"Task number: {index}\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)


# --------------- View All Tasks Functions --------------- 
def view_mine():
        '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)'''
        view_all()

        loop_done = False
        while (not loop_done):

            try:
                task_number = int(input("Enter a valid task number to edit task or enter '-1' to return to MENU: "))
            except (ValueError, NameError):
                print("Select a valid row number to edit.")
                loop_done = True
            else:
                for task_num, t in enumerate(task_list):
                    if task_number == -1:
                        loop_done = True
                    
                    elif task_number == task_num:
                            if t['username'] != curr_user:
                                print("This task is not assigned to you. please select a task assigned to you.")
                                loop_done = True
                                #print(t)
                            else:
                                option = input("Select 'mc' to mark task complete or 'et' to edit task: ")
                            
                                if option == 'mc':
                                    if t['completed'] == True:
                                        print("This task is already complete")
                                        loop_done = True

                                    else:
                                        t['completed'] = True # update task value to true
                                        print("task has been marked as complete.")
                                        loop_done = True
                                
                                elif option == 'et': # edit the edit task field
                                    option = input("Enter 'eu' to edit username or 'edd' to edit the due date: ")

                                    if option == 'eu':
                                        user_found = False
                                        while (not user_found):
                                            username = input("Enter the new username to be assigned to this task: ")
                                            for task in task_list:
                                                if username in task.values():
                                                    task_list[task_number]['username'] = username
                                                    user_found = True
                                            
                                            if user_found == False:
                                                print(f"Username {username} not found")
                                                user_found = True
                                                loop_done = True
                                            else:
                                                print("Username has been updated")
                                                user_found = True
                                                loop_done = True
                                    
                                    elif option == 'edd':
                                        while True:
                                            try: # update the due date field
                                                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                                                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                                                task_list[task_number]['due_date'] = due_date_time
                                                print(f"Due date has been updated to {task_due_date}")
                                                loop_done = True
                                                break
                                            except ValueError:
                                                print("Invalid datetime format. Please use the format specified")   
                                    else:
                                        print("Enter 'eu' to edit username or 'edd' to edit due date. You will return to the main menu.")
                                        loop_done = True
                                else:
                                    print(("You need to enter 'mc' to mark task complete  or 'et' to edit task."))
                                    loop_done = True         
        
        # update text file with changes made.
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


# --------------- Main Code ---------------  
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()
            
    elif menu == 'vm':
        view_mine()
        # '''Reads the task from task.txt file and prints to the console in the 
        #    format of Output 2 presented in the task pdf (i.e. includes spacing
        #    and labelling)
        # ''' 
        # for index, t in enumerate(task_list):
        #     if t['username'] == curr_user:
        #         disp_str = f"Task number: {index}\n"
        #         disp_str += f"Task: \t\t {t['title']}\n"
        #         disp_str += f"Assigned to: \t {t['username']}\n"
        #         disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        #         disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        #         disp_str += f"Task Description: \n {t['description']}\n"
        #         print(disp_str)

        # selected_task = input('Select your task:')

    
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
   # print('-'*80)
