import mysql.connector
from ..util import dbutil
from ..util import inpututil
from ..db import dbaccess_student


def execute():
    try:
        # mysqlに接続
        cnx = dbutil.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 学生削除 ***")

        while True:
            id = inpututil.input_int("IDを入力してください: ")

            # 入力したIDがテーブルが存在するかチェック
            student = dbaccess_student.find_by_id_student(cursor, id)
            if student:
                break

            print(f"ID={id}は存在していません")

        # 削除対象の表示
        student = dbaccess_student.find_by_id_student(cursor, id)
        if student:
            print(f"ID={student['id']} : ", end=" ")
            print(f"name={student['name']} : ", end=" ")
            print(f"birthday={student['birthday']} :", end=" ")
            print(f"class={student['class']}")

        result_confirm = inpututil.confirming("本当に削除してもよろしいでしょうか(Y/n)")

        if result_confirm:
            sql = "DELETE FROM student WHERE id = %s"

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
