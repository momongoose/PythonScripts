import mariadb
import sys
import mysql.connector
from mysql.connector import Error
import logging
logging.basicConfig(filename="Errorlog.log", level=logging.ERROR)

try:
    conn = mariadb.connect(
        user="user",
        password="password",
        host="host",
        port="port",
        database="database"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()
a = []
cur.execute("""
sql SELECT query
""")

try:
    connection = mysql.connector.connect(host='host',
                                         database='database',
                                         user='user',
                                         password='password')
    if connection.is_connected():
        cursor = connection.cursor()
        for val in cur:
            x = list(val)
            count = 0
            for var in x:
                if count == 2:
                    if var is None:
                        x[count] = None
                elif count > 13:
                    if var is None:
                        x[count] = ""
                else:
                    if var is None:
                        x[count] = 0
                count += 1
            val = tuple(x)
            a.append(val)
        sql = "INSERT INTO table(column) VALUES (%s) AS new ON DUPLICATE KEY UPDATE column=new.column;"
        cursor.executemany(sql, a)
        connection.commit()
except Error as e:
    logging.error("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        cur.close()
        conn.close()