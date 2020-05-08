import json
from  difflib import get_close_matches


data = json.load(open("data.json"))

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys()))>0:
        print("Did you mean %s instead of"%get_close_matches(word, data.keys())[0])
        deci = input("Press Y for yes and N for no: ")
        if deci == "Y"or"y":
            return [get_close_matches(word, data.keys())]
        if deci == "N"or"n":
            print("LULL")
        else:
            print("Enter either Y or N.")

    else:
        print("No such word found in given data...")

word = input("Enter the word you want to search: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
