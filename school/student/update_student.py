import mysql.connector
from ..util import dbutil
from ..util import inpututil
from ..db import dbaccess_student
from ..db import student


def execute():
    try:
        # mysqlに接続
        cnx = dbutil.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 学生更新 ***")

        while True:
            id = inpututil.input_int("IDを入力してください: ")

            # 入力したIDがテーブルが存在するかチェック
            existing_student = dbaccess_student.find_by_id_student(cursor, id)
            if existing_student:
                break

            print(f"ID={id}は存在していません")

        name = inpututil.input_replace("氏名を入力してください: ")
        birthday = inpututil.input_date("生年月日を入力してください: ")
        clas = inpututil.input_replace("クラスを入力してください: ")

        result_confirm = inpututil.confirming("本当に更新してもよろしいでしょうか(Y/n)")

        if result_confirm:
            student_obj = student.Student(
                id=id, name=name, birthday=birthday, clazz=clas
            )
            dbaccess_student.update_student(cursor, student_obj)
        else:
            print("更新をキャンセルしました")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    else:
        cnx.commit()
        print(f"ID: {id} を更新しました")

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
