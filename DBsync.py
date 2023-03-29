import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='host',
                                         database='database',
                                         user='user',
                                         password='password')
    if connection.is_connected():
        cursor = connection.cursor()
        sql = "SELECT name FROM table1;"
        sql2 = "INSERT INTO tableA(name) VALUES (%s) AS new ON DUPLICATE KEY UPDATE name=new.name;"
        cursor.execute(sql)
        list = cursor.fetchall()
        cursor.executemany(sql2, list)
        connection.commit()
except Error as e:
    logging.error("Error while connecting to MySQL", e)

try:
    connection = mysql.connector.connect(host='host',
                                         database='database',
                                         user='user',
                                         password='password')
    if connection.is_connected():
        cursor = connection.cursor()
        sql = "SELECT name FROM table2;"
        sql2 = "INSERT INTO tableB(name) VALUES (%s) AS new ON DUPLICATE KEY UPDATE name=new.name;"
        cursor.execute(sql)
        list = cursor.fetchall()
        cursor.executemany(sql2, list)
        connection.commit()
except Error as e:
    logging.error("Error while connecting to MySQL", e)

try:
    connection = mysql.connector.connect(host='host',
                                         database='database',
                                         user='user',
                                         password='password')
    if connection.is_connected():
        cursor = connection.cursor()
        sql = "SELECT name FROM table3;"
        sql2 = "INSERT INTO ftableC(name) VALUES (%s) AS new ON DUPLICATE KEY UPDATE name=new.name;"
        cursor.execute(sql)
        list = cursor.fetchall()
        cursor.executemany(sql2, list)
        connection.commit()
except Error as e:
    logging.error("Error while connecting to MySQL", e)