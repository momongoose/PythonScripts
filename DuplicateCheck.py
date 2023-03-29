import tkinter as tk
from pynput.keyboard import Key, Controller
from datetime import date
from datetime import datetime
import MySQLdb.converters
import mysql.connector
from mysql.connector import Error
import sys
# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText

global counter
counter = 0

def reorganizeButtons(event):
    e2.place(x=root.winfo_width() - 700, y=100)
    e1.place(x=120, y=100)
    e4.place(x=root.winfo_width() - 700, y=250)
    e3.place(x=120, y=250)
    e6.place(x=root.winfo_width() - 700, y=400)
    e5.place(x=120, y=400)
    e8.place(x=root.winfo_width() - 700, y=550)
    e7.place(x=120, y=550)
    e9.place(x=root.winfo_width() - 500, y=700)
    a = root.winfo_width() - 580
    message2.place(x=a, y=700)

def save():
    Input1 = str(e1.get())
    Input2 = str(e2.get())
    Input3 = str(e3.get())
    Input4 = str(e4.get())
    Input5 = str(e5.get())
    Input6 = str(e6.get())
    Input7 = str(e7.get())
    Input8 = str(e8.get())
    Input9 = str(e9.get())
    Color1 = str(e1.cget("bg"))
    Color2 = str(e2.cget("bg"))
    Color3 = str(e3.cget("bg"))
    Color4 = str(e4.cget("bg"))
    Color5 = str(e5.cget("bg"))
    Color6 = str(e6.cget("bg"))
    Color7 = str(e7.cget("bg"))
    Color8 = str(e8.cget("bg"))
    Color9 = str(e9.cget("bg"))
    if Color1 == "red" or Color2 == "red" or Color3 == "red" or Color4 == "red" or Color5 == "red" or Color6 == "red" or Color7 == "red" or Color8 == "red" or Color9 == "red":
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        pas = "pas"
        s.starttls()
        s.login("login@mail.com", pas)
        sender_email = "sender@mail.com"
        receiver_email = "receiver@mail.com"
        messag = """\
Subject: Error from {}

The entered values:
 {} | {}
 {} | {}
 {} | {}
 {} | {}""".format(Input9, Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8)
        s.sendmail(sender_email, receiver_email, messag)
    if Input9 != "":
        data = [Input1, Input2, Input3, Input4, Input5, Input6, Input7, Input8, Input9, str(datetime.now()), "10"]
        db(data)
        button1.place(relx=0.8, rely=0.01, anchor='n')
        message7.config(text="Last Save: " + datetime.now().strftime("%H:%M:%S"))
        clear()
    else:
        button1.place_forget()

def db(data):
    try:
        connection = mysql.connector.connect(host='host',
                                            database='database',
                                            user='user',
                                            password='password')
        if connection.is_connected():
            cursor = connection.cursor(buffered=True)
            cursor.execute("INSERT into table (`plate1a`,`plate1b`,`plate2a`,`plate2b`,`plate3a`,`plate3b`,`plate4a`,`plate4b`,name,`check_time`, `machine`) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{}) AS new ON DUPLICATE KEY UPDATE plate1a=new.plate1a, plate1b=new.plate1b, plate2a=new.plate2a, plate2b=new.plate2b, plate3a=new.plate3a, plate3b=new.plate3b, plate4a=new.plate4a, plate4b=new.plate4b, name=new.name, check_time=new.check_time, machine=new.machine;".format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10]))
            connection.commit()
    except Error as e:
        print("Error while connecting to MySQL", e, file=sys.stdout)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def clear():
    e1.config(state="normal")
    e1.delete(0, tk.END)
    e1.insert(0, "")
    e2.config(state="normal")
    e2.delete(0, tk.END)
    e2.insert(0, "")
    e3.config(state="normal")
    e3.delete(0, tk.END)
    e3.insert(0, "")
    e4.config(state="normal")
    e4.delete(0, tk.END)
    e4.insert(0, "")
    e5.config(state="normal")
    e5.delete(0, tk.END)
    e5.insert(0, "")
    e6.config(state="normal")
    e6.delete(0, tk.END)
    e6.insert(0, "")
    e7.config(state="normal")
    e7.delete(0, tk.END)
    e7.insert(0, "")
    e8.config(state="normal")
    e8.delete(0, tk.END)
    e8.insert(0, "")
    e9.config(state="normal")
    e9.delete(0, tk.END)
    e9.insert(0, "")
    global counter
    counter = 0
    colorEntrys("")

def colorEntrys(event):
    Input1 = str(e1.get())
    Input2 = str(e2.get())
    Input3 = str(e3.get())
    Input4 = str(e4.get())
    Input5 = str(e5.get())
    Input6 = str(e6.get())
    Input7 = str(e7.get())
    Input8 = str(e8.get())

    if Input1 == Input2 and Input1 != "":
        e1.config(bg="light green", readonlybackground="light green")
        e2.config(bg="light green", readonlybackground="light green")
    elif Input1 == "" and Input2 != "":
        e1.config(bg="yellow", readonlybackground="yellow")
    elif Input2 == "" and Input1 != "":
        e2.config(bg="yellow", readonlybackground="yellow")
    elif Input1 != "" and Input2 != "":
        e1.config(bg="red", readonlybackground="red")
        e2.config(bg="red", readonlybackground="red")
    else:
        e1.config(bg="white")
        e2.config(bg="white")

    if Input3 == Input4 and Input3 != "":
        e3.config(bg="light green", readonlybackground="light green")
        e4.config(bg="light green", readonlybackground="light green")
    elif Input3 == "" and Input4 != "":
        e3.config(bg="yellow", readonlybackground="yellow")
    elif Input4 == "" and Input3 != "":
        e4.config(bg="yellow", readonlybackground="yellow")
    elif Input3 != "" and Input4 != "":
        e3.config(bg="red", readonlybackground="red")
        e4.config(bg="red", readonlybackground="red")
    else:
        e3.config(bg="white")
        e4.config(bg="white")

    if Input5 == Input6 and Input5 != "":
        e5.config(bg="light green", readonlybackground="light green")
        e6.config(bg="light green", readonlybackground="light green")
        if Input5 == Input7 and Input5 != "":
            e5.config(bg="red", readonlybackground="red")
            e7.config(bg="red", readonlybackground="red")
        if Input6 == Input8 and Input6 != "":
            e6.config(bg="red", readonlybackground="red")
            e8.config(bg="red", readonlybackground="red")
    elif Input5 == "" and Input6 != "":
        e5.config(bg="yellow", readonlybackground="yellow")
    elif Input6 == "" and Input5 != "":
        e6.config(bg="yellow", readonlybackground="yellow")
    elif Input5 != "" and Input6 != "":
        e5.config(bg="red", readonlybackground="red")
        e6.config(bg="red", readonlybackground="red")
    else:
        e5.config(bg="white")
        e6.config(bg="white")
    if Input7 == Input8 and Input7 != "":
        e7.config(bg="light green", readonlybackground="light green")
        e8.config(bg="light green", readonlybackground="light green")
    elif Input7 == "" and Input8 != "":
        e7.config(bg="yellow", readonlybackground="yellow")
    elif Input8 == "" and Input7 != "":
        e8.config(bg="yellow", readonlybackground="yellow")
    elif Input7 != "" and Input8 != "":
        e7.config(bg="red", readonlybackground="red")
        e8.config(bg="red", readonlybackground="red")
    else:
        e7.config(bg="white")
        e8.config(bg="white")
    if Input1 == Input3 and Input1 != "":
        e1.config(bg="red", readonlybackground="red")
        e3.config(bg="red", readonlybackground="red")
    if Input2 == Input4 and Input2 != "":
        e2.config(bg="red", readonlybackground="red")
        e4.config(bg="red", readonlybackground="red")
    if Input3 == Input5 and Input3 != "":
        e3.config(bg="red", readonlybackground="red")
        e5.config(bg="red", readonlybackground="red")
    if Input4 == Input6 and Input4 != "":
        e4.config(bg="red", readonlybackground="red")
        e6.config(bg="red", readonlybackground="red")
    if Input5 == Input7 and Input5 != "":
        e5.config(bg="red", readonlybackground="red")
        e7.config(bg="red", readonlybackground="red")
    if Input6 == Input8 and Input6 != "":
        e6.config(bg="red", readonlybackground="red")
        e8.config(bg="red", readonlybackground="red")
    global counter
    if str(event).find("keycode=13") > 0 and counter == 0:
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        e1.config(state="readonly")
        counter += 1
    elif str(event).find("keycode=13") > 0 and counter == 1:
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        e2.config(state="readonly")
        counter += 1
    elif str(event).find("keycode=13") > 0 and counter == 2:
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        e3.config(state="readonly")
        counter += 1
    elif str(event).find("keycode=13") > 0 and counter == 3:
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        e4.config(state="readonly")
        counter += 1
    elif str(event).find("keycode=13") > 0 and counter == 4:
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        e5.config(state="readonly")
        counter += 1
    elif str(event).find("keycode=13") > 0 and counter == 5:
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        e6.config(state="readonly")
        counter += 1
    elif str(event).find("keycode=13") > 0 and counter == 6:
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        e7.config(state="readonly")
        counter += 1
    elif str(event).find("keycode=13") > 0 and counter == 7:
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        e8.config(state="readonly")
        counter += 1


keyboard = Controller()
root = tk.Tk()
root.geometry("1500x800")
root.configure(bg="light blue")
root.resizable(False, False)
root.iconbitmap(default="icon.ico")
root.title("title")
message = tk.Label(root, text="Duplicate Check", fg="black", bg="light blue", width="800")
message.config(font=('Helvatical bold', 20, "bold"))
message2 = tk.Label(root, text="Name:", fg="black", bg="light blue")
message2.config(font=('Helvatical bold', 18, "bold"))
message3 = tk.Label(root, text="Plate 1", fg="black", bg="light blue")
message3.config(font=('Helvatical bold', 18, "bold"))
message4 = tk.Label(root, text="Plate 2", fg="black", bg="light blue")
message4.config(font=('Helvatical bold', 18, "bold"))
message5 = tk.Label(root, text="Plate 3", fg="black", bg="light blue")
message5.config(font=('Helvatical bold', 18, "bold"))
message6 = tk.Label(root, text="Plate 4", fg="black", bg="light blue")
message6.config(font=('Helvatical bold', 18, "bold"))
message7 = tk.Label(root, text="", fg="black", bg="light blue")
message7.config(font=('Helvatical bold', 18, "bold"))
button1 = tk.Button(root, text="Clear All", fg="black", bg="light grey", command=clear)
button1.config(font=('Helvatical bold', 18, "bold"))
button2 = tk.Button(root, text="Save", fg="black", bg="light grey", command=save)
button2.config(font=('Helvatical bold', 18, "bold"))
e1 = tk.Entry(root, width=20, font=("Helvatical 40"), justify="center")
e2 = tk.Entry(root, width=20, font=("Helvatical 40"), justify='center')
e3 = tk.Entry(root, width=20, font=("Helvatical 40"), justify='center')
e4 = tk.Entry(root, width=20, font=("Helvatical 40"), justify='center')
e5 = tk.Entry(root, width=20, font=("Helvatical 40"), justify='center')
e6 = tk.Entry(root, width=20, font=("Helvatical 40"), justify='center')
e7 = tk.Entry(root, width=20, font=("Helvatical 40"), justify='center')
e8 = tk.Entry(root, width=20, font=("Helvatical 40"), justify='center')
e9 = tk.Entry(root, width=20, font=("Helvatical 20"), justify='center')
message.place(relx=0.5, rely=0, anchor='n')
message3.place(relx=0.5, rely=0.15, anchor='n')
message4.place(relx=0.5, rely=0.33, anchor='n')
message5.place(relx=0.5, rely=0.52, anchor='n')
message6.place(relx=0.5, rely=0.71, anchor='n')
message7.place(relx=0.9, rely=0.924, anchor='n')
a = root.winfo_width() - 580
message2.place(x=a, y=700)
button1.place(relx=0.8, rely=0.01, anchor='n')
button2.place(relx=0.95, rely=0.93, anchor='se')
e2.place(x=root.winfo_width() - 700, y=100)
e1.place(x=120, y=100)
e4.place(x=root.winfo_width() - 700, y=250)
e3.place(x=120, y=250)
e6.place(x=root.winfo_width() - 700, y=400)
e5.place(x=120, y=400)
e8.place(x=root.winfo_width() - 700, y=550)
e7.place(x=120, y=550)
e9.place(x=root.winfo_width() - 500, y=700)
root.bind("<Key>", colorEntrys)
root.bind("<Configure>", reorganizeButtons)
root.mainloop()
