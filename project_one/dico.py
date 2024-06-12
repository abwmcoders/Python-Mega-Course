import json
from difflib import get_close_matches

data = json.load(open("./project_one/data.json"))

def dictionary(word):
    if word in data:
        definition = data[word]
        return definition
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        prediction = get_close_matches(word, data.keys())[0]
        yn = input("Did you mean %s instead? Please enter Y for yes or N for no: " % prediction)
        if yn.upper() == "Y":
            return data[prediction]
        elif yn.upper() == "N":
            return "Word does not exists"
        else:
            return "We don't understand your entry, Good bye"
    else:
        return "Word not found, Please double check your input!"


word = input("Please enter a word: ")
output = dictionary(word.lower())

if type(output) == str:
    print(output)
else:
    for definition in output:
        print(definition)
