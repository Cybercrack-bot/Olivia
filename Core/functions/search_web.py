def search_google(query):
    import webbrowser
    from googlesearch import search
    from text_to_speak import speak
    webbrowser.open("https://www.google.com/search?q={}".format(query))

    
