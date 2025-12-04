import mysql.connector
from ..util import db_util
from ..util import input_util
from ..db import access_users


def execute():
    try:
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** ユーザ情報検索 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        is_user_exists = access_users.find_by_name(cursor, name)
        if is_user_exists:
            user = is_user_exists
            print()
            print(f"ユーザ名: {user.name}")
            print(f"生年月日: {user.birthday}")
            print(f"身長: {user.height} cm")
            print(f"目標体重: {user.target_weight} kg")
            print()
        else:
            print("[Error] そのユーザ名は存在しません")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
