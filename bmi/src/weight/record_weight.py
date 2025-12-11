import mysql.connector
from ..util import db_util
from ..util import input_util
from ..util import calc_util
from ..util import validate_util
from ..db import access_users
from ..db import access_weight_records
from ..util import print_util


def execute():
    try:
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 体重記録 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        user_obj = access_users.find_by_name(cursor, name)
        if user_obj:
            while True:
                weight_kg = input_util.input_float("体重を入力してください(kg) : ")
                if validate_util.validate_weight(weight_kg):
                    break

            user_id = user_obj.id
            height_cm = float(user_obj.height)
            target_weight = float(user_obj.target_weight)
            birthday = user_obj.birthday

            access_weight_records.insert_weight_records(
                cursor, user_id, height_cm, weight_kg, target_weight
            )

            (
                height_cm,
                weight_kg,
                target_weight,
                _record_date,
                bmi,
                standard_weight,
                fat_level,
                remain_standard,
                remain_target,
            ) = calc_util.calc_metrics_from_values(
                height_cm,
                weight_kg,
                target_weight,
                birthday,
                record_date=None,
            )

            print()
            print("---- BMI計算 ----")

            print_util.print_weight_metrics(
                id=id,
                height_cm=height_cm,
                weight_kg=weight_kg,
                bmi=bmi,
                standard_weight=standard_weight,
                fat_level=fat_level,
                target_weight=target_weight,
                remain_standard=remain_standard,
                remain_target=remain_target,
            )

            if calc_util.is_birthday_today(birthday):
                print("今日はあなたの誕生日です！")

            print("体重を記録しました")

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
