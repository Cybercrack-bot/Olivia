from text_to_speech import speak
def open_apps(command):
    import os
    vscode_possible_strings = [
        "open vscode",
        "open visual studio code",
        "open visual studio",
        "i need to code in python",
        "i need to code",
        "i need to create a python script"
    ]
    mcreator_possible_strings = [
        "i need to code a minecraft mod",
        "i need to make a mod",
        "i want to code a minecraft mod",
        "i want to make a mod",
        "open m creator",
        "open mcreator"
        
    ]
    intelij_possible_strings = [
        "open intelij",
        "open my java ide",
        "open the java ide",
        "open java ide"
    ]
    google_chrome_strings = [
        "open google",
        "open google chrome",
        "open chrome",
        "i need to search something",
        "i need to open a website",
        "open a new tab",
        "i want to search something"

    ]
    minecraft_possible_strings = [
        "open minecraft",
        "open mine craft",
        "i want to play minecraft",
        "i want to play mine craft",
        "i need to play mine craft",
        "i need to play minecraft",
        "open minecraft launcher",
        "open mine craft launcher",
        "lets play mine craft",
        "lets play minecraft",
        "i want to play some minecraft",
        "i want to play some mine craft",
        "i need to play some mine craft",
        "i need to play some minecraft",
        "open the minecraft launcher",
        "open the mine craft launcher",
        "lets play some mine craft",
        "lets play some minecraft"
    ]
    zoom_possible_strings = [
        "open zoom",
        "i need you to open zoom",
        "i need to open zoom",
        "i want you to open zoom",
        "i want to open zoom",
        "i want to attend a meeting",
        "i need to attend a meeting"
    ]
    libre_office_possible_strings = [
        "open libre office",
        "open libreoffice",
        "open libre office writer",
        "open libreoffice writer",
        "open word",
        "i want to write my book",
        "i want to write a book",
        "i need to write a book"
    ]
    for vs in vscode_possible_strings:

        if vs in command:
            sys_command = "code"
            return [sys_command, "Opening visual studio code, happy coding sir"]

        else:
            pass
    for mc in mcreator_possible_strings:

        if mc in command:
            sys_command = "./home/cybercrack/Olivia/Core/software/mcreator.sh"
            return [sys_command, "Opening mcreator, i love mincraft"]
        else:
            pass

    for intel in intelij_possible_strings:

        if intel in command:
            sys_command = "./home/cybercrack/Olivia/Core/software/Intelij.sh"
            return [sys_command, "Opening intelij, java is cool"]
        else:
            pass
    for chrome in google_chrome_strings:

        if chrome in command:
            sys_command = "google-chrome"
            return [sys_command, "Opening google chrome, search something good"]
        else:
            pass
    for mclaunch in minecraft_possible_strings:
        if mclaunch in command:
            sys_command = "/home/cybercrack/Olivia/Core/software/minecraft-launcher"
            return [sys_command, "Opening minecraft, it is very educational"]
        else:
            pass
    for zoom in zoom_possible_strings:
        if zoom in command:
            sys_command = "zoom"
            return [sys_command, "Opening zoom, a good meeting is always a good plan"]
        else:
            pass
    for libre_office in libre_office_possible_strings:
        if libre_office in command:
            sys_command = "libreoffice"
            return [sys_command, "Opening libre office, continue your book sir"]
        else:
            pass
    return False



       