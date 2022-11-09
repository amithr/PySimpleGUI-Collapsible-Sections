import PySimpleGUI as sg


SYMBOL_RIGHT =    '▶'
SYMBOL_DOWN =  '▼'

def collapse(layout, key):

    # sg.pin allows us to diplay or hide the column
    return sg.pin(sg.Column(layout, key=key))

section_1 = [
    [sg.Input('Input 1')],
    [sg.Button('Button Section 1', button_color='yellow on green')]
]

section_2 = [
    [sg.Input('Input 2')],
    [sg.Button('Button Section 2', button_color='yellow on purple')]
]

layout = [
    [sg.Text(SYMBOL_DOWN, enable_events=True, key='-OPEN_SEC1-'),
    sg.Text('Section 1')],
    [collapse(section_1, '-SEC_1-')],

    [sg.Text(SYMBOL_DOWN, enable_events=True, key='-OPEN_SEC2-'),
    sg.Text('Section 2')],
    [collapse(section_2, '-SEC_2-')]   
]

window = sg.Window('Collapsible Sections', layout)

opened1 = True
opened2 = True

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-OPEN_SEC1-':
        opened1 = not opened1
        window['-OPEN_SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_RIGHT)
        window['-SEC_1-'].update(visible=opened1)
    
    if event == '-OPEN_SEC2-':
        opened2 = not opened2
        window['-OPEN_SEC2-'].update(SYMBOL_DOWN if opened1 else SYMBOL_RIGHT)
        window['-SEC_2-'].update(visible=opened2)
window.close()