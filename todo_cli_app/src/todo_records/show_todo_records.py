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

        print("*** TODO表示 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # userテーブルに存在するかを確認する
        user_rows = access_users.find_by_name_user(cursor, name)

        # 表示する
        show_todo_record(user_rows, cursor)

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


def show_todo_record(user_rows, cursor):
    if len(user_rows) != 0:
        print("並び順")
        print("1: 優先度高い順")
        print("2: 期限短い順")
        print("を入力してください: ", end="")

        sort_prompt = input_util.input_sort_order()

        user_id = user_rows[0]["id"]

        # 該当するすべてのレコードを取得する
        todo_rows = access_todo_records.find_by_user_id_todo_records(
            cursor, user_id, sort_prompt
        )

        if len(todo_rows) != 0:
            print("-- TODO(最大5件) --")

            for row in todo_rows:
                id = row["id"]
                title = row["title"]
                deadline = row["deadline"]
                priority = row["priority"]

                # deadlineが9999/12/31なら空文字にする
                if deadline == datetime.date(9999, 12, 31):
                    deadline = ""

                # priorityを数値から文字に変換する
                priority = db_util.change_priority(priority)

                # 結果を表示
                print()
                print(f"id: {id}")
                print(f"タイトル: {title}")
                print(f"日付: {deadline}")
                print(f"優先度: {priority}")

            # 表示した件数の合計を最後に表示する
            print()
            print(f"{len(todo_rows)}件表示しました")

        # todo_recordsに記録が存在しないなら表示しない
        else:
            print()
            print("[Error] そのユーザのTODOは記録されていません")

    # usersテーブルにユーザが存在しないならば以下を実行する
    else:
        print("[Error] そのユーザ名は存在しません")


if __name__ == "__main__":
    execute()
