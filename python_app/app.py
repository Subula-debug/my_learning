import PySimpleGUI as sg
import pyttsx3

# Define the GUI layout
layout = [[sg.Text('Enter some text:')],
          [sg.Input(key='-INPUT-')],
          [sg.Text('Select a voice:')],
          [sg.Radio('Male', 'voice', key='-MALE-'), sg.Radio('Female', 'voice', key='-FEMALE-', default=True)],
          [sg.Button('Speak'), sg.Button('Exit')]]

# Create the GUI window
window = sg.Window('Text to Speech App', layout)

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Main event loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Speak':
        # Set the voice based on user input
        if values['-MALE-']:
            engine.setProperty('voice', 'english+m3')
        else:
            engine.setProperty('voice', 'english+f3')
        # Speak the text
        engine.say(values['-INPUT-'])
        engine.runAndWait()

# Stop the pyttsx3 engine
engine.stop()

# Close the GUI window
window.close()
