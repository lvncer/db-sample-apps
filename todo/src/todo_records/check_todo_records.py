import mysql.connector
import datetime

from todo.src import todo_records
from ..util import db_util
from ..util import input_util
from ..db import access_users
from ..db import access_todo_records


def execute():
    try:
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** TODO完了確認 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        user = access_users.find_by_name(cursor, name)
        check_todo_records(cursor, user)

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    else:
        cnx.commit()

    finally:
        cursor.close()
        cnx.close()


def check_todo_records(cursor, user):
    if user:
        todo_id = input_util.input_int("完了したtodoのIDを入力してください : ")

        todo_record = access_todo_records.find_by_id(cursor, todo_id)
        if todo_record:
            id = todo_record.id
            title = todo_record.title
            deadline = todo_record.deadline
            priority = todo_record.priority
            name = user.name

            deadline = input_util.change_deadline_to_empty_string(deadline)
            priority_str, get_experience = (
                input_util.change_priority_to_string_get_experience(priority)
            )

            print()
            print(f"id: {id}")
            print(f"日付: {deadline}")
            print(f"タイトル: {title}")
            print(f"優先度: {priority_str}")
            print()

            result_confirm = input_util.is_confirm("完了しましたか？ [y/n] : ")
            print()
            if result_confirm:
                access_users.update_experience(cursor, name, get_experience)
                access_todo_records.delete_todo_records(cursor, id)

                print(f"{get_experience} 経験値入手しました!")
            else:
                print("完了確認をキャンセルしました")
        else:
            print()
            print("[Error] そのidのTODOは記録されていません")
    else:
        print("[Error] そのユーザ名は存在しません")


if __name__ == "__main__":
    execute()
