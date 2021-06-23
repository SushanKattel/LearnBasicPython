

the_file = open("filecontent.txt", "r")
print(the_file.readable())
print(the_file.writable())
#print(the_file.read())
#print(the_file.readlines())
#print(the_file.readlines()[4])
#print(the_file.readline())
for jpt in the_file.readlines():
    print(jpt)
#   It prints every line of file separately.
the_file.close()