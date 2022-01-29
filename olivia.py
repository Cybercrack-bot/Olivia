import speech_recognition as sr
from Core import option_redirector
import datetime
import pyttsx3, json
import initializeMods
import sys, subprocess
from text_to_speech import speak
from Core import option_redirector
from Core.offensive_mode import offensive_option_redirector
r = sr.Recognizer()
proc = subprocess.Popen('pwd', stdout=subprocess.PIPE)
output = proc.stdout.read()
sys.path.append(output)



def load_mods(command : str, modules_list : list):
    results = []
    for module in modules_list:
        result = module.Main(command, speak)
        results.append(result)
    return results

    
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


def speak_str(audio):
    speak(audio, save=False)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 
  
    speak("Olivia at your service, lets begin")
    

def greet(module_list):
    wishMe()
    while True:
            command = listen(7)

            print(command)
            if command is None:
                print("Nope")
            elif command == "quit":
                speak("Closing myself, have a good day sir")
                quit()
            
            else:
                if command.lower() == "hibernate":
                    speak('okay sir, awaiting the command to wake me up')
                    while True:
                        wake_up = listen(6)
                        print(wake_up)
                        if wake_up is None:
                            continue
                        else:
                            wake_up = wake_up.lower()
                            if wake_up == "wake up now":
                                speak("That was a good rest sir, lets begin")
                                break
                            elif "olivia" in wake_up:
                                speak("I heard you call my name. lets continue sir")
                                break
                            elif wake_up == "quit":
                                speak("Closing myself, have a good day sir")
                                quit()
                else:
                    if module_list[0] == "No mods":
                        commands(command, "passive")
                    else:
                        results = load_mods(command, module_list)
                        if True not in results:
                            commands(command, "passive")

            
    



def commands(command, mode):
    if mode == "passive":
        option_redirector.scan_for_guessing_function(command)
    else:
        offensive_option_redirector

try:
    module_list = initializeMods.initialize_mods()
except NameError:
    speak("The mod functions are not correct")
    quit()
except ImportError:
    speak("Problem importing mods, re-ensure all the paths are correct in config.jason")
    quit()
except json.JSONDecodeError:
    module_list = ["No mods"]

greet(module_list)