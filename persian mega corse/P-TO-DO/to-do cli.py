import P_functions
import time # وارد کردن ماژول تایم در برنامه 
"""
این ماژول عملکرد های مختلفی برا شخصی سازی زمان ارائه می کند
"""


now = time.strftime("%b/%d/%Y,%p %I:%M")
"""
با توجه به مشخصات فرمت دوره زمانی ان را به یک رشته تبدیل می کند
"""
print(f"it is {now}")

while True:
    user_action = input("type add, show, edit , complete or exit:")
    user_action = user_action.strip()


    if  user_action.startswith("add"):
        todo = user_action[4:]

        todos = P_functions.read_todos()
        todos.append(todo + "\n")
        P_functions.write_todos(todos)
 
    elif 'show' in user_action:
        try:
            todos = P_functions.read_todos()
                
            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}-{item}"
                print(row)

        except ValueError:
            print("your command is not valid !")
            continue 
 
    elif user_action.startswith("edit"):

        number = int(user_action[5:])
        print(number)   
        number = number - 1

        todos = P_functions.read_todos()

        new_todo = input("enter new todo")
        todos[number] = new_todo + "\n"

        todos = P_functions.write_todos()
 
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = P_functions.read_todos()
            index = number -1 
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            todos = P_functions.write_todos()

            print(f"todo{todo_to_remove} was removed form the list")

        except IndexError:
            print("There is no item with number")
            continue
 
    elif user_action.startswith("exit"):
        break

    else :
        print("command is not valid !")

print("bye!")