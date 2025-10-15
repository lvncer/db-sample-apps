import datetime
import mysql.connector

from ..util import db_util
from ..util import input_util
from ..db import access_users
from ..db import access_weight_records


def execute():
    try:
        # mysqlに接続
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 体重記録 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # 入力したユーザ名がusersテーブルに存在しているか確認
        rows = access_users.find_by_name_user(cursor, name)

        if len(rows) != 0:
            while True:
                weight_kg = float(
                    input_util.input_float("体重を入力してください(kg) : ")
                )

                if weight_kg <= 0:
                    print("体重は正の値を入力してください")
                elif weight_kg > 1000:
                    print("体重は1000kg未満の値を入力してください")
                else:
                    break

            user_id = rows[0]["id"]
            height_cm = float(rows[0]["height"])
            target_weight = float(rows[0]["target_weight"])
            birthday = rows[0]["birthday"]
            text = []

            # 身長をセンチからメートル単位に変更する
            height_m = height_cm / 100

            # BMI計算
            bmi = weight_kg / (height_m**2.0)
            # 小数点以下第1桁まで表示する
            bmi = round(bmi, 1)

            # 標準体重計算
            standard_weight = height_m**2 * 22
            # 小数点以下第1桁まで表示する
            standard_weight = round(standard_weight, 1)

            # 現在時刻の取得[%Y-%m-%d %H:%M:%S]
            d_today = datetime.datetime.now()

            # 現在日時の取得[%Y-%m-%d]
            today = datetime.datetime.today().date()

            # 年齢を計算する
            age = (
                d_today.year
                - birthday.year
                - ((d_today.month, d_today.day) < (birthday.month, birthday.day))
            )

            # BMIによる肥満度の判定
            fat_level = db_util.calc_fat_level(bmi, age)

            # 残りの平均体重への体重の差
            remain_standard = db_util.calc_remain_standard(weight_kg, standard_weight)

            # 残りの目標体重への体重の差
            remain_target = db_util.calc_remain_target(weight_kg, target_weight)

            access_weight_records.insert_weight_records(
                cursor, user_id, d_today, height_cm, weight_kg, target_weight
            )

            cnx.commit()

            # 誕生日と一致するか確認するための準備
            today_month = today.strftime("%m")
            today_day = today.strftime("%d")
            birthday_month = birthday.strftime("%m")
            birthday_day = birthday.strftime("%d")

            print()
            print("---- BMI計算 ----")
            text.append(f"身長: {height_cm}")
            text.append(f"体重: {weight_kg}")
            text.append(f"BMI: {bmi}")
            text.append(f"標準体重: {standard_weight} (あと{remain_standard}kg)")
            text.append(f"肥満度: {fat_level}")
            text.append(f"目標体重: {target_weight} (あと{remain_target}kg)")
            db_util.play_sound(text)
            print()

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
