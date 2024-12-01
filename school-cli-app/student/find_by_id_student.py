# 学生ID検索プログラム
# studentテーブルからキーボードで入力したIDを条件にレコードを取得して表示

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from util import dbutil
from util import inpututil
from db import dbaccess_student


def execute():
    # 1) 初期処理

    # mysqlに接続
    cnx = dbutil.connect()

    # 2) キーボードから入力させる

    print("*** 学生ID検索 ***")

    id = inpututil.input_int("IDを入力してください")

    # 4) sqlを実行する

    try:
        # カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        # 5) 取得したレコードを表示

        rows = dbaccess_student.find_by_id_student(cursor, id)

        if len(rows) != 0:
            for row in rows:
                print(f"{row['id']} : {row['name']}")
        else:
            print(f"ID={id}は見つかりません")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 6) 終了処理

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
