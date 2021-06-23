from tkinter import *
import os
import re




def newEvent():
    event_info = Ename.get()
    starting_date = Sdate.get()
    closing_date = Cdate.get()


    if os.path.exists("programsInfo.txt"):
        fileu = open("programsInfo.txt", "r+")
    else:
        fileu = open("programsInfo.txt", "x")
        fileu.close()
        fileu = open("programsInfo.txt", "r+")




def register_event():



    global screen2
    screen2 = Toplevel(screen)
    screen2.title("New event")
    screen2.geometry("512x312")

    Label(screen2, text="Please enter details below").pack()
    Label(screen2, text="").pack()


    global Ename
    global Sdate
    global Cdate

    Ename = StringVar()
    Sdate = StringVar()
    Cdate = StringVar()

    global Ename_entry1
    global Sdate_entry1
    global Cdate_entry1

    Label(screen2, text="Name of the event ").pack()
    Ename_entry1 = Entry(screen2, textvariable=Ename)
    Ename_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Event starting date (DD-MM-YYYY)").pack()
    Sdate_entry1 = Entry(screen2, textvariable=Sdate)
    Sdate_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Event closing date (DD-MM-YYYY)").pack()
    Cdate_entry1 = Entry(screen2, textvariable=Cdate)
    Cdate_entry1.pack()
    Label(screen2, text="").pack()


    Button(screen2, text="Create Event", width=15, height=1, command = newEvent).pack()




def register_user():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Register Costumer")
    screen2.geometry("512x412")

    Label(screen2, text="Please enter details below").pack()
    Label(screen2, text="").pack()

    global event
    global Uname
    global Umail
    global ref
    global isadult

    Uname = StringVar()
    Umail = StringVar()
    ref = StringVar()
    event = StringVar()
    isadult = StringVar()

    global event_entry1
    global Uname_entry1
    global Umail_entry1
    global ref_entry1
    global isadult_entry1

    Label(screen2, text="Name of the event ").pack()
    event_entry1 = Entry(screen2, textvariable=event)
    event_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Reference number").pack()
    ref_entry1 = Entry(screen2, textvariable=ref)
    ref_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Name of customer").pack()
    Uname_entry1 = Entry(screen2, textvariable=Uname)
    Uname_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="E-mail adress").pack()
    Umail_entry1 = Entry(screen2, textvariable=Umail)
    Umail_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="a for adult and c for child").pack()
    isadult_entry1 = Entry(screen2, textvariable=isadult)
    isadult_entry1.pack()
    Label(screen2, text="").pack()


    Button(screen2, text="Register Customer", width=15, height=1).pack()








def first_screen():
    global screen
    screen = Tk()
    screen.geometry("512x512")
    screen.title("Choose Option")
    Label(text="CHOOSE THE OPTION TO REGISTER EVENT OR USER", bg="red", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Click here to register event", bg="blue", height="8", width="40", font=("Calibri", 15), command = register_event).pack()
    Label(text="").pack()
    Button(text="Click here to register user", bg="green", height="7", width="50", font=("Calibri", 15), command = register_user).pack()

    screen.mainloop()




first_screen()