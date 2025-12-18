import mysql.connector
from ..util import db_util
from ..util import input_util
from ..db import access_users


def execute():
    try:
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** ユーザ登録 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        rows = access_users.find_by_name_user(cursor, name)

        create_user(rows, cursor, name, cnx)

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


def create_user(rows, cursor, name, cnx):
    if len(rows) == 0:
        birthday = input_util.input_date("生年月日を入力してください [%Y-%m-%d] : ")

        access_users.create_user(cursor, name, birthday)
        cnx.commit()

        print()
        print("ユーザを登録しました")
    else:
        print()
        print("[Error] そのユーザー名はすでに存在します")


if __name__ == "__main__":
    execute()
