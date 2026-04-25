import P_functions
import FreeSimpleGUI as sg
import time
import os


#os.chdir(os.path.dirname(__file__))
"""بخش دایرکتوری (پوشه) یک مسیر را برمی‌گرداند."""

#تم (theme) را در ادامه وارد کنید. شما می‌توانید تم‌ها را از شبکه مشاهده و دانلود کنید.

if not os.path.exists("to-do.txt"):
    with open("to-do.txt", "w") as file:
        file.write("")


clock = sg.Text("",key="clock",text_color="purple")

label = sg.Text("type in a to-do")
input_box = sg.InputText(tooltip="enter to-do", key="todo")
add_button = sg.Button("➕",image_size=(30, 30),
                    mouseover_colors="gray",tooltip="add todo", key = "add")



list_box = sg.Listbox(values= P_functions.read_todos(), 
                    key="todos", enable_events= True, 
                    size=[45, 10])

edit_button = sg.Button("✏️", tooltip= "edit todo")


complete_button=sg.Button("\u2705", image_size=(35, 35),
                        tooltip= "compile todo", key= "complete")

exit_button = sg.Button("exit",button_color=("white", "#dd3c30"),mouseover_colors="DarkRed")

window = sg.Window("my to-do app",
                    layout=[[clock],
                            [label],[input_box, add_button],
                            [list_box, [edit_button,complete_button]],
                            [exit_button]],
                    font=("helvetica", 14))

while True:
    event, values = window.read(timeout=500)
    if event == sg.WIN_CLOSED or event == "exit":
        break
    window["clock"].update(value= time.strftime("%b/%d/%Y\n%p %I:%M"))

    match event:

        case "add":
            todos = P_functions.read_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            P_functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"] + "\n"
                todos = P_functions.read_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                P_functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update("")
            except IndexError:
                sg.popup("Please select an item first",font=("helvetica", 14))

        case "complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = P_functions.read_todos()
                todos.remove(todo_to_complete)
                P_functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first",font=("helvetica", 14))

        case"exit":
            break

        case "todos":
            window['todo'].update(value=values["todos"][0])

        case sg.WIN_CLOSED:
            break

window.close()