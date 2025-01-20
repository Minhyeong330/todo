import json

def file_open(file_path: str) -> dict:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
      
def user_exists(file_path: str, user_name: str) -> dict:
    file_open(file_path)
    data = file_open(file_path)
    if user_name in data["names"]:
        return True # Confusing part = If I didn't use 'return' -> Error occur (doesn't go throught the code) Why?
    elif user_name not in data["names"]:
        return False

def user_add(file_path: str, new_user: str) -> dict:
    file_open(file_path)
    data = file_open(file_path)
    data["names"].update({new_user: []})
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def view_user_list(file_path: str) -> dict:
    file_open(file_path)
    data = file_open(file_path)
    print(data['names'])

def remove_user(file_path: str, list_number: str) -> dict:
    file_open(file_path)
    data = file_open(file_path)
    data['names'].pop(list_number)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def view_to_do_list(file_path: str, user_name: str) -> list:
    file_open(file_path)
    data = file_open(file_path)
    print(data["names"][user_name])

def add_to_do(file_path: str, user_name: str, new_to_do: str) -> list:
    file_open(file_path)
    data = file_open(file_path)
    data["names"][user_name].append(new_to_do)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def remove_to_do(file_path: str, user_name: str, list_number: int) -> list:
    file_open(file_path)
    data = file_open(file_path)
    data["name"][user_name].pop(list_number)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)