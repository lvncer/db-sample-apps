import mysql.connector
from ..util import db_util
from ..util import input_util
from ..db import access_users
from ..db import user


def execute():
    try:
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** ユーザ登録 ***")

        name = input_util.input_replace("ユーザ名を入力してください: ")

        is_input_user_exists = access_users.find_by_name_user(cursor, name)

        if not is_input_user_exists:
            birthday = input_util.input_date("生年月日を入力してください [%Y-%m-%d] : ")
            height = input_util.input_int("身長を入力してください(cm) : ")
            target_weight = input_util.input_int("目標体重を入力してください(kg) : ")

            user_obj = user.User(
                id=None,
                name=name,
                birthday=birthday,
                height=height,
                target_weight=target_weight,
            )

            access_users.create_user(cursor, user_obj)
            cnx.commit()

            print()
            print("ユーザを登録しました")
            print()

        else:
            print("[Error] そのユーザー名はすでに存在します")
            print()

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
