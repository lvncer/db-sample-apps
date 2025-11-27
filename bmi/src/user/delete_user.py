import mysql.connector
from ..util import db_util
from ..util import input_util
from ..db import access_users
from ..db import access_weight_records


def execute():
    try:
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** ユーザ削除 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        deleting_user_obj = access_users.find_by_name(cursor, name)

        if deleting_user_obj:
            # 削除対象の表示
            print()
            print(f"ユーザ名: {deleting_user_obj.name}")
            print(f"生年月日: {deleting_user_obj.birthday}")
            print(f"身長　　: {deleting_user_obj.height} cm")
            print(f"目標体重: {deleting_user_obj.target_weight} kg")
            print()

            record_rows = access_weight_records.find_by_user_id(cursor, deleting_user_obj.id)

            print(f"体重記録: {len(record_rows)}件")
            print()

            is_delete_confirm = input_util.confirming(
                "このデータをすべて削除してもよろしいですか？(y/n): "
            )

            if is_delete_confirm:
                deleting_id = access_users.find_by_name(cursor, name).id

                access_weight_records.delete_records(cursor, deleting_id)
                access_users.delete_user(cursor, deleting_id)
                cnx.commit()

                print("削除しました")
                print()
            else:
                print("削除をキャンセルしました")
                print()

        else:
            print("[Error] そのユーザ名は存在しません")
            print()

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
