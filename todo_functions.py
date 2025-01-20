import json

def file_open(file_path: str) -> dict:
    """Open a json file
    The type of file_path is 'str'
    The return type will be 'dict'
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
      
def user_exists(file_path: str, user_name: str) -> dict:
    """To find if there is a username as the values in the key
    The key is "names"
    """
    file_open(file_path)
    data = file_open(file_path)
    if user_name in data["names"]:
        return True # Confusing part = If I didn't use 'return' -> Error occur (doesn't go throught the code) Why?
    elif user_name not in data["names"]:
        return False

def add_user(file_path: str, new_user: str) -> dict:
    """Add new_user to "names" as a dictionary
    """
    file_open(file_path)
    data = file_open(file_path)
    data["names"].update({new_user: []})
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def view_user_list(file_path: str) -> dict:
    """View userlist. This is the values of username (key)
    """
    file_open(file_path)
    data = file_open(file_path)
    print(data['names'])

def remove_user(file_path: str, list_number: int) -> dict:
    """Remove user from the username
    List_number = index number of the username
    """
    file_open(file_path)
    data = file_open(file_path)
    data['names'].pop(list_number)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def view_to_do_list(file_path: str, user_name: str) -> list:
    """Show the to-do list according to 'user_name'
    """
    file_open(file_path)
    data = file_open(file_path)
    print(data["names"][user_name])

def add_to_do(file_path: str, user_name: str, new_to_do: str) -> list:
    """Add new_to_do to the to-do list
    """
    file_open(file_path)
    data = file_open(file_path)
    data["names"][user_name].append(new_to_do)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def remove_to_do(file_path: str, user_name: str, list_number: int) -> list:
    """Remove to-do from the lis. List_number is the index number.
    The index number starts at 0, so this function adjusts the start point to '1'
    """
    file_open(file_path)
    data = file_open(file_path)
    data["names"][user_name].pop(list_number-1)
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)