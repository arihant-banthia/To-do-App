import PySimpleGUI as sg

label1 = sg.Text("Enter Feet")
label2 = sg.Text("Enter inches")
input_feet = sg.InputText()
input_inches = sg.InputText()
button_convert = sg.Button("Convert")

window = sg.Window('CONVERTER', layout=[[label1, input_feet], [label2, input_inches], [button_convert]])
window.read()
window.close()