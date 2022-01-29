# Olivia
A cool virtual assistant for windows that can automate your daily tasks. note: not a chatbot

# Installation

Let's install Olivia.

Go to the installation directory and run the below command


```bash
python3 setup.py
```

## Usage

```bash
python3 Olivia.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

# Tasks that Olivia can do

~~~
Open Gmail
download YouTube videos
open discord
search youtube
open website
play music
suggest music
switch tabs
tell weather report
~~~

No standard commands are needed, talk to her like you talk to other people but limit the word count.

# Modding Olivia

You can add your own features to her if you know basic python and json. Here's how you can easily mod Olivia. 
 ```
1. First go to the folder Olivia
2. You can see a folder called Mods and inside of it,
   a file called config.json which is empty
3. Create a folder and name it anything you like
4. Inside of it create a python script also named anything you like
5. Open it with an IDE and copy this piece of code into it
```

```python
# Note that this Core module isn't a module that is needed to be
# installed with pip
import Core

def Main(command : str, text_to_speech):
    # The code you want to be run every time you give a voice command
 ```
```
6. Modify the code all you want but without changing the above template.
7. The "Main" function is the one that is run in a loop everytime you 
   give a voice command.
8. The "command" parameter is supplied when a voice command is given 
   to Olivia. So you can use a simple "if" statement to check if that
   is equal to your desired string.
9. The "text_to_speech" parameter is used to convert 
   your desired string to an Olivia response
10. After you modify the code all you want, open that config.json 
    you saw earlier
11. It should be empty, the first time you use it. Then, copy- 
    paste the below code
```
```json
"module| any module name":{
        "name": "Name of your module",
        "script_location": "the script location of where you put your Main function"
        "Example modulefolder/yourscript.py"


    }
```
```
12. After you modify the above code as in the instructions,
    put it inside the config.json
13. If you want to add another mod, repeat the above steps and 
    add any amount of the above entries.
14. Note that in the first json parameter, "module| any module name" is given,
    the part "module| " is necessary but change the "any module name" to your module name.
    And yes the space after "module|" is necessary too.
15. After you have done this, go ahead and start Olivia!


