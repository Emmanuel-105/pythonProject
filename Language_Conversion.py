# TO JUNGLE LANGUAGE

def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter in "Aa":
            translation = translation + "1"
        elif letter in "Ee":
            translation = translation + "2"
        elif letter in "Ii":
            translation = translation + "3"
        elif letter in "Oo":
            translation = translation + "4"
        elif letter in "Uu":
            translation = translation + "5"
        elif letter in " ":
            translation = translation + " "
        else:
            translation = translation + letter + "a"
    return translation


# TO ENGLISH

def convert_back(phrase):

    conversion = ""
    for letter in phrase:
        if letter == "1":
            conversion = conversion + "a"
        elif letter == "2":
            conversion = conversion + "e"
        elif letter == "3":
            conversion = conversion + "i"
        elif letter == "4":
            conversion = conversion + "o"
        elif letter == "5":
            conversion = conversion + "u"
        elif letter == " ":
            conversion = conversion + " "
        elif letter == "a":
            conversion = conversion + ""
        else:
            conversion = conversion + letter

    return conversion

# Testing
# print(translate("my name is emmanuel"))

print(convert_back("maya na1ma2 3sa 2mama1na52la"))



