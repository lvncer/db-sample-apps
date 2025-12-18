import mysql.connector
from ..util import db_util
from ..util import input_util
from ..db import access_users
from ..db import access_todo_records
from ..db.todo_record import TodoRecord


def execute():
    try:
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** TODO記録 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        user = access_users.find_by_name(cursor, name)
        if user:
            title = input("タイトルを入力してください : ")
            deadline = input_util.input_deadline(
                "(任意)期日を入力してください[%Y-%m-%d] : "
            )
            priority = input_util.input_priority(
                "優先度(1:高 2:中 3:低)を入力してください : "
            )

            todo_record = TodoRecord(
                id=None,
                user_id=user.id,
                title=title,
                deadline=deadline,
                priority=priority,
            )
            access_todo_records.insert_todo_records(cursor, todo_record)

            print()
            print("TODOを記録しました")
        else:
            print()
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
