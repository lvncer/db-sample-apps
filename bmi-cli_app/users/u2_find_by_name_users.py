# ユーザ検索プログラム
# usersテーブルからキーボードで入力したユーザ名を条件にレコードを取得して表示

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

        text = []

        print("*** ユーザ情報検索 ***")

        # 2) キーボードから入力させる
        name = input_util.input_replace("ユーザ名を入力してください : ")

        # 4) sqlを実行する
        rows = access_users.find_by_name_user(cursor, name)

        # 5) 取得したレコードを表示
        if len(rows) != 0:
            for row in rows:
                print()

                # ユーザ情報をリストに追加する
                text.append(f"ユーザ名: {row['name']}")
                text.append(f"生年月日: {row['birthday']}")
                text.append(f"身長: {row['height']} cm")
                text.append(f"目標体重: {row['target_weight']} kg")

                # リストから音声を再生する
                db_util.play_sound(text)
                print()

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
