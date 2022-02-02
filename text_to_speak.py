from gtts import gTTS  
import os
from playsound import playsound  

def speak(text_val : str, save):
    language = 'en'    
    obj = gTTS(text=text_val, lang=language, slow=False)  
    obj.save("speak.mp3")  
    playsound("speak.mp3")  
    os.remove("speak.mp3")