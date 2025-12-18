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

        print("*** TODO更新 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        user = access_users.find_by_name(cursor, name)
        if user:
            todo_id = input_util.input_int("更新するIDを入力してください : ")

            todo_record = access_todo_records.find_by_id(cursor, todo_id)
            if todo_record:
                deadline = input_util.change_deadline_to_empty_string(
                    todo_record.deadline
                )
                priority_str = input_util.change_priority_to_string(
                    todo_record.priority
                )

                todo_record_obj = TodoRecord(
                    id=todo_record.id,
                    user_id=user.id,
                    title=todo_record.title,
                    deadline=deadline,
                    priority=priority_str,
                )

                print_util.print_todo_record(todo_record_obj)

                new_title = input("タイトルを入力してください : ")
                new_deadline = input_util.input_deadline(
                    "(任意)期日を入力してください[%Y-%m-%d] : "
                )
                new_priority = input_util.input_priority(
                    "優先度(1:高 2:中 3:低)を入力してください : "
                )

                print()

                new_todo_record_obj = TodoRecord(
                    id=todo_record.id,
                    user_id=user.id,
                    title=new_title,
                    deadline=new_deadline,
                    priority=new_priority,
                )

                is_confirm = input_util.is_confirm("更新してもよろしいですか？ (y/n): ")
                if is_confirm:
                    access_todo_records.update_todo_records(cursor, new_todo_record_obj)

                    print()
                    print("更新しました")
                else:
                    print("更新をキャンセルしました")
                    print()
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
