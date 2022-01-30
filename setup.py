import os
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
prGreen("Starting setup!\n")
modules = [
    "subprocess.run",
    "windowsapps",
    "pytube",
    "text_to_speech",
    "SpeechRecognition",
    "google",
    "youtube-search-python"
    "pynput",
    "beautifulsoup4",
    "requests",
    "pyttsx3",
    "nltk"

]
for module in modules:
    prGreen("Installing module %s" % module)
    os.system(f"pip install {module}")

import text_to_speech
import nltk
prGreen("Installing nltk datasets")
nltk.download("all")
text_to_speech.speak("Done installing myself, starting Olivia, you can quit this by pressing control c", save=False)
os.system("python3 Olivia.py")
