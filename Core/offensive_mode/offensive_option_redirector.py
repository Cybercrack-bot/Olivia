from Core.offensive_mode import backdoor_generation
from text_to_speech import speak
import speech_recognition as sr
r = sr.Recognizer()
def listen(duration):
    with sr.Microphone() as source:
        try:
            # read the audio data from the default microphone
            audio_data = r.record(source, duration=duration)
            print("Recognizing...")
            # convert speech to text
            text = r.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return 


def guess_functions(command):
    if backdoor_generation.scan_to_find_out(command):
        backdoor_generation.supply_input()
        speak("Completed the task sir")
        