import functions
import FreeSimpleGUI as sg

label = sg.Text("type in a to-do")
input_box = sg.InputText("enter to-do")
add_button = sg.Button("add")

window = sg.Window("my to-do app", layout=[[label], [input_box, add_button]])
window.read()
window.close()