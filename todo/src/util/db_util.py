import mysql.connector


def connect():
    cnx = mysql.connector.connect(
        host="localhost", user="root", password="password", database="23010025_exam_db"
    )
    cnx.ping(reconnect=True)

    return cnx
