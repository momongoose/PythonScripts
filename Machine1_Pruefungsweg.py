import shutil
import os
from os import path
import logging
from datetime import datetime
from pathlib import Path
import glob
import mysql.connector


def getDbData():
    try:
        cnx = mysql.connector.connect(
            user="user",
            password="password",
            host="host",
            port="port",
            database="database",
        )
        cursor = cnx.cursor()

        cursor.execute(
            "SELECT plate1a, plate2a, plate3a, plate4a, machine FROM table WHERE check_time > now() - INTERVAL 3 MINUTE;"
        )
        Plates = cursor.fetchall()
        cursor.close()
        cnx.close()
        return Plates

    except mysql.connector.Error as err:
        print("Error: " + str(err))


def searchFolder(folder, array):
    folder = str(folder) + "\\good"
    target = r"path" + str(
        array[-1])
    GLOB_PARMS = "*.csv"
    for file in glob.glob(os.path.join(folder, GLOB_PARMS)):
        filename = str(os.path.basename(file)).split(".")[0]
        fil1 = target + "\\good\\" + filename + ".csv"
        fil2 = target + "\\" + filename + ".csv"
        if filename.split("-")[0] in array and path.exists(fil1) == False and path.exists(fil2) == False:
            shutil.copy(file, target)
            logging.info(
                filename + " is moved to " + str(target) + " time: " + datetime.now().strftime("%H:%M:%S %d/%m/%Y"))


if __name__ == "__main__":
    logging.basicConfig(filename="Infolog.log", level=logging.INFO)
    Dir = r"path"
    Plates = getDbData()
    array = []
    arr = []
    for plates in Plates:
        for plate in plates:
            if plate != "":
                array.append(plate)
        arr.append(array)
        array = []
    for ar in arr:
        for folder in Path(Dir).glob("*"):
            if "Machine2" in str(folder):
                searchFolder(folder, ar)
