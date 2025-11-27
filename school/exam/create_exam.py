import mysql.connector
from ..util import dbutil
from ..util import inpututil
from ..db import dbaccess_student
from ..db import dbaccess_exam
from ..db import exam


def execute():
    try:
        # mysqlに接続
        cnx = dbutil.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 学生登録 ***")

        while True:
            id = inpututil.input_int("IDを入力してください: ")

            rows_student = dbaccess_student.find_by_id_student(cursor, id)
            if not rows_student:
                print(f"ID={id}は登録されていません")
                print("再入力してください")
                continue
            break

        while True:
            subject = input("科目を入力してください: ")

            rows_exam = dbaccess_exam.find_by_id_and_subject(cursor, id, subject)
            if not rows_exam:
                break
            print(f"ID={id}, 科目={subject}はすでに存在しています")

        score = inpututil.input_int("成績を入力してください: ")

        exam_obj = exam.Exam(id=id, subject=subject, score=score)
        dbaccess_exam.insert_exam(cursor, exam_obj)

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
