# cli --> command line interface
import functions
ask_user = "Type add, show, edit, complete or exit : "

while True:
    user_action = input(ask_user)
    user_action = user_action.strip().lower()

    if user_action.startswith('add'):
        todos = functions.get_todos()
        todo = user_action[4:]

        todos.append(todo + '\n')
        functions.set_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index+1}-{item}")

    elif user_action.startswith('edit'):
        number = int(user_action[5:])
        todos = functions.get_todos()
        todos[number-1] = input("Enter the task to be replaced with") + '\n'
        functions.set_todos(todos)

    elif user_action.startswith('complete'):
        number = int(user_action[9:])
        todos = functions.get_todos()
        todo_to_remove = todos.pop(number-1)
        functions.set_todos(todos)
        print("Removed today is : --> ", todo_to_remove)

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid action !!\n Try Again ")
        continue
