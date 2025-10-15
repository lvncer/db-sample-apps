# ユーザ削除プログラム
# キーボードで入力した情報をusersテーブルから削除する

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from util import db_util
from util import input_util
from db import access_users
from db import access_weight_records


def execute():
    try:
        # mysqlに接続
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** ユーザ削除 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # 入力したIDがテーブルが存在するかチェック
        rows = access_users.find_by_name_user(cursor, name)

        if len(rows) != 0:
            # 削除対象の表示
            for row in rows:
                print()
                print(f"ユーザ名: {row['name']}")
                print(f"生年月日: {row['birthday']}")
                print(f"身長: {row['height']} cm")
                print(f"目標体重: {row['target_weight']} kg")
                print()

            # 該当するユーザ名の体重記録を取得する
            record_rows = access_users.find_weight_records(cursor, name)

            print(f"体重記録: {len(record_rows)}件")
            print()

            # 削除確認
            result_confirm = db_util.confirming(
                "このデータをすべて削除してもよろしいですか？(y/n): "
            )

            if result_confirm:
                # 削除するユーザ名からweight_recordsテーブルのidを取得する
                delete_id = access_users.find_id_by_name(cursor, name)

                # weight_recordsテーブルから指定されたユーザの体重記録を削除する
                access_weight_records.delete_records(cursor, delete_id)

                # 指定された名前のユーザをusersテーブルから削除する
                access_users.delete_user(cursor, name)

                cnx.commit()

                print("削除しました")
                print()

            else:
                print("削除をキャンセルしました")
                print()

        else:
            print("[Error] そのユーザ名は存在しません")
            print()

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
