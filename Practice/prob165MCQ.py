import PySimpleGUI as sg

label = sg.Text("What are dolphins :")
option1 = sg.Radio("Amphibian", group_id="ques1")
option2 = sg.Radio("Mammals", group_id="ques1")
option3 = sg.Radio("Reptile", group_id="ques1")
option4 = sg.Radio("Fish", group_id="ques1")

window = sg.Window('MCQ example', layout=[[label], [option1], [option2], [option3], [option4]])
window.read()
print("You successfully responded to the Question")
window.close()
