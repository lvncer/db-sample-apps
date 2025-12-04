import datetime
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

        print("*** 記録表示 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        user_obj = access_users.find_by_name(cursor, name)
        if user_obj:
            user_id = user_obj.id
            birthday = user_obj.birthday
            weight_records = access_weight_records.find_by_user_id(
                cursor, user_id
            )
            if weight_records:
                for weight_record in weight_records:
                    id = weight_record.id
                    height_cm = weight_record.height
                    weight_kg = weight_record.weight
                    target_weight = weight_record.target_weight
                    record_date = weight_record.record_date

                    height_m = height_cm / 100
                    bmi = round(weight_kg / (height_m**2), 1)
                    standard_weight = round(height_m**2 * 22, 1)

                    d_today = datetime.datetime.now()
                    age = (
                        d_today.year
                        - birthday.year
                        - (
                            (d_today.month, d_today.day)
                            < (birthday.month, birthday.day)
                        )
                    )

                    fat_level = calc_util.calc_fat_level(bmi, age)
                    remain_standard = calc_util.calc_remain_standard(
                        weight_kg, standard_weight
                    )
                    remain_target = calc_util.calc_remain_target(
                        weight_kg, target_weight
                    )

                    print()
                    print(f"id: {id}")
                    print(f"日付: {record_date}")
                    print(f"身長: {height_cm}")
                    print(f"体重: {weight_kg}")
                    print(f"BMI: {bmi}")
                    print(f"標準体重: {standard_weight} (あと{remain_standard}kg)")
                    print(f"肥満度: {fat_level}")
                    print(f"目標体重: {target_weight} (あと{remain_target}kg)")
                    print()

                print(f"{len(weight_records)}件表示しました")
                print()
            else:
                print("[Error] そのユーザの体重は記録されていません")
                print()

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
