def search_for_website(query):
    from googlesearch import search
    from text_to_speech import speak
    import webbrowser
    
    # to search
    speak("Opening {}, give me a second".format(query), save=False)
    result = list(search(query, tld="co.in", num=10, stop=10, pause=2))[0]
    webbrowser.open(result)
    
        
