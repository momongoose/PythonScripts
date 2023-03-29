import glob
import logging
import os
import multiprocessing
import re
from pathlib import Path
from datetime import datetime
import mysql.connector
from mysql.connector import Error

logging.basicConfig(filename="Errorlog.log", level=logging.ERROR)
directory = str(os.getcwd())

def CheckFileInFolderSvc(folder):
    messagePath = directory + "\\Error_Messages.txt"
    with open(messagePath) as f:
        msg = f.readlines()
    pathSvc = r"path"
    pathLog = directory + "\\Errorlog.log"
    pathFolder = r"{}\*".format(folder)
    os.chdir(pathSvc)
    if len(os.listdir(folder)) > 0:
        os.chdir(folder)
        list_of_files = glob.glob(pathFolder)
        latest_file = max(list_of_files, key=os.path.getmtime)
        with open(latest_file, encoding="ANSI") as file:
            for line in (file.readlines()):
                for err in msg:
                    err = err.replace("\n", "")
                    if line.find(err) != -1:
                        pattern = " '(.*?)' "
                        sample = re.search(pattern, line).group(1)
                        start = line.index("MACHINE")
                        end = start + 11
                        janus = line[start:end]
                    if line.find(err) != -1 and str(open(pathLog, "r").read()).find(line) == -1:
                        if line.find("EMPTY") != -1 or line.find("Cassette") != -1:
                            continue
                        sql = "INSERT INTO table (event,sample,time,done,file,machine) VALUES (%s,%s,%s,%s,%s,%s);"
                        val = (err, sample, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 0, latest_file, janus)
                        try:
                            connection = mysql.connector.connect(host='host', database='database', user='user', password='password')
                            if connection.is_connected():
                                cursor = connection.cursor()
                                cursor.execute(sql, val)
                                connection.commit()
                        except Error as e:
                            logging.error("Error while connecting to MySQL", e)
                        finally:
                            if connection.is_connected():
                                cursor.close()
                                connection.close()
                        logging.error(line + " | " + datetime.now().strftime("%H:%M:%S %d/%m/%Y"))

if __name__ == "__main__":
    multiprocessing.freeze_support()
    Svc = r"path"
    folder_array = []
    for folder in Path(Svc).glob("*"):
        if str(folder).find("rick") > 0:
            continue
        folder_array.append(str(folder))
    pool = multiprocessing.Pool(4)
    pool.map(CheckFileInFolderSvc, folder_array)