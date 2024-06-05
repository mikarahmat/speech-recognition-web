# libraries used
import os
import soundfile as sf
import speech_recognition as sr
import webbrowser
import json
import pyttsx3
import numpy as np
from language_tool_python import LanguageTool
from flask import Flask, render_template, request

# declare flask variable for html access
app = Flask(__name__)

# declare the speech recognizer & grammar checker tools
r = sr.Recognizer()
r.pause_threshold = 1
language_tool = LanguageTool('en-US')

# File path to store the commands
storage_file = 'stored_commands.json'

# Load stored commands from the file if it exists
try:
    with open(storage_file, 'r') as f:
        stored_commands = json.load(f)
except FileNotFoundError:
    stored_commands = {}

# Function to save stored commands to the file
def save_commands_to_file():
    with open(storage_file, 'w') as f:
        json.dump(stored_commands, f)

# function for text-to-speech
def SpeakText(command, rate=200):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(command)
    engine.runAndWait()

# function for accessing microphone
def get_voice():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    return audio

# access microphone & save the result
def get_voice_save_sound():
    audio = get_voice()

    sound_folder = 'sound'
    if not os.path.exists(sound_folder):
        os.makedirs(sound_folder)
    audio_data = np.frombuffer(audio.get_raw_data(), dtype=np.int16)
    sf.write(os.path.join(sound_folder, 'input.wav'), audio_data, audio.sample_rate)

    return audio

# function for grammar checker
def grammar_check(text):
    matches = language_tool.check(text)
    return matches

# function for speech-to-text
def convert_audio_to_text(audio):
    text = ""
    try:
        text = r.recognize_google(audio, language='en')
        print(f"Result: {text}")
        SpeakText(text)

    except sr.UnknownValueError:
        print("Unrecognized")
    except sr.RequestError as e:
        print(f"Error; {e}")
    return text

# speech-to-text with grammar checker & save text
def convert_audio_to_text_save_grammar(audio):
    text = ""
    try:
        text = r.recognize_google(audio, language='en')
        print(f"Result: {text}")
        SpeakText(text, rate=125)

        # Grammar check
        matches = grammar_check(text)
        if matches:
            print("Grammar issues:")
            for match in matches:
                print(match)

        # Save text to file in text folder
        text_folder = 'text'
        if not os.path.exists(text_folder):
            os.makedirs(text_folder)
        with open(os.path.join(text_folder, 'output.txt'), 'w') as f:
            f.write(text)

    except sr.UnknownValueError:
        print("Unrecognized")
    except sr.RequestError as e:
        print(f"Error; {e}")
    return text

# v routing to the html v

# home route
@app.route('/')
def index():
    return render_template('index2.html')

# speech-to-text route
@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    audio = get_voice_save_sound()
    text = convert_audio_to_text_save_grammar(audio)
    return text

# text-to-speech route
@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text1 = request.form['area']
    SpeakText(text1)
    return text1

# store-command to store the commands and save it
@app.route('/store-command', methods=['POST'])
def store_command():
    link = request.form['link']
    command = request.form['command']
    stored_commands[command.lower()] = link
    save_commands_to_file()
    return "Command stored successfully."

# open-task route
@app.route('/open-task', methods=['POST'])
def open_tabs():
    audio = get_voice()
    text = convert_audio_to_text(audio)
    
    # detect keywords
    relevant_command = None
    for command_key in stored_commands:
        if command_key in text.lower():
            relevant_command = command_key
            break
    
    if relevant_command is not None:
        webbrowser.open(stored_commands[relevant_command])
        return f"Website Opened"
    else:
        return "Command not found."

if __name__ == '__main__':
    app.run(debug=True, port=8000)