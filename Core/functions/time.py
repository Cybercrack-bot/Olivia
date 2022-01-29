from datetime import datetime
from text_to_speech import speak

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
speak(current_time, save=False)
