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

        print("*** ユーザ削除 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # 入力した名前のユーザがテーブルが存在するかチェック
        user_rows = access_users.find_by_name_user(cursor, name)

        # 削除する
        delete_user(user_rows, cursor, name, cnx)

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


def delete_user(user_rows, cursor, name, cnx):
    if len(user_rows) != 0:

        # 削除対象の表示
        for row in user_rows:
            print()
            print(f"ユーザ名: {row['name']}")
            print(f"生年月日: {row['birthday']}")
            print(f"経験値: {row['experience']}")
            print(f"敵撃破状況: {row['birthday']} 体")
            print()

        # 該当するユーザ名のTODO記録を取得する
        record_rows = access_todo_records.find_by_user_id(cursor, user_rows[0]["id"])

        # TODO記録の件数を表示する
        print(f"TODO: {len(record_rows)}件")
        print()

        # 削除確認
        result_confirm = db_util.confirming(
            "このデータを全て削除してもよろしいですか？(y/n): "
        )

        # Yが入力されたならば削除を確定する
        if result_confirm:

            access_todo_records.delete_by_user_id_todo_records(
                cursor, user_rows[0]["id"]
            )

            # 指定された名前のユーザをusersテーブルから削除する
            access_users.delete_user(cursor, name)

            cnx.commit()

            print()
            print("削除しました")

        else:
            print()
            print("削除をキャンセルしました")

    else:
        print()
        print("[Error] そのユーザ名は存在しません")


if __name__ == "__main__":
    execute()
