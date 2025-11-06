import mysql.connector
from ..util import dbutil
from ..util import inpututil
from ..db import dbaccess_student


def execute():
    try:
        # mysqlに接続
        cnx = dbutil.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 学生更新 ***")

        while True:
            id = inpututil.input_int("IDを入力してください: ")

            # 入力したIDがテーブルが存在するかチェック
            rows = dbaccess_student.find_by_id_student(cursor, id)

            if len(rows) != 0:
                break  # 入力したIDは存在する

            print(f"ID={id}は存在していません")

        name = inpututil.input_replace("氏名を入力してください: ")
        birthday = inpututil.input_date("生年月日を入力してください: ")
        clas = inpututil.input_replace("クラスを入力してください: ")

        result_confirm = inpututil.confirming("本当に更新してもよろしいでしょうか(Y/n)")

        if result_confirm:
            sql = """
                UPDATE student
                SET name = %s, birthday = %s, class = %s
                WHERE id = %s
                """

            data = [name, birthday, clas, id]
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
