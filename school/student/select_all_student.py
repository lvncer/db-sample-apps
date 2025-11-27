import mysql.connector
from ..util import dbutil
from ..db import dbaccess_student


def execute():
    try:
        # mysqlに接続
        cnx = dbutil.connect()
        cursor = cnx.cursor(dictionary=True)

        students = dbaccess_student.select_all(cursor)

        for student in students:
            print(f"{student.id} : {student.name} : {student.birthday} : {student.clazz}")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
