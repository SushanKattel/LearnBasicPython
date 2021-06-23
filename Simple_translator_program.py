def translate(string):
    translated = ""   #  This is declaring empty variable.
    for everyletter in string:      #  You can write anything in place of everyletter!!
        if everyletter.lower() in "aeiou\"":
            if everyletter.isupper():
                translated = translated + "G"
            else:
                translated = translated + "g"
        else:
            translated = translated + everyletter
    return translated

print(translate(input("Enter a phrase to translate: ")))





