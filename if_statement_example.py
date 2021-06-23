print("This is example of boolean if i.e, True or False")
is_male = True

if is_male:
    print("You are a male!!")

print("_________________________________________________________")

is_female = False
if is_female:
    print("You are a Female!!")
else:
    print("You are a male!!")
print("_________________________________________________________")

is_male = True
is_tall = True

if is_male or is_tall:
    print("You are male or tall or both !")
else:
    print("You are neither Male nor Tall !")

print("_________________________________________________________")

is_male1 = True
is_tall1 = False

if is_male1 and is_tall1:
    print("You are a tall male !")

elif is_male1 and not (is_tall1):
    print("You are a short male!!")

elif not(is_male1) and is_tall1:
    print("You are a not a male but is tall !!")

else:
    print("You are not a male and not tall !")

print("Try printing by changing is_male1 and is_tall1 True or False :p ")