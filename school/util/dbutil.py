import mysql.connector


# データベースに接続します
def connect():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="school",
    )

    # コネクションが切れたときに再接続する
    cnx.ping(reconnect=True)

    return cnx
