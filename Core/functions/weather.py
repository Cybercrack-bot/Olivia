import requests
from bs4 import BeautifulSoup
 
def get_weather_data():
    
    # creating url and requests instance
    url = "https://www.google.com/search?q="+"weather"
    html = requests.get(url).content
    
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    
    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    
    # getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
    
    # getting other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]
    return "The temperature is {} and the sky description is {}".format(temp, sky)


def guess_command(command):
    possible_strings = [
        "what is the weather",
        "say the weather",
        "tell me the weather",
        "what is the weather today",
        "whats the weather today",
        "what's the weather today"
    ]
    for guess in possible_strings:

        if guess in command:
            return get_weather_data()
        else:
            pass

    return False