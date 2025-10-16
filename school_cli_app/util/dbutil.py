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


def confirming(prompt):
    while True:
        message = input(prompt).strip().lower()

        if message == "y":
            return True
        elif message == "n":
            return False
        else:
            print("入力された値は指定されていません")
            print("Yかnで入力してください")
