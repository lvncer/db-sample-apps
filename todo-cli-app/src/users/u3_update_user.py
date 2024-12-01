# ユーザ更新プログラム
# 入力されたユーザ情報をusersテーブルに更新する

import os
import sys
import mysql.connector

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util import db_util
from util import input_util
from db import access_users


def execute():
    try:
        # mysqlに接続
        cnx = db_util.connect()
        # カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        print("*** ユーザ更新 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # 入力したIDがテーブルが存在するかチェック
        rows = access_users.find_by_name_user(cursor, name)

        # 更新する
        update_user(rows, cursor, name, cnx)

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 終了処理
    finally:
        cursor.close()
        cnx.close()


def update_user(rows, cursor, name, cnx):
    if len(rows) != 0:

        birthday = input_util.input_date("生年月日を入力してください[%Y-%m-%d] : ")

        # 指定されたユーザ名の生年月日を更新する
        access_users.update_birthday(cursor, birthday, name)

        cnx.commit()

        print()
        print("ユーザを更新しました")

    else:
        print("[Error] そのユーザ名は存在しません")


if __name__ == "__main__":
    execute()
