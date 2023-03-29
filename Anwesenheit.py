import requests
import pandas as pd
import tkinter as tk
from functools import partial


headers = {
    'Accept': 'application/json',
    'Authorization': 'Token abc'
}

att = []
per = []
emp = []
dat = []
eve = []
tim = []
root = tk.Tk()

def getDataFromDate(Date):
    if Date[0:2] != "20" or Date.find("-") == -1 or len(Date) != 10:
        err = tk.Label(root, text="Wrong Date", fg="black", bg="red", width="20")
        err.config(font=('Helvatical bold', 20, "bold"))
        err.pack(pady=50)
        return err.after(2000, lambda: err.destroy())

    r = requests.get('https://url/4/api/call/'+Date, headers=headers)

    employeeData = r.json()

    for key in employeeData["attendanceRegistration"]:
        att.append(key["attendanceRegistrationId"])
        emp.append(key["employeeId"])
        per.append(key["personnelNumber"])
        rawTime = str(key["dateTime"])
        cutTime = rawTime[11:19]
        HourInt = cutTime[0:2]
        if HourInt == "23":
           HourInt = "00"
           Date = rawTime[:8]
           Day = str(int(rawTime[8:10]) + 1)
           if len(Day) == 1:
               Day = "0" + Day
           Date = Date + Day
        else:
           HourInt = int(HourInt) + 1
           HourInt = str(HourInt)
           Date = rawTime[:10]
           if len(HourInt) == 1:
               HourInt = "0" + HourInt
        ourTimezone = HourInt + cutTime[2:]
        dat.append(Date)
        tim.append(ourTimezone)
        eve.append(key["event"])

    a = {"Anwesenheits-RegistrierungsID": att, "MitarbeiterID": emp, 'Personalnummer': per, "Datum": dat, 'Uhrzeit': tim, "Ereigniss": eve}
    df = pd.DataFrame(a)
    writer = pd.ExcelWriter('Anwesenheit.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
    suc = tk.Label(root, text="Erfolgreich", fg="black", bg="light green", width="20")
    suc.config(font=('Helvatical bold', 20, "bold"))
    suc.pack(pady=50)
    suc.after(2000, lambda: suc.destroy())

def FuncToCallFunc():
    getDataFromDate(str(e1.get()))


root.geometry("1000x600")
root.configure(bg="light blue")
message = tk.Label(root, text="Anwesenheitsliste", fg="black", bg="light blue", width="800")
message.config(font=('Helvatical bold',20, "bold"))
InputText = tk.Label(root, text="Bitte ein Datum zur Kontrolle eingeben,\nin dem Format YYYY-MM-DD", fg="black", bg="light blue", width=800, height=5)
InputText.config(font=('Helvatical bold', 15))
e1 = tk.Entry(root, width=15, font=("Helvatical 15"), justify='center')
Input = str(e1.get())
Button1 = tk.Button(root, text='Check', command=FuncToCallFunc)
Button1.config(font=('Helvatical bold', 15))
message.pack(pady=20)
InputText.pack()
e1.pack()
Button1.pack(pady=20)
root.mainloop()
