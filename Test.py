import mysql.connector
from mysql.connector import Error
from mysql.connector import MySQLConnection, Error

def query_with_fetchall():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='project2',
                                       user='alex',
                                       password='supachief6')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM attendance")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
    

def connect():
    """ Connect to MySQL database """
    conn = None
    
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='project2',
                                       user='alex',
                                       password='supachief6')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            
    


if __name__ == '__main__':
    connect()
    
if __name__ == '__main__':
    query_with_fetchall()