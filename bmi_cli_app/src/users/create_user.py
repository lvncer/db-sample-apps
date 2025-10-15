import mysql.connector

from ..util import db_util
from ..util import input_util
from ..db import access_users


def execute():
    try:
        # mysqlに接続
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** ユーザ登録 ***")

        name = input_util.input_replace("ユーザ名を入力してください: ")

        # 入力したユーザ名がテーブルが存在するかチェック
        rows = access_users.find_by_name_user(cursor, name)

        # 存在していなければ新規で登録する
        if len(rows) == 0:
            birthday = input_util.input_date("生年月日を入力してください [%Y-%m-%d] : ")
            height = input_util.input_int("身長を入力してください(cm) : ")
            target_weight = input_util.input_int("目標体重を入力してください(kg) : ")

            access_users.create_user(cursor, name, birthday, height, target_weight)

            cnx.commit()

            print()
            print("ユーザを登録しました")
            print()

        # 存在していた場合は登録をキャンセルする
        else:
            print("[Error] そのユーザー名はすでに存在します")
            print()

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
