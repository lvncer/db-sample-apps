# 目標体重更新プログラム
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

        print("*** 目標体重更新 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # 入力したIDがテーブルが存在するかチェック
        rows = access_users.find_by_name_user(cursor, name)

        # 存在していれば更新手続きを開始する
        if len(rows) != 0:

            target_weight = input_util.input_replace("目標体重を入力してください(kg) : ")

            # 更新確認（Yを入力すると更新が確定される)
            result_confirm = db_util.confirming("本当に更新してもよろしいでしょうか(Y/n)")

            # Yが入力されたならば以下を実行する
            if result_confirm:

                access_users.update_target_weight(cursor, target_weight, name)

                # 5) 結果を表示
                cnx.commit()

                print("目標体重を更新しました")
                print()

            # nが入力されたならば以下を実行する
            else:
                print("更新をキャンセルしました")
                print()

        # 入力したユーザが存在しないので更新をキャンセルする
        else:
            print("[Error] そのユーザ名は存在しません")
            print()

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 6) 終了処理

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
