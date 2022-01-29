import json
import importlib


def initialize_mods():
    mods = open("Mods/config.json")
    mods_json = json.load(mods)
    mod_classes = []
    modules = []
    for mod in mods_json:
        if "module| " in mod:
            mod_classes.append(str(mod))
    for mod_class in mod_classes:
        details = mods_json[mod_class]
        name = details['name']
        location = "Mods." + (str(details["script_location"]).replace("/", ".")).replace(".py", "")
        module = importlib.import_module(location)
        if "Main" in dir(module):
            modules.append(module)
        else:
            raise NameError
    return modules
    
        


