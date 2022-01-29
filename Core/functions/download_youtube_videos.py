import pytube  
from pytube import YouTube  
from text_to_speech import speak
import subprocess

def get_yt_link(query):
    import urllib.request
    import re
    search_keyword=query
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return "https://www.youtube.com/watch?v=" + video_ids[0]
def download(query):
    query = query.replace(" ", "+")
    video_url = get_yt_link(query)
    print(video_url)
    video = YouTube(video_url)
    video_streams = video.streams.filter(file_extension='mp4').get_by_itag(18)
    proc = subprocess.Popen('pwd', stdout=subprocess.PIPE)
    output = ((proc.stdout.read()).decode()).replace("\n", "")
    video_streams.download(output_path = output + "/Songs")


def check_functions(command):
    possible_strings = [
        "download the video",
        "download the youtube video",
        "download the you tube video",
        "download the video called",
        "download the song",
        "download the music video called",
        "download the music video",
        
        
    ]
    for guess in possible_strings:

        if guess in command:
            query = command.replace(guess, "")
            return query
        else:
            pass

    return False





