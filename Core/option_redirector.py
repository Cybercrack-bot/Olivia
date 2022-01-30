from Core.functions import open_gmail, weather
from text_to_speech import speak
import nltk  
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize
from Core.functions import open_web, download_youtube_videos
from Core.functions import suggest_music, search_web, open_discord, open_apps, search_youtube, switch_tabs
from Core.Datasets import bot_identity
import subprocess, sys, os
sys.path.append(os.system("pwd"))
def ProperNounExtractor(text : str):
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(words)
        for (word, tag) in tagged:
            if tag == "NN" or tag == "NNS" or tag == "VBZ":
                return word

def checkPersonalQuestions(text):
    nouns = ProperNounExtractor(text)
    for word in text.split():
        if nouns in word:
            index1 = ((text.split()).index(word)) - 1
            index2 = ((text.split()).index(word)) + 1
            if text.split()[index1] == "your" or text.split()[index1] == "you":
                return True
            elif text.split()[index2] == "your" or text.split()[index2] == "you":
                return True


def search_youtube_command(command):
    possible_strings = [
        "search youtube for",

    ]
    for guess in possible_strings:

        if guess in command:
            return command.replace(guess, "")
        else:
            pass

    return False
def open_discord_command(command):
    possible_strings = [
        "open discord",
        "open the application discord",
        "open the app discord",
        "i need to chat with my friends",
        "i want to chat with my friends"
    ]
    for guess in possible_strings:

        if guess in command:
            return True
        else:
            pass

    return False
def web_command(command):
    possible_strings = [
        "open the website",
        "go to the website",
        "vist the website",
        "visit this website called",
        "visit this website",
        "visit that website called",
        "open this website called",
        "open this website",
        "open that website called",
        "open",
        "the website",
        "go to"

    ]
    for guess in possible_strings:

        if guess in command:
            print(guess)
            website = command.replace(guess, "")
            return website
        else:
            pass

    return False


def suggest_music_command(command):
    possible_strings = [
        "what are the top trending songs",
        "what are the top trending songs right now",
        "suggest me some music",
        "suggest some music",
        "coolest songs",
        "what are the most trending songs right now",
        "what are the most trending songs today",
        "tell me the top trending songs",
        "what is the most trending song"

    ]
    for guess in possible_strings:

        if guess in command:
            return True
        else:
            pass

    return False


def search_google_command(command):
    possible_strings = [ 
        "search google for",
        "search"
    ]
    for guess in possible_strings:

        if guess in command:
            query = command.replace(guess, "")
            return query
        else:
            pass

    return False

def play_music_command(command):
    possible_strings = [
        "play the song",
        "i want to listen to the song",
        "search youtube for",
        "play",
        "play the music track",
        "play this music track"
    ]
    for guess in possible_strings:

        if guess in command:
            music = command.replace(guess, "")
            return music
        else:
            pass

    return False


def scan_for_guessing_function(command):
        command = cleanse_command(command)
        if checkPersonalQuestions(command):
            speak("I dont answer personal questions sir")
        elif open_gmail.guess_function(command):
            open_gmail.open_gmail_in_browser()
        elif download_youtube_videos.check_functions(command):
            query = download_youtube_videos.check_functions(command)
            speak("Downloading the video {}".format(query), save=False)
            download_youtube_videos.download(query)
            speak("Downloaded the music video {}".format(query), save=False)
            return
        elif open_discord_command(command):
            open_discord.open_discord()
            speak("Completed the task sir", save=False)
            return 
        elif search_youtube_command(command):
            query = search_youtube_command(command)
            search_youtube.search_youtube(query)
            speak("Completed the task sir", save=False)
            return
        elif web_command(command) != False:
            open_web.search_for_website(web_command(command))
            speak("Completed the task sir", save=False)
            return
        elif play_music_command(command) != False:
            suggest_music.play_music(play_music_command(command))
            speak("Completed the task sir", save=False)
            return
        elif suggest_music_command(command) != False:
            suggest_music.top_trending()
            speak("Completed the task sir", save=False)
            return
        elif switch_tabs.check_if_command_refers(command):
            switch_tabs.switch_window_tabs()
            speak("Completed the task sir", save=False)
            return
        elif search_google_command(command):
            search_web.search_google(search_google_command(command))
            speak("Completed the task sir", save=False)
            return
        elif weather.guess_command(command):
            speak(weather.guess_command(command))
            speak("Completed the task sir", save=False)
        else:
            if thank_you_and_other_appreciations(command):
                speak("You are very welcome sir")
            
    

def thank_you_and_other_appreciations(command):
        possible_appriciations = [
            "thank you olivia",
            "thank you honey",
            "thank you",
            "thank you very much",
            "thanks"
        ]
        for appreciation in possible_appriciations:
            if command == appreciation:
                return True

            else:
                continue
        return False


def cleanse_command(command):
    possible_unwanted_greets = [
        "hey olivia",
        "hey honey",
        "hello olivia",
        "hello honey",
        "olivia"
    ]
    cleansed = (command.lower()).strip()
    for greet in possible_unwanted_greets:
        if greet in cleansed:
            cleansed = cleansed.replace(greet, "")

    more = [
        "please",
        "just",
        "anyway"
    ]
    for word in more:
        if cleansed.startswith(word):
            cleansed = cleansed.replace(word, "")
            return cleansed 
    print(cleansed)
    return cleansed
