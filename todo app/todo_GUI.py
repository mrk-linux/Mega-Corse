import functions
import FreeSimpleGUI as sg
import time
import os
os.chdir(os.path.dirname(__file__))


#sg.theme("") The them : for them input in the continue you can see and download them from network.

if not os.path.exists("todo.txt"):
    with open("todo.txt","w") as file:
        pass 

clock = sg.Text("",key="clock",text_color="purple")

label = sg.Text("type in a to-do")
input_box = sg.InputText(tooltip="enter to-do", key="todo")
add_button = sg.Button(image_size=(30, 30),image_source = "add.png", 
                    mouseover_colors="gray",tooltip="add todo", key = "add")



list_box = sg.Listbox(values= functions.read_todos(), 
                    key="todos", enable_events= True, 
                    size=[45, 10])

edit_button = sg.Button("edit")

complete_button=sg.Button(image_size=(35, 35), image_source="complete.png", 
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
    window["clock"].update(value= time.strftime("%b/%d/%Y\n%p %I:%M"))
    match event:

        case "add":
            todos = functions.read_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.read_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update("")
            except IndexError:
                sg.popup("Please select an item first",font=("helvetica", 14))

        case "complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.read_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
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