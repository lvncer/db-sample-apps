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

        user = access_users.find_by_name(cursor, name)
        if not user:
            birthday = input_util.input_date("生年月日を入力してください [%Y-%m-%d] : ")

            access_users.create_user(cursor, name, birthday)

            print()
            print("ユーザを登録しました")
        else:
            print()
            print("[Error] そのユーザー名はすでに存在します")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    else:
        cnx.commit()

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
