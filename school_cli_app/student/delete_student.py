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

        print("*** 学生削除 ***")

        while True:
            id = inpututil.input_int("IDを入力してください: ")

            # 入力したIDがテーブルが存在するかチェック
            rows = dbaccess_student.find_by_id_student(cursor, id)

            if len(rows) != 0:
                break  # 入力したIDは存在しています

            print(f"ID={id}は存在していません")

        # 削除対象の表示
        dbaccess_student.pre_delete_showtable_school(cursor, id)

        result_confirm = dbutil.confirming("本当に削除してもよろしいでしょうか(Y/n)")

        if result_confirm:
            sql = "DELETE FROM student WHERE id = %s"

            data = [id]
            cursor.execute(sql, data)
            cnx.commit()

            print(f"ID={id} を削除しました")

        else:
            print("削除をキャンセルしました")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
