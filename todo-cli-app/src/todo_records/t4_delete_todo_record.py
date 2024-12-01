# TODO削除プログラム
# 入力されたユーザ名のTODO記録を削除する

import os
import sys
import mysql.connector
import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util import db_util
from util import input_util
from db import access_users
from db import access_todo_records


def execute():
    try:
        # mysqlに接続
        cnx = db_util.connect()
        # カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        print("*** TODO削除 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # userテーブルに存在するかを確認する
        user_rows = access_users.find_by_name_user(cursor, name)

        # 削除する
        delete_todo_records(user_rows, cursor, cnx)

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 終了処理
    finally:
        cursor.close()
        cnx.close()


def delete_todo_records(user_rows, cursor, cnx):
    if len(user_rows) != 0:
        todo_id = input_util.input_int('削除するIDを入力してください : ')

        todo_id_rows = access_todo_records.find_by_id_todo(
            cursor, todo_id
        )

        # todo_recordsに記録がが一件以上存在するならば削除を開始する
        if len(todo_id_rows) != 0:
            for row in todo_id_rows:
                id = row['id']
                title = row['title']
                deadline = row['deadline']
                priority = row['priority']

                if deadline == datetime.date(9999, 12, 31):
                    deadline = ''

                priority = db_util.change_priority(priority)

                # 削除対象を表示
                print(f"id: {id}")
                print(f"日付: {deadline}")
                print(f"タイトル: {title}")
                print(f"優先度: {priority}")
                print()

            # 削除確認
            result_confirm = db_util.confirming(
                "削除してもよろしいですか？ [y/n] : "
            )
            print()

            if result_confirm:

                # 削除する
                access_todo_records.delete_todo_records(cursor, id)
                cnx.commit()

                print('削除しました')

            # nが入力されたならば削除をキャンセルする
            else:
                print("削除をキャンセルしました")

        # todo_recordsに記録が存在しないならば以下を実行する
        else:
            print()
            print("[Error] そのユーザのTODOは記録されていません")

    # usersテーブルにユーザが存在しないならば以下を実行する
    else:
        print("[Error] そのユーザ名は存在しません")


if __name__ == "__main__":
    execute()
