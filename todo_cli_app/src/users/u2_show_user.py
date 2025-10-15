# ユーザ表示プログラム
# 入力されたユーザ名をusersテーブルからレコードを取得して表示

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

        print("*** ユーザ表示 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # 入力したユーザ名がテーブルが存在するかチェック
        rows = access_users.find_by_name_user(cursor, name)

        # 表示する
        show_user(rows)

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


def show_user(rows):
    if len(rows) != 0:
        for row in rows:
            print()
            print(f"ユーザ名: {row['name']}")
            print(f"生年月日: {row['birthday']}")
            print(f"経験値: {row['experience']}")
            print(f"敵撃破状況: {row['progress'] - 1} 体")

    else:
        print("[Error] そのユーザ名は存在しません")


if __name__ == "__main__":
    execute()
