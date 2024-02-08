# #--------------- Functions ------------------#

def incomplete_tasks(task_list):

    if task_list["name"] == name and task_list["done"] == "No":
        return True
    else:
        return False


def complete_tasks(task_list):
    if task_list["name"] == name and task_list["done"] == "Yes":
        return True
    else:
        return False


# #--------------- User data ------------------#
    
task_list = [
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
dict_keys = (['mary', 'jamie', 'john'])
user_dict_list = []


# #--------------- Code ------------------#

for name in dict_keys: # Loop over each name in the dictionary

    # create a dict based on the user
    name_dict = {
        "name": name,
        "complete": 0,
        "incomplete": 0,        
    }

    # user their name to filter against in the functions above.  Use the length of the filter value as the values inside each dict.
    # i.e. filter will check how many incomplete tasks a user has, then the return value, a list, it's length will be the value in the dict.
    x = list(filter(incomplete_tasks, task_list))
    y = list(filter(complete_tasks, task_list))

    if x:
        name_dict["incomplete"] = len(x)

    if y:
        name_dict["complete"] = len(y)
    
    name_dict["total assigned"] = len(x) + len(y)
    name_dict["total percentage assigned"] = f"{((name_dict['total assigned'] / len(task_list)) * 100):.1f}"
    name_dict["total percentage assigned complete"] = f"{((name_dict['complete'] / name_dict['total assigned'])* 100):.1f}%"
    name_dict["total percentage assigned incomplete"] = f"{((name_dict['incomplete'] / name_dict['total assigned'])* 100):.1f}%"
    
    user_dict_list.append(name_dict)

for user_dict in user_dict_list:
    for k,v in user_dict.items():
        print(k,v)
    print('-'*79)
