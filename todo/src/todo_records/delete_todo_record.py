import mysql.connector
import datetime
from ..util import db_util
from ..util import input_util
from ..db import access_users
from ..db import access_todo_records
from ..db.todo_record import TodoRecord
from ..util import print_util


def execute():
    try:
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** TODO削除 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        user = access_users.find_by_name(cursor, name)
        if user:
            deleting_todo_record_id = input_util.input_int(
                "削除するIDを入力してください : "
            )

            deleting_todo_record = access_todo_records.find_by_id(
                cursor, deleting_todo_record_id
            )
            if deleting_todo_record:
                deadline = input_util.change_deadline_to_empty_string(
                    deleting_todo_record.deadline
                )
                priority_str = input_util.change_priority_to_string(
                    deleting_todo_record.priority
                )

                deleting_todo_record_obj = TodoRecord(
                    id=deleting_todo_record.id,
                    user_id=user.id,
                    title=deleting_todo_record.title,
                    deadline=deadline,
                    priority=priority_str,
                )

                print_util.print_todo_record(deleting_todo_record_obj)
                print()

                is_confirm = input_util.is_confirm(
                    "削除してもよろしいですか？ [y/n] : "
                )
                if is_confirm:
                    access_todo_records.delete_todo_records(
                        cursor, deleting_todo_record_id
                    )

                    print("削除しました")
                else:
                    print("削除をキャンセルしました")
            else:
                print()
                print("[Error] そのユーザのTODOは記録されていません")
        else:
            print("[Error] そのユーザ名は存在しません")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    else:
        cnx.commit()

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
