
# Just OverView to OS module, Basically for files, Not a complete os module example.

import os
from datetime import datetime
#print(os.getcwd()) #  Gives current directory.

x=os.getcwd()
print(x)

os.chdir("E:\program projects\Python projects\ ")  # Changes current directory.
print(os.getcwd())

os.chdir("E:\program projects\Python projects\Project 1 ")
print(os.getcwd())

print(os.listdir())   # Lists the files and folders present in current directory.

os.mkdir('NewDir')   # Creates new directory; but not directory inside directory.
os.makedirs("NewDir2/sub-dir1") # Creates directory with subdirectory.
  # If dir is already created, they gives an error!!
print(os.listdir())

os.rmdir('NewDir')    # Remove directories. These two are in same kinds as above.
os.removedirs("NewDir2/sub-dir1")

print(os.listdir())

print("____________________________________________________________________")

os.rename("ToRename.txt", "Renamed.txt")
print(os.listdir())
os.rename("Renamed.txt", "ToRename.txt")
print(os.listdir())
print("____________________________________________________________________")

print(os.stat("ToRename.txt"))   # prints info about file. See documentation for their meanings.
print(os.stat("ToRename.txt").st_size) # Gives size of document
print(os.stat("ToRename.txt").st_mtime) # Gives modification timestamp. To make it readable, we import dattime and print as:

ReadableModTime = os.stat("ToRename.txt").st_mtime
print(datetime.fromtimestamp(ReadableModTime))  # Now, the date and time printed is readable.

print("____________________________________________________________________")

for dirpath, dirnames, filenames in os.walk(os.getcwd()):   # os.walk() gives all directories and files present there:
    print("Current Path: ", dirpath)
    print("Directories: ", dirnames)
    print("Files: ", filenames)
    print()
print("____________________________________________________________________")

print(os.environ)
print(os.environ.get("COMPUTERNAME")) # os.environ gives all environment variables.I am doing this only for COMPUTERNAME.
# To create a directory inside any environment variable, we do following:

file_path_jpt = os.path.join(os.environ.get("ALLUSERSPROFILE"),"Test.txt")
print(file_path_jpt)   # Look for how to write file there !
print("____________________________________________________________________")

print(os.path.basename("/tmp/test.txt")) # It gives name of file, though directory and file doesn't exists
print(os.path.dirname("/tmp/test.txt"))  # Gives name of directory
print(os.path.split("/tmp/test.txt"))  # Splits name of file and directory
print(os.path.exists("/tmp/test.txt"))  # Check weather it exists or not !!
print(os.path.isdir("/tmp/test"))   # if file doesn't have extension, to check it is directory or file, isdir; isfile.
                                    # Here, sine it doesnt exists, both are false.
print(os.path.splitext("/tmp/test.txt")) # It splits the root and extension of file.
print("____________________________________________________________________")