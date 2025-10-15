# 学生ID登録プログラム
# キーボードで入力した情報をstudentテーブルに登録する

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from util import dbutil
from util import inpututil
from db import dbaccess_student


def execute():
    # 1) 初期処理

    # mysqlに接続
    cnx = dbutil.connect()

    try:
        # カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        # 2) キーボードから入力させる

        print("*** 学生登録 ***")

        while True:
            id = inpututil.input_int("IDを入力してください: ")

            # 入力したIDがテーブルが存在するかチェック
            rows = dbaccess_student.find_by_id_student(cursor, id)

            if len(rows) == 0:
                break  # 入力したIDは存在しない

            # 入力したIDが存在する
            print(f"ID={id}はすでに存在しています")

        name = inpututil.input_replace("氏名を入力してください : ")
        birthday = inpututil.input_date("生年月日を入力してください : ")
        clas = inpututil.input_replace("クラスを入力してください : ")

        # 3) 登録sqlを作成

        # あとから設定したい値には%sに置き換える
        sql = "INSERT INTO student (id, name, birthday, class) VALUES (%s, %s, %s, %s)"

        # 設定したい値はリストにする
        data = [id, name, birthday, clas]

        # sqlを実行(SQLの文字列、値のリスト)
        cursor.execute(sql, data)

        # 5) 結果を表示

        cnx.commit()

        print(f"ID={id} を登録しました")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 6) 終了処理

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
