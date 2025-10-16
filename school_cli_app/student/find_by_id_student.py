import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from util import dbutil
from util import inpututil
from db import dbaccess_student


def execute():
    try:
        # mysqlに接続
        cnx = dbutil.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 学生ID検索 ***")

        id = inpututil.input_int("IDを入力してください")

        rows = dbaccess_student.find_by_id_student(cursor, id)

        if len(rows) != 0:
            for row in rows:
                print(f"{row['id']} : {row['name']}")
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
