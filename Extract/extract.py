import FreeSimpleGUI as sg
from zip_Extract import extract_archive

label1 = sg.Text("select archive:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("choose", key = "archive")

label2 = sg.Text("select dest dir:")
input2 = sg.Input()
choose_button2 = sg.FileBrowse("choose", key = "folder")

extract_button = sg.FolderBrowse("Extract")
output_label = sg.Text(key = "output", text_color = "green")

window = sg.Window("Archive Extractor", 
                layput = [[label1, input1, choose_button1],
                        [label2, input2, choose_button2],
                        [extract_button, output_label]])

while True:
        event, value = window.read()
        archivepath = value["archive"]
        dest_dir = value["folder"]
        extract_archive(archivepath, dest_dir)
        window["output"].update(value = "extrraction completed")

window.close()