import mysql.connector
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

        print('*** TODO記録 ***')

        name = input_util.input_replace('ユーザ名を入力してください : ')

        # 入力したユーザ名がusersテーブルに存在しているか確認
        rows = access_users.find_by_name_user(cursor, name)

        # 登録する
        create_todo_record(rows, cursor, cnx)

    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)

    # 終了処理
    finally:
        cursor.close()
        cnx.close()


def create_todo_record(rows, cursor, cnx):
    if len(rows) != 0:

        # 必要な情報を入力させる
        title = input('タイトルを入力してください : ')
        deadline = input_util.input_deadline(
            '(任意)期日を入力してください[%Y-%m-%d] : '
        )
        priority = input_util.input_priority(
            '優先度(1:高 2:中 3:低)を入力してください : '
        )

        user_id = rows[0]['id']

        # sqlを実行してデータベースに登録する
        access_todo_records.insert_todo_records(
            cursor, user_id, title, deadline, priority
        )

        cnx.commit()

        print()
        print('TODOを記録しました')

    # 存在しない場合は登録をキャンセルする
    else:
        print()
        print("[Error] そのユーザ名は存在しません")


if __name__ == '__main__':
    execute()
