def open_gmail_in_browser():
    import webbrowser
    from text_to_speech import speak
    speak("Opening your inbox")
    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    return


def guess_function(command):
    possible_strings = [
        "open gmail",
        "open email",
        "check my inbox",
        "open my email",
        "open my gmail",
        "open my inbox"
    ]
    for guess in possible_strings:

        if guess in command:
            return True
        else:
            pass

    return False