import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("Press Y for yes or N for no: ")
        if decide == "y" or "Y":
            return data[get_close_matches(word , data.keys())[0]]
            if decide == "n" or "N":
                return("Sorry the word dont exist in data. ")
        else:
             return("You have entered wrong input please enter just y or n. ")
    else:
        print("Please check the word again. ")



word = input("Enter the word you want to search: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)