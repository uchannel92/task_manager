from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

people = [
    {'name': "john",
     'done': "Yes",
     'task': "hello hi welcome" },
    {'name': "mary",
     'done': "No",
     'task': "good evening good morning goodnight" },
    {'name': "mary",
     'done': "No",
     'task': "This stuff is tricky to learn!" },
     {'name': "jamie",
     'done': "No",
     'task': "hello hi welcome" },
    ]
username = 'jamie' # This is used to test if the 'logged in user' is the same person who wants to complete task.


for row_num, row in enumerate(people):
            print(row_num, row)    

loop_done = False
while (not loop_done):
    
    try:
        user_option = int(input("Enter a valid key to edit task or enter '-1' to return to MENU: "))    
    except (ValueError, NameError):
        print("Select a valid row number to edit.")
        loop_done = True
    else:    
        for row_num, row in enumerate(people):
            if user_option == -1:
                loop_done = True
            
            elif user_option == row_num: 
                    option = input("Select 'mc' to mark task complete or 'et' to edit task: ") # Mark task complete or edit task

                    if people[user_option]['done'] == "Yes":
                            print("This task is already complete")
                            loop_done = True
                    
                    elif option == 'mc': # edit the marked complete field

                        """ This is currently marked out for now as i believe it's redundant. If the tasks is complete then the only reason to check if the value is No, so it can be changed to Yes."""
                        """ Which means i may be able to remove the if statement 4 lines down. and just update the value from No to Yes """ 
                        # if people[user_option]['done'] == "Yes":
                        #     print("This task is already complete")
                        #     loop_done = True
                        if people[user_option]['done'] == "No":
                            people[user_option]['done'] = "Yes"
                            print("This task has been marked complete")
                            loop_done = True

                    elif option == 'et': # edit the edit task field

                        option = input("Enter 'eu' to edit username or 'edd' to edit the due date: ")

                        # if username already exists in people dict, the username can be updated 
                        if option == 'eu':
                            user_found = False
                            username = input('enter the name of new user: ')
                            for row in people:
                                if username in row.values():
                                    people[user_option]['name'] = username
                                    user_found = True
                            
                            if user_found == False:
                                print(f"User {username} not found")
                            else:
                                print("User updated")
                            loop_done = True

                        elif option == 'dd':

                            while True:
                                try: # update the due date field
                                    task_due_date = input("Due date of task (YYYY-MM-DD): ")
                                    due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                                    people[user_option]['task'] = task_due_date
                                    loop_done = True
                                    break
                                except ValueError:
                                    print("Invalid datetime format. Please use the format specified")                           
                        else:
                             print("Enter 'eu' to edit username or 'edd' to edit due date. You will return to the main menu.")
                             loop_done = True             
                    else:
                        print(("You need to enter 'mc' to markt task complete  or 'et' to edit task."))
                        loop_done = True
print(people)