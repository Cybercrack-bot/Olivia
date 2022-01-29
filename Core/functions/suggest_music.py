from text_to_speech import speak
import webbrowser
def top_trending():
    speak("I will fetch to top trending songs for you sir")
    webbrowser.open("https://www.google.com/search?q=top+trending+songs&oq=top+trending+&aqs=chrome.1.69i57j0i512l9.4428j0j4&sourceid=chrome&ie=UTF-8")


def play_music(title):
    try:
        speak("I will play the song {} now, enjoy".format(title))
        print(title)
        webbrowser.open("https://open.spotify.com/search/" + title)
    except IndexError:
        speak("Sorry, i cannot play it, please try again")

