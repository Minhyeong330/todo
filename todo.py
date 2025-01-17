# Error Note - Always check '()' and indent

from todo_functions import *

file_path = 'todo.json'
file_open(file_path)

user_name = input('Please enter your username: ').upper()
logged_in = False

while not logged_in:
    try:
        user_name_log = False
        while not user_name_log:
            if user_check(file_path, user_name):
                print(f"Welcome, {user_name}!")
                user_name_log = True
                logged_in = True
            elif not user_check(file_path, user_name):
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
                        retry = True
                        logged_in = True
                    except ValueError:
                        print("Please type the right answer")
                        retry = False
            else:
                raise ValueError
    except ValueError:
        print(f"Please enter the right answer")
        logged_in = False

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
        else:
            raise ValueError
        todo_loop = False
        user_name_log = True
        logged_in = True
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