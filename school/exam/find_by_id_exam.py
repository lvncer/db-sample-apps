import mysql.connector
from ..util import dbutil
from ..util import inpututil
from ..db import dbaccess_exam


def execute():
    try:
        # mysqlに接続
        cnx = dbutil.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 学生IDで成績検索 ***")

        id = inpututil.input_int("IDを入力してください : ")
        exams = dbaccess_exam.find_by_id(cursor, id)
        if exams:
            for exam in exams:
                print(f"ID: {exam.id} 科目: {exam.subject} 成績: {exam.score}")
        else:
            print(f"ID: {id} は見つかりません")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
