import mysql.connector


def connect():
    cnx = mysql.connector.connect(
        host="localhost", user="root", password="password", database="bmiapp"
    )

    cnx.ping(reconnect=True)

    return cnx
