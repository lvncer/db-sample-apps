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

        print("*** 成績更新 ***")

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
            print(f"subject={subject}は存在していません")

        while True:
            change_subject = input("変更後の科目名を入力してください。")

            rows_exam = dbaccess_exam.find_by_id_and_subject(cursor, id, change_subject)
            if rows_exam and change_subject != subject:
                print(
                    f"ID: {id} と科目=: {change_subject} の組み合わせは既に存在しています"
                )
                print("再入力してください")
                continue
            break

        score = inpututil.input_int("成績を入力してください: ")

        result_confirm = inpututil.confirming("本当に更新してもよろしいでしょうか(Y/n)")

        if result_confirm:
            exam_obj = exam.Exam(id=id, subject=change_subject, score=score)
            dbaccess_exam.update_exam(cursor, exam_obj)
        else:
            print("更新をキャンセルしました")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    else:
        cnx.commit()
        print(f"ID={id} を更新しました")

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
