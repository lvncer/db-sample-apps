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

        print("*** 体重記録 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        user_obj = access_users.find_by_name(cursor, name)
        if user_obj:
            while True:
                weight_kg = input_util.input_float("体重を入力してください(kg) : ")

                if weight_kg <= 0:
                    print("体重は正の値を入力してください")
                elif weight_kg > 1000:
                    print("体重は1000kg未満の値を入力してください")
                else:
                    break

            user_id = user_obj.id
            height_cm = float(user_obj.height)
            target_weight = float(user_obj.target_weight)
            birthday = user_obj.birthday

            height_m = height_cm / 100

            bmi = round(weight_kg / (height_m**2), 1)
            standard_weight = round(height_m**2 * 22, 1)

            age = calc_util.calc_age(birthday)
            fat_level = calc_util.calc_fat_level(bmi, age)
            remain_standard = calc_util.calc_remain_standard(weight_kg, standard_weight)
            remain_target = calc_util.calc_remain_target(weight_kg, target_weight)

            d_today = datetime.datetime.now()
            access_weight_records.insert_weight_records(
                cursor, user_id, d_today, height_cm, weight_kg, target_weight
            )
            cnx.commit()

            print()
            print("---- BMI計算 ----")
            print(f"身長: {height_cm}")
            print(f"体重: {weight_kg}")
            print(f"BMI: {bmi}")
            print(f"標準体重: {standard_weight} (あと{remain_standard}kg)")
            print(f"肥満度: {fat_level}")
            print(f"目標体重: {target_weight} (あと{remain_target}kg)")
            print()

            today = datetime.datetime.today().date()
            today_month = today.strftime("%m")
            today_day = today.strftime("%d")
            birthday_month = birthday.strftime("%m")
            birthday_day = birthday.strftime("%d")
            if today_month == birthday_month and today_day == birthday_day:
                print("誕生日おめでとうございます！")

            print("体重を記録しました")

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
