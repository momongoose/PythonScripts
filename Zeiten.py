import tkinter as tk
import pandas as pd
import requests

headers = {
    'Accept': 'application/json',
    'Authorization': 'Token abc'
}

stempler = {}
root = tk.Tk()


def getDataFromDate(Date):
    if Date[0:2] != "20" or Date.find("-") == -1 or len(Date) != 10:
        err = tk.Label(root, text="Falsches Datum", fg="black", bg="red", width="20")
        err.config(font=('Helvatical bold', 20, "bold"))
        err.pack(pady=50)
        return err.after(2000, lambda: err.destroy())

    r = requests.get('https://url/4/api/call/' + Date, headers=headers)

    employeeData = r.json()

    for key in employeeData["Registration"]:
        rawTime = str(key["dateTime"])
        cutTime = rawTime[11:16]
        HourInt = cutTime[0:2]
        MinInt = cutTime[3:6]
        Zeit = HourInt + ':' + MinInt
        #s = {"id": None, "check-in": None, "check-out": None}
        if key["event"] == "clocked in":
            s = {"id": key["Number"], "check-in": Zeit, "check-out": None}
        else:
            s = {"id": key["Number"], "check-in": None, "check-out": Zeit}
        if not (bool(stempler)):
            stempler[key["Number"]] = s
        elif key["Number"] not in stempler:
            stempler[key["Number"]] = s
        else:
            x = stempler[key["Number"]]
            if s["check-in"] is not None and x["check-in"] is None:
                x["check-in"] = s["check-in"]
            elif s["check-out"] is not None and x["check-out"] is None:
                x["check-out"] = s["check-out"]
            elif s["check-in"] is not None and x["check-in"] is not None:
                if s["check-in"] < x["check-in"]:
                    x["check-in"] = s["check-in"]
            else:
                if s["check-out"] > x["check-out"]:
                    x["check-out"] = s["check-out"]
            stempler[key["Number"]] = x

    id_ = []
    cIn = []
    cOut = []
    dd = []
    for key in stempler:
        id_.append(stempler[key]["id"])
        if stempler[key]["check-in"] is None:
            cIn.append('00:00')
        else:
            cIn.append(stempler[key]["check-in"])
        if stempler[key]["check-out"] is None:
            cOut.append('24:00')
        else:
            cOut.append(stempler[key]["check-out"])
        dd.append(Date)

    a = {"ID": id_, "Datum": dd, "Ein": cIn, "Aus": cOut}
    df = pd.DataFrame(a)
    writer = pd.ExcelWriter('../Excel/' + Date + 'Zeiten.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Zeiten', index=False)
    writer.save()
    suc = tk.Label(root, text="Erfolgreich", fg="black", bg="light green", width="20")
    suc.config(font=('Helvatical bold', 20, "bold"))
    suc.pack(pady=50)
    suc.after(2000, lambda: suc.destroy())


def FuncToCallFunc():
    getDataFromDate(str(e1.get()))


root.geometry("1000x600")
root.configure(bg="light blue")
message = tk.Label(root, text="Zeiten", fg="black", bg="light blue", width="800")
message.config(font=('Helvatical bold', 20, "bold"))
InputText = tk.Label(root, text="Datum für die Zeiten eingeben\nFormat: YYYY-MM-DD", fg="black", bg="light blue",
                     width=800, height=5)
InputText.config(font=('Helvatical bold', 15))
e1 = tk.Entry(root, width=15, font=("Helvatical 15"), justify='center')
Input = str(e1.get())
Button1 = tk.Button(root, text='Herunterladen', command=FuncToCallFunc)
Button1.config(font=('Helvatical bold', 15))
message.pack(pady=20)
InputText.pack()
e1.pack()
Button1.pack(pady=20)
root.mainloop()
