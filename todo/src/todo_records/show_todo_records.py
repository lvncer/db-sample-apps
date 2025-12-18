import mysql.connector
import datetime
from ..util import db_util
from ..util import input_util
from ..db import access_users
from ..db import access_todo_records
from ..util import print_util
from ..db.todo_record import TodoRecord


def execute():
    try:
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** TODO表示 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        user = access_users.find_by_name(cursor, name)
        if user:
            print("並び順")
            print("1: 優先度高い順")
            print("2: 期限短い順")
            print("を入力してください: ", end="")

            sort_prompt = input_util.input_sort_order()

            user_id = user.id
            todo_records = access_todo_records.find_by_user_id_sort_order(
                cursor, user_id, sort_prompt
            )
            if todo_records:
                print("-- TODO(最大5件) --")

                for todo_record in todo_records:
                    deadline = input_util.change_deadline_to_empty_string(
                        todo_record.deadline
                    )
                    priority_str = input_util.change_priority_to_string(
                        todo_record.priority
                    )

                    todo_record_obj = TodoRecord(
                        id=todo_record.id,
                        user_id=user_id,
                        title=todo_record.title,
                        deadline=deadline,
                        priority=priority_str,
                    )

                    print()
                    print_util.print_todo_record(todo_record_obj)
                print()
                print(f"{len(todo_records)}件表示しました")
            else:
                print()
                print("[Error] そのユーザのTODOは記録されていません")
        else:
            print("[Error] そのユーザ名は存在しません")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
