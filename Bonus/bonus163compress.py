import PySimpleGUI


label1 = PySimpleGUI.Text("Select Files to Compress ")
input1 = PySimpleGUI.Input()
button_choose1 = PySimpleGUI.FilesBrowse("Choose")

label2 = PySimpleGUI.Text("Select location to save ")
input2 = PySimpleGUI.Input()
button_choose2 = PySimpleGUI.FolderBrowse("Choose")

button_compress = PySimpleGUI.Button("Compress")

window = PySimpleGUI.Window("File Compressor",
                            layout=[[label1, input1, button_choose1],
                                    [label2, input2, button_choose2],
                                    [button_compress]])

window.read()
window.close()

