people = [
    {'name': "jamie",
     'done': "No",
     'task': "hello hi welcome",
     'date': '2024-02-01'},
    {'name': "john",
     'done': "Yes",
     'task': "hello hi welcome",
     'date': '2024-02-05' },
    {'name': "mary",
     'done': "No",
     'task': "good evening good morning goodnight",
     'date': '2024-02-01' },
    {'name': "mary",
     'done': "Yes",
     'task': "This stuff is tricky to learn!",
     'date': '2024-02-01'},
     {'name': "mary",
     'done': "No",
     'task': "This stuff is tricky to learn!",
     'date': '2024-02-01'},
     {'name': "jamie",
     'done': "No",
     'task': "This stuff is tricky to learn!",
     'date': '2024-02-01'},
    ]

user_stats_list = []
user_stats = []
user = {}
unique_val = []

# mimics list of text file string.
for line in people:
    string = ''
    for k, v in line.items():
        string += f"{v};"
    user_stats_list.append(string)
# ['john;Yes;hello hi welcome;2024-02-05;', 'mary;No;good evening good morning goodnight;2024-02-01;', 'mary;Yes;This stuff is tricky to learn!;2024-02-01;', 'jamie;No;hello hi welcome;2024-02-01;']
print(user_stats_list)

for i, p in enumerate(people):
        name = people[i]['name'] # create a unique instance of name

        if name not in unique_val:
             unique_val.append(name) # if name is unqiue add to list
             user = {people[i]['name']: 0} # create k/v pair with 0 as get me.
             user_stats.append(user)
        else:
            continue

print(user_stats)
print(user_stats[0])
print('-'*80)

for user in user_stats: # users dict
    for name, user_total in user.items(): # each user, and their user total
        for line in user_stats_list: # text file which represents the string line list. includes username, if task is complete, date etc.
            if name in line: # if the name key is found in the list
                user[name] += 1 # access the User dict on line 27, then increment the value for the matched user
                print(user_total, True, line)
print(user_stats)

for i, p in enumerate(user_stats_list):
    line = p.split(';')
    username = line[0]
    task = line[1]
    if username in unique_val:
        len(user_stats)
         
         
totals = []
users_list_container = []
print('-'*80)

for row in user_stats_list: # loop through text file / list?
    test_dict = {}
    split_row = row.split(';') # apply some string formatting
    print("#####",split_row)
    username = split_row[0]
    task_completed = split_row[1]
    not_complete = split_row[1]
    print("******",task_completed)
    test_dict = { # create an empty dict for each user
            'name': username,
            'total_tasks_assigned': 0,
            'percentage_assigned': 0,
            'percentage_complete': 0,
            'percentage_yet_complete': 0,
            'pecentage_overdue_not_complete': 0,
            'complete': 0,
            'not_complete': 0,
        }
    
    if username not in totals: # this creates a unique dict/key for each user
        totals.append(username) # add username to list
        users_list_container.append(test_dict)
    
    for row in users_list_container:

        # total number of tasks assigned to a user
        if row['name'] == username:
            row['total_tasks_assigned'] += 1
        
        # percentage assigned to the user they have complete
        if task_completed == 'Yes' and row['name'] == username:
            row['complete'] += 1
            
        # percentage the user has assigned to them from total.
        if not_complete == 'No' and row['name'] == username:
            row['not_complete'] += 1

        # percentage assigned, percentage complete, percentage yet to complete totals.
        row['percentage_assigned'] = (row['total_tasks_assigned'] / len(people)) * 100
        row['percentage_complete'] = (row['complete'] / row['total_tasks_assigned']) * 100
        row['percentage_yet_complete'] = (row['not_complete'] / row['total_tasks_assigned']) * 100

for user in users_list_container:
    print(user)
    print('-'*80)
print('-'*80)

# for i in users_list_container:
#     string = [
#         f"Name: {i['name']}",
#         f"Total tasks: {str(i['total_tasks_assigned'])}",
#         str(f"Percentage assigned: {i['percentage_assigned']}%"),
#         str(f"Percentage yet complete: {i['percentage_yet_complete']}%"),
#         "\n"
#     ]
#     sentence = f"\n".join(string)
#     print(sentence)

def write_to_file():
    with open("user_overview.txt", "w") as task_file:
            task_list_to_write = []
            for t in users_list_container:
                str_attrs = [
                    f"Name: {t['name']}",
                    f"Total tasks assigned: {str(t['total_tasks_assigned'])}",
                    str(f"Percentage of total tickets you have assigned: {t['percentage_assigned']}%"),
                    str(f"Percentage complete: {t['percentage_complete']}%"),
                    str(f"Percentage yet complete: {t['percentage_yet_complete']}%"),
                ]
                task_list_to_write.append("\n".join(str_attrs))
            task_file.write("\n\n".join(task_list_to_write))
    print("Task successfully added.") # Is this needed?

write_to_file()