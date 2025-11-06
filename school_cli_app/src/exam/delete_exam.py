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

            # studentテーブルに該当するIDが存在しているかのチェック
            if len(rows_student) == 0:
                print(f"ID={id}は登録されていません")
                print("再入力してください")
                continue

            subject = input("科目を入力してください: ")

            rows = dbaccess_exam.update_score(cursor, id, subject)

            if len(rows) != 0:
                break  # 入力したsubjectは存在する

            # 入力したIDが存在しない
            print(f"ID={id}, subject={subject}は存在していません")

        # 削除対象の表示
        dbaccess_exam.pre_delete_showtable_exam(cursor, id, subject)

        result_confirm = inpututil.confirming("本当に削除してもよろしいでしょうか(Y/n)")

        if result_confirm:
            sql = "DELETE FROM exam WHERE id = %s"

            data = [id]
            cursor.execute(sql, data)
            cnx.commit()

            print(f"ID={id} を削除しました")

        else:
            print("削除をキャンセルしました")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
