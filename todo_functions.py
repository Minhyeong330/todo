import json

def file_open(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def user_check(file_path, user_name):
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