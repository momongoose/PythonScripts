
import glob
import logging
import os
import multiprocessing
from pathlib import Path
from datetime import datetime
import sqlite3

logging.basicConfig(filename="Errorlog.log", level=logging.ERROR)
directory = str(os.getcwd())


def CheckFileInFolderSvc(folder):
    messagePath = directory + "\\Error_Messages.txt"
    with open(messagePath) as f:
        msg = f.readlines()
    pathSvc = r"path"
    pathLog = directory + "\\Errorlog.log"
    os.chdir(pathSvc)
    if len(os.listdir(folder)) > 0:
        os.chdir(folder)
        list_of_files = glob.glob('*.log')
        latest_file = max(list_of_files, key=os.path.getmtime)
        with open(latest_file, encoding="ANSI") as file:
            for line in (file.readlines()):
                for err in msg:
                    err = err.replace("\n", "")
                    if line.find(err) != -1:
                        logging.error("...")
                    if line.find(err) != -1 and str(open(pathLog, "r").read()).find(
                            ' "' + err + '"' + " in " + latest_file + " found\n" + latest_file) == -1:
                        conn = sqlite3.connect(directory + "\\Errorlog.db")
                        cur = conn.cursor()
                        cur.execute("INSERT INTO table(event,time,file) VALUES(?,?,?)", (err, datetime.now().strftime("%H:%M:%S %d/%m/%Y"), latest_file))
                        conn.commit()
                        logging.error(
                            ' "' + err + '"' + " in " + latest_file + " found\ntime: " + datetime.now().strftime(
                                "%H:%M:%S %d/%m/%Y") + "\n")


def CheckFileInFolderTrl(folder):
    messagePath = directory + "\\Error_Messages.txt"
    with open(messagePath) as f:
        msg = f.readlines()
    pathTrl = r"path"
    pathLog = directory + "\\Errorlog.log"
    os.chdir(pathTrl)
    if len(os.listdir(folder)) > 0:
        os.chdir(folder)
        list_of_files = glob.glob('*.log')
        latest_file = max(list_of_files, key=os.path.getmtime)
        with open(latest_file, encoding="ANSI") as file:
            for line in (file.readlines()):
                for err in msg:
                    err = err.replace("\n", "")
                    if line.find(err) != -1:
                        logging.error("...")
                    if line.find(err) != -1 and str(open(pathLog, "r").read()).find(
                            ' "' + err + '"' + " in " + latest_file + " found\n" + latest_file) == -1:
                        conn = sqlite3.connect(directory + "\\Errorlog.db")
                        cur = conn.cursor()
                        cur.execute("INSERT INTO table(event,time,file) VALUES(?,?,?)", (err, datetime.now().strftime("%H:%M:%S %d/%m/%Y"), latest_file))
                        conn.commit()
                        logging.error(
                            ' "' + err + '"' + " in " + latest_file + " found\ntime: " + datetime.now().strftime(
                                "%H:%M:%S %d/%m/%Y") + "\n")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    begin = os.path.getsize(directory + "\\Errorlog.log")
    #logging.error("Logging started at: " + datetime.now().strftime("%H:%M:%S"))
    Trl = r"path"
    Svc = r"path"
    folder_array = []
    for folder in Path(Svc).glob("*"):
        if str(folder).find("rick") > 0:
            continue
        folder_array.append(str(folder))
    pool = multiprocessing.Pool(4)
    pool.map(CheckFileInFolderSvc, folder_array)
    folder_array2 = []
    #logging.error("finished Svc Check and starting Trl Check")
    for folder in Path(Trl).glob("*"):
        folder_array2.append(str(folder))
    pool.map(CheckFileInFolderTrl, folder_array2)
    end = os.path.getsize(directory + "\\Errorlog.log")
    #logging.error("Logging ended at: " + datetime.now().strftime("%H:%M:%S"))
    if begin != 0 and begin == end:
        #wenn kein Fehler gefunden wird, aber Fehler im File stehen entweder trl fehler oder svc fehler
        time = datetime.now().strftime("%d%m%Y_%H%M%S")
        f = open(directory + "\\Errorlog.log", "r")
        read = f.read()
        fo = open(directory + "\\Errorlog.log", "w")
        fi = open(directory + "\\Logfolder\\Error" + time + ".log", "w")
        fi.write(read.replace("ERROR:root:...",""))
        fo.write("")
