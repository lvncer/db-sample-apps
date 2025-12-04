import mysql.connector
from ..util import db_util
from ..util import input_util
from ..util import calc_util
from ..db import access_users
from ..db import access_weight_records


def execute():
    try:
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 記録削除 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        user_obj = access_users.find_by_name(cursor, name)
        if user_obj:
            deleting_id = input_util.input_int("削除するIDを入力してください : ")

            weight_record_obj = access_weight_records.find_by_id(
                cursor, deleting_id
            )
            if weight_record_obj:
                id = weight_record_obj.id
                height_cm = float(weight_record_obj.height)
                weight_kg = float(weight_record_obj.weight)
                record_date = weight_record_obj.record_date
                birthday = user_obj.birthday

                # 身長をセンチからメートル単位に変更する
                height_m = height_cm / 100

                bmi = round(weight_kg / (height_m**2), 1)
                standard_weight = round(height_m**2 * 22, 1)

                age = calc_util.calc_age(birthday)
                fat_level = calc_util.calc_fat_level(bmi, age)

                print()
                print(f"id: {id}")
                print(f"日付: {record_date}")
                print(f"BMI: {bmi}")
                print(f"標準体重: {standard_weight} kg")
                print(f"肥満度: {fat_level}")
                print()

                result_confirm = input_util.confirming(
                    "削除してもよろしいですか？ [y/n] : "
                )
                if result_confirm:
                    access_weight_records.delete_by_id(cursor, id)
                    cnx.commit()

                    print("削除しました")
                    print()
                else:
                    print("削除をキャンセルしました")
                    print()

            else:
                print("[Error] 指定されたIDは存在しません")

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
