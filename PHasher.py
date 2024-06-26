import PySimpleGUI as sg
import hashlib

# All the stuff inside your window.
layout = [  [sg.Text('Input your password'), sg.InputText()],
            [sg.Text('Input your key'), sg.InputText()],
            [sg.Text('Hash: '), sg.Text('', key = "asd")],
            [sg.Button('Ok'), sg.Button('Cancel')]
             ]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    password = values[0]
    salt = values[1]
    dataBase_password = password + salt
    hashed = hashlib.md5(dataBase_password.encode())
    print(hashed.hexdigest())
    contraseña = hashed.hexdigest()
    window['asd'].update(contraseña)

window.close()