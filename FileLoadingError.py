
import glob
import logging
import os
import time
from datetime import datetime

pathTrl = r"path"

pathSvc = r"path"

directory = str(os.getcwd())

pathLog = directory + r"\Errorlog.log"

messagePath = directory + r"\Error_Messages.txt"

messages = ""

with open(messagePath) as f:
    messages = f.readlines()

logging.basicConfig(filename="Errorlog.log", level=logging.ERROR)  # creates logging file


def read_text_file(path, logPath, msg):  # this function goes through the folder and all folders in them and searches
    # every
    # file for the entered messages
    os.chdir(path)
    folder_array = []
    file_array = []
    folder_file_array = []
    text_array = []
    file_text_array = []

    for folder in glob.glob("*"):
        folder_array.append(folder)
    i = 0
    for folder in folder_array:
        if len(os.listdir(path + "\\" + folder)) > 0:

            os.chdir(path + "\\" + folder)
            list_of_files = glob.glob('*.log')
            latest_file = max(list_of_files, key=os.path.getctime)
            text = ""
            lines = ""
            with open(latest_file) as f:
                for line in f:
                    lines += line
                text = text + str(lines)
            text_array.append(text)
            file_array.append(latest_file)
            file_text_array.append(text_array)
            folder_file_array.append(file_array)
            file_array = []
            i += 1
    j = 0
    for folder in folder_file_array:
        if not folder:
            continue
        for file in folder:
            for err in msg:
                err = err.replace("\n", "")
                if file_text_array[0][j].find(err) > 0 and str(open(logPath, "r").read()).find(
                        ' "' + err + '"' + "\n" + "Error Message found in File:\n" + file) < 1:
                    logging.error(
                        ' "' + err + '"' + "\n" + "Error Message found in File:\n" + file + "\ntime: " + datetime.now().strftime(
                            "%d/%m/%Y %H:%M:%S") + "\n")
            j += 1


x = 0

while x == 0:
    read_text_file(pathSvc, pathLog, messages)
    print("Success Svc")
    read_text_file(pathTrl, pathLog, messages)
    print("Success Trl")