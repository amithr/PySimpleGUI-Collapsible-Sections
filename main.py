import PySimpleGUI as sg


SYMBOL_UP =    '▶'
SYMBOL_DOWN =  '▼'


def collapse(layout, key):
    # Pin is an element that can be hidden and revealed
    return sg.pin(sg.Column(layout, key=key))


section1 = [[sg.Input('Input 1', key='-IN1-')],
            [sg.Button('Button Section 1',  button_color='yellow on green')]]

section2 = [[sg.Input('Input 2')],
            [sg.Button('Button Section 2', button_color=('yellow on purple'))]]


layout =   [
            [sg.Text(SYMBOL_DOWN, enable_events=True, key='-OPEN_SEC1-'), 
             sg.Text('Section 1', enable_events=True)],
             # Adds a column to the layout
            [collapse(section1, '-SEC1-')],

            [sg.Text(SYMBOL_DOWN, enable_events=True, key='-OPEN_SEC2-'),
             sg.Text('Section 2')],
             # Adds a column to the layout
            [collapse(section2, '-SEC2-')]]

window = sg.Window('Collapsible Sections', layout)

opened1, opened2 = True, True

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == '-OPEN_SEC1-':
        opened1 = not opened1
        window['-OPEN_SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
        window['-SEC1-'].update(visible=opened1)

    if event == '-OPEN_SEC2-':
        opened2 = not opened2
        window['-OPEN_SEC2-'].update(SYMBOL_DOWN if opened2 else SYMBOL_UP)
        window['-SEC2-'].update(visible=opened2)

window.close()
