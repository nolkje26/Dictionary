import json
from difflib import get_close_matches
import re

data = json.load(open("data.json", "r"))

def define(word):
    word = word.lower() 
    if word in data:
        for definition in data[word]:
            print(definition)
    elif get_close_matches(word, data.keys()):
        userResponse = input("Did you mean {0}?".format(get_close_matches(word, data.keys())[0]))
        while not re.search(r'Y(e|eah|ah|a|ay|es)?$', userResponse, re.IGNORECASE) and not re.search(r'N(o|ope|ay|ah)?$', userResponse, re.IGNORECASE):
            userResponse = input("Did you mean {0}?".format(get_close_matches(word, data.keys())[0]))
        if re.search(r'Y(e|eah|ah|a|ay|es)?$', userResponse, re.IGNORECASE):
            return define(get_close_matches(word, data.keys())[0])  
        elif re.search(r'N(o|ope|ay|ah)?$', userResponse, re.IGNORECASE):
            print("Could not find a match. Please recheck the spelling of the word.")
    else:
        print("Could not find a match. Please recheck the spelling of the word.")

word = input("Enter word: ")

define(word)
