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

        print("*** 成績更新 ***")

        while True:
            id = inpututil.input_int("IDを入力してください: ")

            rows_student = dbaccess_student.find_by_id_student(cursor, id)

            # studentテーブルに該当するIDが存在しているかのチェック
            if len(rows_student) == 0:
                print(f"ID={id}は登録されていません")
                print("再入力してください")
                continue

            subject = input("科目を入力してください: ")

            rows = dbaccess_exam.update_score(cursor, id, subject)

            if len(rows) != 0:
                break  # 入力したsubjectは存在する

            print(f"subject={subject}は存在していません")

        # 入力されたIDと科目の組み合わせが既に存在しているかをチェック
        while True:
            change_subject = input("変更後の名を入力してください。")
            rows_exam = dbaccess_exam.update_score(cursor, id, change_subject)
            if len(rows_exam) != 0 and change_subject != subject:
                print(
                    f"ID={id} と科目={change_subject}の組み合わせは既に存在しています"
                )
                print("再入力してください")
                continue
            break

        score = inpututil.input_int("成績を入力してください: ")

        result_confirm = inpututil.confirming("本当に更新してもよろしいでしょうか(Y/n)")

        if result_confirm:
            sql = """
            UPDATE exam
            SET subject = %s, score = %s
            WHERE id = %s AND subject = %s
            """

            data = [change_subject, score, id, subject]
            cursor.execute(sql, data)
            cnx.commit()

            print(f"ID={id} を更新しました")

        else:
            print("更新をキャンセルしました")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
