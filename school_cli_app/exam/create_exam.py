import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from util import dbutil
from util import inpututil
from db import dbaccess_student
from db import dbaccess_exam


def execute():
    try:
        # mysqlに接続
        cnx = dbutil.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 学生登録 ***")

        while True:
            id = inpututil.input_int("IDを入力してください: ")

            rows_student = dbaccess_student.find_by_id_student(cursor, id)

            # studentテーブルに該当するIDが存在しているかのチェック
            if len(rows_student) == 0:
                # 存在してないので再入力させる
                print(f"ID={id}は登録されていません")
                print("再入力してください")
                continue

            subject = input("科目を入力してください: ")

            # 入力したIDがテーブルが存在するかチェック
            rows = dbaccess_exam.update_score(cursor, id, subject)

            if len(rows) == 0:
                break  # 入力したsubjectは存在しない

            # 入力したIDが存在しない
            print(f"ID={id}, 科目={subject}はすでに存在しています")

        score = inpututil.input_int("成績を入力してください: ")

        sql = "INSERT INTO exam (id, subject, score) VALUES (%s, %s, %s)"

        data = [id, subject, score]
        cursor.execute(sql, data)
        cnx.commit()

        print(f"ID={id} を登録しました")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
