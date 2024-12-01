# 身長更新プログラム
# キーボードで入力した情報をusersテーブルに更新する

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from util import db_util
from util import input_util
from db import access_users


def execute():
    # mysqlに接続
    cnx = db_util.connect()

    try:
        # カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        print("*** 身長更新 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # 入力したIDがテーブルが存在するかチェック
        rows = access_users.find_by_name_user(cursor, name)

        # 存在していれば更新手続きを開始する
        if len(rows) != 0:

            height = input_util.input_replace("身長を入力してください(cm) : ")

            # 更新確認（Yを入力すると更新が確定される)
            result_confirm = db_util.confirming("本当に更新してもよろしいでしょうか(Y/n)")

            # Yが入力されたならば以下を実行する
            if result_confirm:
                # 指定された名前の身長を更新する
                access_users.update_height(cursor, name, height)

                # 結果を反映させる
                cnx.commit()

                print()
                print("身長を更新しました")
                print()

            # nが入力されたならば以下を実行する
            else:
                print("更新をキャンセルしました")

        else:
            print("[Error] そのユーザ名は存在しません")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 6) 終了処理

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
