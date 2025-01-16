# Error Note - Always check '()' and indent

from todo_functions import *

file_path = 'todo.json'
file_open(file_path)

log_in = False

while not log_in:
    try:
        check_user = input('Do you have a username? [Y/N]: ').upper()
        if check_user == 'Y':
            user_name_log = False
            while not user_name_log:
                user_name = input('Please enter your username: ').upper()
                if user_check(file_path, user_name) == True:
                    print(f"Welcome, {user_name}!")
                    user_name_log = True
                    log_in = True
                elif user_check(file_path, user_name) == False:
                    user_retry = int(input("We can't find your username. Please enter correct username or create new one \n 1. New try \n 2. create a new user \n")) # Make sure the return by input() is always 'str'
                    retry = False
                    while not retry: # while loop for a correct username
                        try:
                            if user_retry == 1: # Go back to user_name_log - Why doesn't go back to while not user_name_log
                                user_name_log = False
                            elif user_retry == 2: # Add a new username, and go to todo
                                user_name = input('Please enter your new user name: ').upper()
                                user_add(file_path, user_name)
                                print(f"Welcome! {user_name} has been created")
                                user_name_log = True
                                log_in = True
                            retry = True
                        except ValueError:
                            print("Please type the right answer")
                            retry = False
        elif check_user == "N":
            user_name = input('Please enter your new username: ').upper()
            user_add(file_path, user_name)
            print(f"Welcome, {user_name} has been created")
            log_in = True
        else:
            raise ValueError
    except ValueError:
        print(f"Please enter the right answer")
        log_in = False

# Need to keep the username to add todo to the same user
# It will not add something to "todo". It will add something to "Username"

to_do_loop = True

while to_do_loop:
    to_do_options = input("Please select options: \n1. View list \n2. Add to list \n3. Remove from list \n4. Exit \n")
    if to_do_options == 1:
        view_to_do_list(file_path)
    elif to_do_options == 2:
        new_to_do = input("Please type in the new to-do list: ")
        add_to_do(file_path,new_to_do)
    elif to_do_options == 3:
        list_wanna_remove = int(input("Please enter the number of the list that you want to remove: "))
        remove_to_do(file_path, list_wanna_remove-1)
    elif to_do_options == 4:
        print("Exit")
    to_do_loop = False

last_edit = False

try:
    last_question = input("Do you still want to edit your list? [Y/N]: ").upper()
    if  last_question == 'Y':
        to_do_loop = True
    elif last_question == 'N':
        print('Done')
except ValueError:
    print("Please type in the right answer")