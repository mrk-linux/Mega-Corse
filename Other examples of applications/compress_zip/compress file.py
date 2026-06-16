import FreeSimpleGUI as sg
from ZIP_file import make_archive
label1 = sg.Text("select files to compass:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("choose", key="files")


label2 = sg.Text("select filer to folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("choose", key="folder")

compress_button = sg.Button("compress")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File compressor",
                layout=[[label1, input1, choose_button1],
                        [label2, input2, choose_button2],
                        [compress_button, output_label]])

while True:
        event, values = window.read()
        filepaths = values["files"].split(";")
        folder = values["folder"]
        make_archive(filepaths, folder)
        window["output"].update(value="comperession completed")
        

window.close()