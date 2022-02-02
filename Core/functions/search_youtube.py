def search_youtube(query):
    import webbrowser
    from text_to_speech import speak
    speak("Searching Youtube for {}, please give me a second".format(query))
    webbrowser.open("https://www.youtube.com/results?search_query=" + query.replace(" ", "+"), save=False)