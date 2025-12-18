import mysql.connector
from ..util import db_util
from ..util import input_util
from ..db import access_users
from ..util import print_util


def execute():
    try:
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** ユーザ表示 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")
        user = access_users.find_by_name(cursor, name)

        print_util.print_user(user)

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
