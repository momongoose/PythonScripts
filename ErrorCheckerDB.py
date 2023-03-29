import mysql.connector
from mysql.connector import Error
from datetime import datetime
import logging


def insertTableData(err, sample, machine):
    sql = "INSERT INTO table (event,sample,time,done,file,machine) VALUES (%s,%s,%s,%s,%s,%s);"
    val = (err, sample, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 0, "none", machine)
    try:
        connection = mysql.connector.connect(host='host', database='database', user='user',
                                             password='password')
        if connection.is_connected():
            with open('Errorlog.log') as f:
                if str(err) + " | " + str(sample) + " | " + str(machine) + "\n" in f.read():
                    o = 0
                    cursor = connection.cursor()
                else:
                    logging.error(str(err) + " | " + str(sample) + " | " + str(machine) + "\n")
                    cursor = connection.cursor()
                    cursor.execute(sql, val)
                    connection.commit()
    except Error as e:
        logging.error("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def checkDuplicateSample():
    try:
        connection = mysql.connector.connect(host='host',
                                             database='database',
                                             user='user',
                                             password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(
                "SELECT sample_id, COUNT(sample_id) FROM table GROUP BY sample_id HAVING COUNT(sample_id) > 1;")
            record = cursor.fetchall()
            for sample in record:
                if "EMPTY" in sample:
                    continue
                cursor = connection.cursor()
                cursor.execute("SELECT machine FROM table WHERE sample_id = '" + sample[0] + "';")
                rec = cursor.fetchall()
                try:
                    machine = "MACHINE_" + str(rec[0][0]) + " | " + "MACHINE_" + str(rec[1][0])
                except:
                    machine = "MACHINE_" + str(rec[0][0]) + " | " + "MACHINE_" + str(rec[1][0])
                insertTableData("duplicate sample ID", sample[0], machine)
    except Error as e:
        Errorlog.error("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def checkDuplicatePlate():
    try:
        connection = mysql.connector.connect(host='host',
                                             database='database',
                                             user='user',
                                             password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT DISTINCT(plate_id) FROM table;")
            record = cursor.fetchall()
            for plate in record:
                if "EMPTY" in plate:
                    continue
                cur = connection.cursor()
                cur.execute("SELECT max(DISTINCT run) FROM table WHERE plate_id = '" + str(plate[0]) + "';")
                rec = cur.fetchall()
                cu = connection.cursor()
                cu.execute(
                    "SELECT DISTINCT(plate_id), COUNT(plate_id) FROM table WHERE plate_id = '" + str(
                        plate[0]) + "' GROUP BY plate_id HAVING COUNT(plate_id) >" + str(
                        rec[0][0] * 93) + ";")
                rem = cu.fetchall()
                curs = connection.cursor()
                try:
                    curs.execute("SELECT DISTINCT machine FROM table WHERE plate_id = '" + str(rem[0][0]) + "';")
                except:
                    continue
                re = curs.fetchall()
                try:
                    machine = "MACHINE_" + str(re[0][0]) + " | " + "MACHINE_" + str(re[1][0])
                except:
                    machine = "MACHINE_" + str(re[0][0]) + " | " + "MACHINE_" + str(re[0][0])
                insertTableData("duplicate plate ID", rem[0][0], machine)
    except Error as e:
        Errorlog.error("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


if __name__ == '__main__':
    logging.basicConfig(filename="Errorlog.log", level=logging.ERROR)
    checkDuplicateSample()
    checkDuplicatePlate()
