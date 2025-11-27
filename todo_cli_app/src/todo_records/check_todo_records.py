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

        print("*** TODO完了確認 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # userテーブルに存在するかを確認する
        user_rows = access_users.find_by_name_user(cursor, name)

        # チェックして削除する
        check_todo_records(user_rows, cursor, name, cnx)

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 終了処理
    finally:
        cursor.close()
        cnx.close()


def check_todo_records(user_rows, cursor, name, cnx):
    if len(user_rows) != 0:
        todo_id = input_util.input_int('完了したtodoのIDを入力してください : ')

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

                if priority == 1:
                    priority = '高'
                    get_experience = 30
                elif priority == 2:
                    priority = '中'
                    get_experience = 20
                elif priority == 3:
                    priority = '低'
                    get_experience = 10

                # 削除対象を表示
                print(f"id: {id}")
                print(f"日付: {deadline}")
                print(f"タイトル: {title}")
                print(f"優先度: {priority}")
                print()

            # 削除確認（Yを入力すると削除が確定される)
            result_confirm = db_util.confirming(
                "完了しましたか？ [y/n] : "
            )
            print()

            # Yが入力されたならば削除を確定する
            if result_confirm:
                # ユーザレベルの更新
                access_users.update_experience(
                    cursor, name, get_experience
                )

                # 削除を確定する
                access_todo_records.delete_todo_records(
                    cursor, id
                )

                cnx.commit()

                print(f'{get_experience} 経験値入手しました!')

            # nが入力されたならば削除をキャンセルする
            else:
                print("完了確認をキャンセルしました")

        # todo_recordsにtodo記録が存在しないならば以下を実行する
        else:
            print()
            print("[Error] そのidのTODOは記録されていません")

    # usersテーブルにユーザが存在しないならば以下を実行する
    else:
        print("[Error] そのユーザ名は存在しません")


if __name__ == "__main__":
    execute()
