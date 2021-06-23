i = 1
while i <= 3:
    print(i)
    i = i+1
print("----------------------<<<<<>>>>>-----------------------")

guess_try = 0
guess_limit = 5
guess_offer = False
the_word = "horse"
guess = ""
while guess != the_word and not(guess_offer):
    if guess_try < guess_limit:
        if guess_try >= 1:
            print("PLEASE TRY AGAIN")
        if guess_try == 4:
            print("It's your LAST CHANCE !! BE CAREFUL !!!" )
        guess = input("Enter your guess word: ")
        guess_try = guess_try + 1
    else:
        guess_offer = True

if guess_offer:
    print("Sorry!! you had just 5 chances and you lose. Please restart the game again..! ")
else:
    print("Congo!! You Won!!!")

