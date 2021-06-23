def encrypter(string):
    encrypted = ""
    for all in string:
        if all.lower() in "a":
            if all.isupper():
                encrypted = encrypted + ";"
            else:
                encrypted = encrypted + "\""
        elif all.lower() in "b":
            if all.isupper():
                encrypted = encrypted + "l"
            else:
                encrypted = encrypted + "Z"
        elif all.lower() in "c":
            if all.isupper():
                encrypted = encrypted + "?"
            else:
                encrypted = encrypted + "^"
        elif all.lower() in "d":
            if all.isupper():
                encrypted = encrypted + "."
            else:
                encrypted = encrypted + ","
        elif all.lower() in "e":
            if all.isupper():
                encrypted = encrypted + ">"
            else:
                encrypted = encrypted + "<"
        elif all.lower() in "f":
            if all.isupper():
                encrypted = encrypted + ";"
            else:
                encrypted = encrypted + ":"
        elif all.lower() in "g":
            if all.isupper():
                encrypted = encrypted + "-"
            else:
                encrypted = encrypted + "_"
        elif all.lower() in "h":
            if all.isupper():
                encrypted = encrypted + "x"
            else:
                encrypted = encrypted + "+"
        elif all.lower() in "i":
            if all.isupper():
                encrypted = encrypted + "["
            else:
                encrypted = encrypted + "{"
        elif all.lower() in "j":
            if all.isupper():
                encrypted = encrypted + "}"
            else:
                encrypted = encrypted + "]"
        elif all.lower() in "k":
            if all.isupper():
                encrypted = encrypted + "%"
            else:
                encrypted = encrypted + "("
        elif all.lower() in "l":
            if all.isupper():
                encrypted = encrypted + ")"
            else:
                encrypted = encrypted + "B"
        elif all.lower() in "m":
            if all.isupper():
                encrypted = encrypted + "1"
            else:
                encrypted = encrypted + "!"
        elif all.lower() in "n":
            if all.isupper():
                encrypted = encrypted + "0"
            else:
                encrypted = encrypted + "6"
        elif all.lower() in "o":
            if all.isupper():
                encrypted = encrypted + "&"
            else:
                encrypted = encrypted + "2"
        elif all.lower() in "p":
            if all.isupper():
                encrypted = encrypted + "7"
            else:
                encrypted = encrypted + "@"
        elif all.lower() in "q":
            if all.isupper():
                encrypted = encrypted + "4"
            else:
                encrypted = encrypted + "~"
        elif all.lower() in "r":
            if all.isupper():
                encrypted = encrypted + "`"
            else:
                encrypted = encrypted + "3"
        elif all.lower() in "s":
            if all.isupper():
                encrypted = encrypted + "|"
            else:
                encrypted = encrypted + "\\"
        elif all.lower() in "t":
            if all.isupper():
                encrypted = encrypted + "/"
            else:
                encrypted = encrypted + "8"
        elif all.lower() in "u":
            if all.isupper():
                encrypted = encrypted + "'"
            else:
                encrypted = encrypted + "*"
        elif all.lower() in "v":
            if all.isupper():
                encrypted = encrypted + "$"
            else:
                encrypted = encrypted + "Y"
        elif all.lower() in "w":
            if all.isupper():
                encrypted = encrypted + "5"
            else:
                encrypted = encrypted + "#"
        elif all.lower() in "x":
            if all.isupper():
                encrypted = encrypted + "z"
            else:
                encrypted = encrypted + "="
        elif all.lower() in "y":
            if all.isupper():
                encrypted = encrypted + "v"
            else:
                encrypted = encrypted + "9"
        elif all.lower() in "z":
            if all.isupper():
                encrypted = encrypted + "b"
            else:
                encrypted = encrypted + "X"
#  letters are encripted here for first time.

        elif all in "1":
            encrypted = encrypted + "M"
        elif all in "2":
            encrypted = encrypted + "o"
        elif all in "3":
            encrypted = encrypted + "r"
        elif all in "4":
            encrypted = encrypted + "Q"
        elif all in "5":
            encrypted = encrypted + "W"
        elif all in "6":
            encrypted = encrypted + "n"
        elif all in "7":
            encrypted = encrypted + "P"
        elif all in "8":
            encrypted = encrypted + "t"
        elif all in "9":
            encrypted = encrypted + "y"
        elif all in "0":
            encrypted = encrypted + "N"

        else:
            encrypted = encrypted + all

#  numbers are encrypted here for first time

    #elif all in "":
    #encrypted = encrypted + "M"

    return encrypted

print(encrypter(input("Enter a phrase to translate: ")))