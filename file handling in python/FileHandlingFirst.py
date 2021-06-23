
import os

#  f=open("FirstFile.txt","x")  #Creates a new file if it doesn't exist. Returns eror if file pre Exists.

jpt1file=open("FirstFile.txt", "r")
print(jpt1file.read(15))  # It prints upto first 15 character of the file.
jpt1file.close()
print("-----------------a-------------------------- ")
jptfile=open("FirstFile.txt", "r")
print (jptfile.read())
jptfile.close()
print("-----------------b-------------------------- ")
file=open("FirstFile.txt", "r")
print (file.readline())
file.close()
print("------------------c------------------------- ")
files = open("FirstFile.txt", "r")
print(files.readlines())
files.close()
print("------------------d------------------------- ")
filee=open("FirstFile.txt", "r")
print (filee.readlines(1))
filee.close()
print("-----------hahaha-------------------------------- ")

loopfile=open("FirstFile.txt", "r")
for line in loopfile:
    print (loopfile.read())
loopfile.close()
print("------------------end read mode------------------------- ")

# wfile=open("FirstFile.txt", "a")

if os.path.exists("SecondFile.txt"):
    f = open("SecondFile.txt", "w")
else:
    f = open("SecondFile.txt","x")

f.close()


if os.path.exists("FirstFile.txt"):
    print("The File Already Exists ")
else:
    f = open("FirstFile.txt","x")

print("This is the way we should be using file for our program")
print("------------------End the Phase------------------------- ")

sfile = open("SecondFile.txt", "w")
sfile.write("I have written this from Pycharm")
sfile.close()

# os.remove("filename.txt") deletes the file.   os.rmdir("Myfolder") deletes the folder



sfile = open("SecondFile.txt", "w")
sfile.write(" Write overridden")
sfile.close()

sfile = open("SecondFile.txt", "a")
sfile.write("\n I have written this from Pycharm after Opening in append mode!! ")
sfile.close()



