import mysql.connector
from ..util import db_util
from ..util import input_util
from ..db import access_users
from ..db import access_todo_records
from ..util import print_util


def execute():
    try:
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** ユーザ削除 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        user = access_users.find_by_name(cursor, name)
        if user:
            print_util.print_user(user)

            todo_records = access_todo_records.find_by_user_id(cursor, user.id)

            print(f"TODO: {len(todo_records)}件")
            print()

            is_confirm = input_util.is_confirm(
                "このデータを全て削除してもよろしいですか？(y/n): "
            )
            if is_confirm:
                access_todo_records.delete_by_user_id_todo_records(cursor, user.id)
                access_users.delete_user(cursor, name)

                print()
                print("削除しました")
            else:
                print()
                print("削除をキャンセルしました")
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
