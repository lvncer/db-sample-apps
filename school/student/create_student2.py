import mysql.connector
from ..util import dbutil
from ..util import inpututil
from ..db import dbaccess_student
from ..db.student import Student


def execute():
    try:
        # mysqlに接続
        cnx = dbutil.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 学生登録 ***")

        while True:
            id = inpututil.input_int("IDを入力してください: ")

            # 入力したIDがテーブルが存在するかチェック
            existing_student = dbaccess_student.find_by_id_student(cursor, id)
            if not existing_student:
                break

            print(f"ID={id}はすでに存在しています")

        name = inpututil.input_replace("氏名を入力してください : ")
        birthday = inpututil.input_date("生年月日を入力してください : ")
        clazz = inpututil.input_replace("クラスを入力してください : ")

        student_obj = Student(id=id, name=name, birthday=birthday, clazz=clazz)
        dbaccess_student.insert_student(cursor, student_obj)

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    else:
        cnx.commit()
        print(f"ID={id} を登録しました")

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
