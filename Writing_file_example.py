

x = input("Enter the name to add: ")
y = input("Enter post of "+ x + ": ")
print("Do you want to add "+x+" as a "+y+" in the list of file. ")
z = input("Press \"y\" for YES and \"n\" for NO: ")

if z=="y":
    the_file = open("filecontent.txt", "a")
    #  If we use w here in place of a, it will erse all from prev. file and write new file.
    #  We can create a new file using w like, the_file = open("filecontent1.txt", "w").
    #  We can write any extension file, like html or any.
    #  print(the_file.readable())
    #  print(the_file.writable())

    the_file.write(x+" - "+y+"\n")


    the_file.close()
else:
    print("Please start again!")

