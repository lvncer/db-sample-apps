import mysql.connector
from ..util import db_util
from ..util import input_util
from ..db import access_users


def execute():
    try:
        # mysqlに接続
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 身長更新 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # 入力したユーザ名がテーブルが存在するかチェック
        rows = access_users.find_by_name_user(cursor, name)

        if len(rows) != 0:
            height = input_util.input_replace("身長を入力してください(cm) : ")

            result_confirm = input_util.confirming(
                "本当に更新してもよろしいでしょうか(Y/n)"
            )

            if result_confirm:
                # 指定された名前の身長を更新する
                access_users.update_height(cursor, name, height)

                cnx.commit()

                print()
                print("身長を更新しました")
                print()

            else:
                print("更新をキャンセルしました")

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
