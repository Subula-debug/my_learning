import pyttsx3
import PySimpleGUI as sg

# Create the GUI layout
layout = [
    [sg.Text("Enter the text you want to convert to speech:")],
    [sg.InputText()],
    [sg.Text("Select a voice:")],
    [sg.Radio("Male", "voice", default=True, key="-MALE-"),
     sg.Radio("Female", "voice", key="-FEMALE-")],
    [sg.Button("Speak"), sg.Button("Exit")]
]

# Create the window
window = sg.Window("Text-to-Speech App", layout)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Start the main event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    if event == "Speak":
        text = values[0]
        if values["-MALE-"]:
            engine.setProperty("voice", "english+m3")
        elif values["-FEMALE-"]:
            engine.setProperty("voice", "english+f3")
        engine.say(text)
        engine.runAndWait()

# Clean up the text-to-speech engine
engine.stop()
engine.shutdown()

# Close the window
window.close()
