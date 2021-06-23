import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
import xlwt
from xlwt import Workbook

from functools import partial

HEIGHT=700
WIDTH=800

window=tk.Tk()
window.title("Event registration")

canvas1=tk.Canvas(window,height=HEIGHT,width=WIDTH)
canvas1.pack()

frame1=tk.Frame(window,bg="#80c1ff")
frame1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)


def button3_clicked():
    print(Name)
    messagebox.showinfo("Registered", "Registration complete!!")
def button4_clicked():

    window4 = tk.Tk()
    window.title("Select Date")
    canvas1 = tk.Canvas(window, height=HEIGHT, width=WIDTH)
    canvas1.pack()

    cal = Calendar(window4,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2018, month=2, day=5)
    cal.pack(fill="both", expand=True)
    print(cal.selection_get())


def button2_clicked():
    global Name,Email,Refcode
    Name=tk.StringVar()
    Email=tk.StringVar()
    Refcode=tk.StringVar()
    window2=tk.Toplevel(window)
    window2.title("Costumer detail")
    canvas2=tk.Canvas(window2,height=700,width=800)
    canvas2.pack()

    frame2=tk.Frame(window2,bg="#80c1ff",bd=0)
    frame2.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

    tk.Label(window2, text="Name:",bg="#80c1ff").place(relx=0.17,rely=0.18,relwidth=0.15,relheight=0.08)
    tk.Label(window2, text="Email:",bg="#80c1ff").place(relx=0.17,rely=0.25,relwidth=0.15,relheight=0.08)
    tk.Label(window2, text="REF code:", bg="#80c1ff").place(relx=0.17, rely=0.32, relwidth=0.15, relheight=0.08)

    E1=tk.Entry(window2,textvariable=Name)
    E1.place(relx=0.33,rely=0.19,relwidth=0.45,relheight=0.05)

    E2=tk.Entry(window2,textvariable=Email)
    E2.place(relx=0.33,rely=0.27,relwidth=0.45,relheight=0.05)
    E3=tk.Entry(window2,textvariable=Refcode)
    E3.place(relx=0.33, rely=0.35, relwidth=0.45, relheight=0.05)

    ok_but=tk.Button(frame2,text="ENTER", bg='green',command=button3_clicked)
    ok_but.place(relx=0.45,rely=0.6,relwidth=0.2,relheight=0.08)

def button1_clicked():
    global NOE, RS, RC
    NOE = tk.StringVar()
    RS = tk.StringVar()
    RC= tk.StringVar()
    window3 = tk.Toplevel(window)
    window3.title("Event Detail")
    canvas3 = tk.Canvas(window3, height=700, width=800)
    canvas3.pack()

    frame2 = tk.Frame(window3, bg="#80c1ff", bd=0)
    frame2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    tk.Label(window3, text="Name of Event:", bg="#80c1ff").place(relx=0.17, rely=0.18, relwidth=0.15, relheight=0.08)
    tk.Label(window3, text="Registration starting Date", bg="#80c1ff").place(relx=0.17, rely=0.25, relwidth=0.2, relheight=0.08)
    tk.Label(window3, text="Registration closing Date", bg="#80c1ff").place(relx=0.17, rely=0.32, relwidth=0.2, relheight=0.08)

    E1 = tk.Entry(window3, textvariable=NOE)
    E1.place(relx=0.33, rely=0.19, relwidth=0.45, relheight=0.05)

    starting = tk.Button(frame2, text="Click Me", bg='green', command=button4_clicked)
    starting.place(relx=0.35, rely=0.2, relwidth=0.15, relheight=0.08)

    closing= tk.Button(frame2, text="Click Me", bg='green', command=button4_clicked)
    closing.place(relx=0.35, rely=0.3, relwidth=0.15, relheight=0.08)

    # E2 = tk.Entry(window3, textvariable=RS)
    # E2.place(relx=0.33, rely=0.27, relwidth=0.45, relheight=0.05)
    # E3 = tk.Entry(window3, textvariable=RC)
    # E3.place(relx=0.33, rely=0.35, relwidth=0.45, relheight=0.05)
    ok_but = tk.Button(frame2, text="Register", bg='green', command=button2_clicked)
    ok_but.place(relx=0.45, rely=0.6, relwidth=0.2, relheight=0.08)

    wb = Workbook()
    sheet1 = wb.add_sheet('NOE')
    # sheet1.write(1, 0, 'NOE')
    sheet1.write(1, 1, 'starting')
    sheet1.write(1, 2, 'closing')
    wb.save('xlwt example1.xls')


button1 = tk.Button(frame1, compound=tk.TOP, width=10, height=10,
    text="Add New Event", bg='grey', command=button1_clicked)
button1.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.2)

window.mainloop()
