import mysql.connector
from ..util import dbutil
from ..db import dbaccess_exam


def execute():
    try:
        # mysqlに接続
        cnx = dbutil.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 成績の全件表示 ***")

        exams = dbaccess_exam.select_all(cursor)
        if exams:
            for exam in exams:
                print(f"ID: {exam.id} 科目: {exam.subject} 成績: {exam.score}点")
        else:
            print("成績がありません")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
