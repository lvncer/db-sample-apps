import mysql.connector
import datetime
from ..util import db_util
from ..util import input_util
from ..db import access_users
from ..db import access_todo_records


def execute():
    try:
        # mysqlに接続
        cnx = db_util.connect()
        # カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        print("*** TODO更新 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # userテーブルに存在するかを確認する
        user_rows = access_users.find_by_name_user(cursor, name)

        # 更新する
        update_todo_records(user_rows, cursor, cnx)

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 終了処理
    finally:
        cursor.close()
        cnx.close()


def update_todo_records(user_rows, cursor, cnx):
    if len(user_rows) != 0:
        todo_id = input_util.input_int('更新するIDを入力してください : ')

        # 更新するユーザのTODO記録のレコードを取得する
        todo_id_rows = access_todo_records.find_by_id_todo(
            cursor, todo_id
        )

        # todo_recordsに記録がが一件以上存在するならば更新を開始する
        if len(todo_id_rows) != 0:
            for row in todo_id_rows:
                id = row['id']
                title = row['title']
                deadline = row['deadline']
                priority = row['priority']

                if deadline == datetime.date(9999, 12, 31):
                    deadline = ''

                priority = db_util.change_priority(priority)

                # 更新するTODOを表示
                print(f"id: {id}")
                print(f"タイトル: {title}")
                print(f"日付: {deadline}")
                print(f"優先度: {priority}")
                print()

            # 必要な情報を入力させる
            title = input('タイトルを入力してください : ')
            deadline = input_util.input_deadline(
                '(任意)期日を入力してください[%Y-%m-%d] : '
            )
            priority = input_util.input_priority(
                '優先度(1:高 2:中 3:低)を入力してください : '
            )
            print()

            # 削除確認
            result_confirm = db_util.confirming(
                "更新してもよろしいですか？ (y/n): "
            )

            # Yが入力されたならば削除を確定する
            if result_confirm:

                # 更新を確定する
                access_todo_records.update_todo_records(
                    cursor, id, title, deadline, priority
                )
                cnx.commit()

                print()
                print('更新しました')

            # nが入力されたならば更新をキャンセルする
            else:
                print("更新をキャンセルしました")
                print()

        # todo_recordsに記録が存在しないならば更新しない
        else:
            print()
            print("[Error] そのユーザのTODOは記録されていません")

    # usersテーブルにユーザが存在しないならば以下を実行する
    else:
        print("[Error] そのユーザ名は存在しません")


if __name__ == "__main__":
    execute()
