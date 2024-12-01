# 学生成績更新プログラム
# キーボードで入力した情報をexamテーブルに更新する

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from util import dbutil
from util import inpututil
from db import dbaccess_student
from db import dbaccess_exam


def execute():
    # 1) 初期処理

    # mysqlに接続
    cnx = dbutil.connect()

    try:
        # カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        # 2) キーボードから入力させる

        print("*** 成績更新 ***")

        while True:
            id = inpututil.input_int("IDを入力してください: ")

            rows_student = dbaccess_student.find_by_id_student(cursor, id)

            # studentテーブルに該当するIDが存在しているかのチェック
            if len(rows_student) == 0:
                # 存在してないので再入力させる
                print(f"ID={id}は登録されていません")
                print("再入力してください")
                continue

            subject = input("科目を入力してください: ")

            rows = dbaccess_exam.update_score(cursor, id, subject)

            if len(rows) != 0:
                break  # 入力したsubjectは存在する

            # 入力したIDが存在しない
            print(f"subject={subject}は存在していません")

        score = inpututil.input_int("成績を入力してください: ")

        # 更新確認（Yを入力すると更新が確定される)
        result_confirm = dbutil.confirming("本当に更新してもよろしいでしょうか(Y/n)")

        # Yが入力されたならば以下を実行する
        if result_confirm:
            # 3) 更新sqlを作成
            # あとから設定したい値には%sに置き換える
            sql = "UPDATE exam SET score = %s WHERE id = %s AND subject = %s"

            # 設定したい値はリストにする
            data = [score, id, subject]

            # sqlを実行(SQLの文字列、値のリスト)
            cursor.execute(sql, data)

            # 5) 結果を表示

            cnx.commit()

            print(f"ID={id} を更新しました")

        # nが入力されたならば以下を実行する
        else:
            print("更新をキャンセルしました")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 6) 終了処理

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
