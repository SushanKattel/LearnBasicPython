from tkinter import *



import os, string



def delete1():
    screen.destroy()



def newDirInfo():

    diskInfo = disk.get().upper()
    mainFolderInfo = mainFolder.get()
    savingFolderInfo = savingFolder.get()

    disk_entry1.delete(0, END)
    mainFolder_entry1.delete(0, END)
    savingFolder_entry1.delete(0, END)

    available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    if diskInfo+":" in available_drives:


        savingPath = diskInfo + ":/" + mainFolderInfo + "/" + savingFolderInfo

        os.chdir(diskInfo + ":/")
        diskcheck = (os.listdir())
        if mainFolderInfo in diskcheck:
            os.chdir(diskInfo + ":/" + mainFolderInfo + "/")
            listcheck = (os.listdir())
            if savingFolderInfo in listcheck:
                Label(screen2, text="Directory already exists !", fg="red").pack()


            else:

                os.makedirs(savingPath)





        else:
            os.makedirs(savingPath)

            os.chdir(diskInfo + ":/" + mainFolderInfo + "/" + savingFolderInfo)

            Label(screen2, text="Task completed Sucessfully!!", fg="red").pack()
            createFile()
    else:

        Label(screen2, text="Please enter valid drive address !", fg="red").pack()
def newDir():

    global screen2
    screen2 = Toplevel(screen)
    screen2.title("New Directory")
    screen2.geometry("350x300")

    Label(screen2, text="Please enter details below").pack()
    Label(screen2, text="").pack()


    global disk
    global mainFolder
    global savingFolder

    disk = StringVar()
    mainFolder = StringVar()
    savingFolder = StringVar()

    global disk_entry1
    global mainFolder_entry1
    global savingFolder_entry1

    Label(screen2, text="Disk to create Directory: ").pack()
    disk_entry1 = Entry(screen2, textvariable=disk)
    disk_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Input the name of master folder!").pack()
    mainFolder_entry1 = Entry(screen2, textvariable=mainFolder)
    mainFolder_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Input the name of folder to save! ").pack()
    savingFolder_entry1 = Entry(screen2, textvariable=savingFolder)
    savingFolder_entry1.pack()
    Label(screen2, text="").pack()


    Button(screen2, text="Create directory", width=15, height=1, command=newDirInfo).pack()





def createFile():
    print(os.getcwd())



def loadDirInfo():
    loadDiskInfo = loadDisk.get().upper()
    loadMainFolderInfo = loadMainFolder.get()
    loadSavingFolderInfo = loadSavingFolder.get()

    load_disk_entry1.delete(0, END)
    load_mainFolder_entry1.delete(0, END)
    load_savingFolder_entry1.delete(0, END)

    available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]

    if loadDiskInfo + ":" in available_drives:
        os.chdir(loadDiskInfo + ":/")
        loadDiskcheck = (os.listdir())
        if loadMainFolderInfo in loadDiskcheck:
            os.chdir(loadDiskInfo + ":/" + loadMainFolderInfo + "/")
            listcheck = (os.listdir())
            if loadSavingFolderInfo in listcheck:
                os.chdir(loadDiskInfo + ":/" + loadMainFolderInfo + "/" + loadSavingFolderInfo)

                Label(screen3, text="Task completed sucessfully.", fg="red").pack()

                createFile()


            else:

                Label(screen3, text="Create the directory first !", fg="red").pack()

        else:
            Label(screen3, text="The Master Folder doesn't Exists!", fg="red").pack()


    else:
        Label(screen3, text="Please enter valid drive address !", fg="red").pack()



def loadDir():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Load Directory")
    screen3.geometry("350x300")
    Label(screen3, text="Please enter details below").pack()
    Label(screen3, text="").pack()

    global loadDisk
    global loadMainFolder
    global loadSavingFolder

    loadDisk = StringVar()
    loadMainFolder = StringVar()
    loadSavingFolder = StringVar()

    global load_disk_entry1
    global load_mainFolder_entry1
    global load_savingFolder_entry1

    Label(screen3, text="Disk of Directory: ").pack()
    load_disk_entry1 = Entry(screen3, textvariable=loadDisk)
    load_disk_entry1.pack()
    Label(screen3, text="").pack()
    Label(screen3, text="Input the name of master folder!").pack()
    load_mainFolder_entry1 = Entry(screen3, textvariable=loadMainFolder)
    load_mainFolder_entry1.pack()
    Label(screen3, text="").pack()
    Label(screen3, text="Input the name of folder to save! ").pack()
    load_savingFolder_entry1 = Entry(screen3, textvariable=loadSavingFolder)
    load_savingFolder_entry1.pack()
    Label(screen3, text="").pack()


    Button(screen3, text="Load directory", width=15, height=1, command=loadDirInfo).pack()





def second_screen():
    global screen
    screen = Tk()
    screen.geometry("512x512")
    screen.title("Choose Option")
    Label(text="CHOOSE THE OPTION TO CREATE NEW DIR OR LOAD OLD DIR", bg="red", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Click here to create new dir", bg="blue", height="8", width="40", font=("Calibri", 15), command=newDir).pack()
    Label(text="").pack()
    Button(text="Click here to load old dir", bg="green", height="7", width="50", font=("Calibri", 15), command=loadDir).pack()

    screen.mainloop()



second_screen()





