# 学生表示プログラム
# studentテーブルからすべてのレコードを取得して表示

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from util import dbutil


def execute():
    # 1) 初期処理

    # mysqlに接続
    cnx = dbutil.connect()

    # 2) 検索用sqlを作成

    sql = "SELECT * FROM student ORDER BY id"

    # 3) sqlを実行する

    try:
        # カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        # sqlを実行
        cursor.execute(sql)

        # 4) 取得したレコードを全て表示

        rows = cursor.fetchall()

        for row in rows:
            print(f"{row['id']} : {row['name']}")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 5) 終了処理

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
