import shutil
import os
from os import path
import logging
from datetime import datetime
from pathlib import Path
import glob
import mariadb


def getDbData():
    try:
        cnx = mariadb.connect(
            user="user",
            password="password",
            host="host",
            port="port",
            database="database"
        )
        cursor = cnx.cursor()

        cursor.execute(
            "SELECT plate_id, machine FROM table WHERE check_time > now() - INTERVAL 200 MINUTE"# AND (plate_id = '1%' OR plate_id = '2%');"
        )
        Plates = cursor.fetchall()
        cursor.close()
        cnx.close()
        return Plates

    except mysql.connector.Error as err:
        print("Error: " + str(err))


def searchFolder(folder, array):
    folder = str(folder) + "\\good"
    target = r"path"
    GLOB_PARMS = "*.txt"
    for file in glob.glob(os.path.join(folder, GLOB_PARMS)):
        filename = str(os.path.basename(file)).split(".")[0]
        fil1 = target + "\\good\\" + filename + ".txt"
        fil2 = target + "\\" + filename + ".txt"
        try:
            if str(filename.split("-")[1]) == str(array) and path.exists(fil1) == False and path.exists(fil2) == False:
                shutil.copy(file, target)
                logging.info(
                    filename + " is moved to " + str(target) + " time: " + datetime.now().strftime("%H:%M:%S %d/%m/%Y"))
        except:
            pass


if __name__ == "__main__":
    logging.basicConfig(filename="Infolog.log", level=logging.INFO)
    Dir = r"\\path"
    Plates = getDbData()
    arr = []
    for plate in Plates:
        if plate[0] != "":
            arr.append(plate[0])
    for ar in arr:
        for folder in Path(Dir).glob("*"):
            if "Machine" in str(folder):
                searchFolder(folder, ar)
