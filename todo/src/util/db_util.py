import mysql.connector


def connect():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="23010025_exam_db"
    )
    # コネクションが切れたときに再接続する
    cnx.ping(reconnect=True)
    return cnx


def change_priority(priority):
    if priority == 1:
        priority = '高'
    elif priority == 2:
        priority = '中'
    elif priority == 3:
        priority = '低'
    return priority
