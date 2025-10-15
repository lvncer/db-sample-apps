# 学生ID削除プログラム
# キーボードで入力した情報をstudentテーブルから削除する

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

        print("*** 学生削除 ***")

        while True:
            id = inpututil.input_int("IDを入力してください: ")

            # 入力したIDがテーブルが存在するかチェック
            rows = dbaccess_student.find_by_id_student(cursor, id)

            if len(rows) != 0:
                break  # 入力したIDは存在しています

            # 入力したIDが存在しない
            print(f"ID={id}は存在していません")

        # 削除対象の表示
        dbaccess_student.pre_delete_showtable_school(cursor, id)

        # 削除確認（Yを入力すると削除が確定される)
        result_confirm = dbutil.confirming("本当に削除してもよろしいでしょうか(Y/n)")

        # Yが入力されたならば以下を実行する
        if result_confirm:
            # 3) 削除sqlを作成
            # あとから設定したい値には%sに置き換える
            sql = "DELETE FROM student WHERE id = %s"

            # 設定したい値はリストにする
            data = [id]

            # sqlを実行(SQLの文字列、値のリスト)
            cursor.execute(sql, data)

            # 5) 結果を表示

            cnx.commit()

            print(f"ID={id} を削除しました")

        # nが入力されたならば以下を実行する
        else:
            print("削除をキャンセルしました")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 6) 終了処理

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
