def open_discord():
    import webbrowser
    from text_to_speak import speak
    speak("Opening discord", save=False)
    webbrowser.open("https://discord.com/channels/@me")