import mysql.connector
from ..util import dbutil
from ..util import inpututil
from ..db import dbaccess_student
from ..db import dbaccess_exam


def execute():
    try:
        # mysqlに接続
        cnx = dbutil.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 学生削除 ***")

        while True:
            id = inpututil.input_int("IDを入力してください: ")

            rows_student = dbaccess_student.find_by_id_student(cursor, id)
            if rows_student:
                break
            print(f"ID={id}は登録されていません")
            print("再入力してください")

        while True:
            subject = input("科目を入力してください: ")

            rows_exam = dbaccess_exam.find_by_id_and_subject(cursor, id, subject)
            if rows_exam:
                break
            print(f"ID={id}, subject={subject}は存在していません")

        # 削除対象の表示
        exam = dbaccess_exam.find_by_id_and_subject(cursor, id, subject)
        if exam:
            print(f"ID: {exam.id} 科目: {exam.subject} 成績: {exam.score}")

        result_confirm = inpututil.confirming("本当に削除してもよろしいでしょうか(Y/n)")
        if result_confirm:
            dbaccess_exam.delete_exam(cursor, id, subject)
        else:
            print("削除をキャンセルしました")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    else:
        cnx.commit()
        print(f"ID: {id} 科目: {subject} を削除しました")

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
