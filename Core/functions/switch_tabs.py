def switch_window_tabs():
    from text_to_speech import speak
    speak("switching", save=False)
    from pynput.keyboard import Key, Controller
    keyboard = Controller()
    keyboard.press(Key.alt_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.tab)


def check_if_command_refers(command):
    possible_strings = [
        "switch tabs",
        "switch to the nex tab",
        "switch to the previous tab",
        "i need you to switch tabs",
        "i need you to switch to the next tab",
        "i need you to switch to the previous tab",
        "i want you to switch tabs",
        "i want you to switch to the next tab",
        "i want you to switch to the previous tab"
    ]
    for guess in possible_strings:

        if guess in command:
            return True
        else:
            pass

    return False