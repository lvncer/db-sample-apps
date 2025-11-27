import datetime
import mysql.connector
from ..util import db_util
from ..util import input_util
from ..util import calc_util
from ..db import access_users
from ..db import access_weight_records


def execute():
    try:
        # mysqlに接続
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** 記録表示 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # userテーブルに存在するかを確認
        rows = access_users.find_by_name_user(cursor, name)

        if len(rows) != 0:
            rows = access_weight_records.find_by_name_weight_records(cursor, name)

            if len(rows) != 0:
                for row in rows:
                    id = row["id"]
                    height_cm = float(row["height"])
                    weight_kg = float(row["weight"])
                    target_weight = float(row["target_weight"])
                    record_date = row["record_date"]
                    birthday = row["birthday"]

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

                    # 年齢を計算する
                    age = (
                        d_today.year
                        - birthday.year
                        - (
                            (d_today.month, d_today.day)
                            < (birthday.month, birthday.day)
                        )
                    )

                    # BMIによる肥満度の判定
                    fat_level = calc_util.calc_fat_level(bmi, age)

                    # 残りの平均体重への体重の差
                    remain_standard = calc_util.calc_remain_standard(
                        weight_kg, standard_weight
                    )

                    # 残りの目標体重への体重の差
                    remain_target = calc_util.calc_remain_target(weight_kg, target_weight)

                    # 結果を表示
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

                print(f"{len(rows)}件表示しました")
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
