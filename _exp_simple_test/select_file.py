from turtle import color
import PySimpleGUI as sg
from numpy import pad

sg.theme('Light Blue 2')

layout = [[sg.Text('选择图片')],
          [sg.Button('OK'), sg.Button('Cancel')],
          [sg.Text('File 1', size=(5, 1)), sg.Input(size=(40, 1)), sg.FileBrowse(key='-File1-')],
          [sg.Text('File 2', size=(5, 1)), sg.Input(size=(40, 1)), sg.FileBrowse(key='-File2-')],
          [sg.Text('File 3', size=(5, 1)), sg.Input(size=(40, 1)), sg.FileBrowse(key='-File3-')]
        ]

window = sg.Window('File Compare', layout)

event, values = window.read()

while True:
    event, values = window.read()
    print(f'Event: {event}')
    
    if event == 'OK':
        fileNames = []
        if len(values[0]) > 0:
            fileNames.append(values[0])
        if len(values[1]) > 0:
            fileNames.append(values[1])
        if len(values[2]) > 0:
            fileNames.append(values[2])
        print('select file: ', fileNames)
    elif event in (None, 'Cancel'):
        # User closed the Window or hit the Cancel button
        break
    print(str(values))
    
window.close()
print(f'You clicked {event}')
