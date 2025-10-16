import mysql.connector
from ..util import dbutil
from ..util import inpututil
from ..db import dbaccess_student


def execute():
    try:
        # mysqlに接続
        cnx = dbutil.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 学生登録 ***")

        while True:
            id = inpututil.input_int("IDを入力してください: ")

            # 入力したIDがテーブルが存在するかチェック
            rows = dbaccess_student.find_by_id_student(cursor, id)

            if len(rows) == 0:
                break  # 入力したIDは存在しない

            print(f"ID={id}はすでに存在しています")

        name = inpututil.input_replace("氏名を入力してください : ")
        birthday = inpututil.input_date("生年月日を入力してください : ")
        clas = inpututil.input_replace("クラスを入力してください : ")

        sql = "INSERT INTO student (id, name, birthday, class) VALUES (%s, %s, %s, %s)"

        data = [id, name, birthday, clas]
        cursor.execute(sql, data)
        cnx.commit()

        print(f"ID={id} を登録しました")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
