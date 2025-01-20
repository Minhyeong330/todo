import json

def file_open(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def user_check(file_path: str, user_name: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        if user_name in data["names"]:
            return True # Confusing part = If I didn't use 'return' -> Error occur (doesn't go throught the code) Why?
        elif user_name not in data["names"]:
            return False

def user_add(file_path, new_user):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
        data["names"].update({new_user: []})
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def view_user_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(data['names'])

def remove_user(file_path, list_number):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
        data['names'].pop(list_number)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def view_to_do_list(file_path, user_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(data["names"][user_name])

def add_to_do(file_path, user_name, new_to_do):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
        data["names"][user_name].append(new_to_do)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def remove_to_do(file_path, user_name, list_number):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        data = json.load(file)
        data["name"][user_name].pop(list_number)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def todo_list_option(file_path, todo_loop, user_name):
    todo_loop = True
    while todo_loop:
        try:
            options = int(input("Please select options: \n1. View list \n2. Add to list \n3. Remove from list \n4. Exit \n"))
            if options == 1:
                view_to_do_list(file_path, user_name)
            elif options == 2:
                new_to_do = input("Please enter to-do: ")
                add_to_do(file_path, user_name, new_to_do)
            elif options == 3:
                list_wanna_remove = int(input("Please enter the list number: "))
                remove_to_do(file_path, user_name, list_wanna_remove)
            elif options == 4:
                print("Exit")
                break
            else:
                raise ValueError
            todo_loop = False
            user_name_log = True
            log_in = True
        except ValueError:
            print("Please enter the right option")
            todo_loop = True
        question = True
        while question:
            try:     
                last_question = input("Do you still want to edit the list? [Y/N]: ").upper()
                if last_question == 'Y':
                    question = False
                    todo_loop = True
                elif last_question == 'N':
                    print("Done")
                    question = False
                else:
                    raise ValueError
            except ValueError:
                print("Please enter right answer")
                question = True