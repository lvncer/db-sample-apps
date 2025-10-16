import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from util import dbutil
from util import inpututil
from db import dbaccess_exam


def execute():
    try:
        # mysqlに接続
        cnx = dbutil.connect()
        print("*** 学生IDで成績検索 ***")

        id = inpututil.input_int("IDを入力してください : ")

        cursor = cnx.cursor(dictionary=True)

        rows = dbaccess_exam.find_by_id_exam(cursor, id)

        if len(rows) != 0:
            for row in rows:
                print(f"{row['id']}: {row['subject']} {row['score']}")
        else:
            print(f"ID={id}は見つかりません")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
