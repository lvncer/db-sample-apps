# ユーザ検索プログラム
# usersテーブルからキーボードで入力したユーザ名を条件にレコードを取得して表示

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

        print("*** 記録削除 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # usersテーブルに指定されたユーザ名が存在するかを確認
        user_row = access_users.find_by_name_user(cursor, name)

        if len(user_row) != 0:
            id = input_util.input_int("削除するIDを入力してください : ")

            rows = access_weight_records.preshow_delete_records(cursor, id, name)

            if len(rows) != 0:
                for row in rows:
                    id = row["id"]
                    height_cm = float(row["height"])
                    weight_kg = float(row["weight"])
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
                    fat_level = db_util.calc_fat_level(bmi, age)

                    print()
                    print(f"id: {id}")
                    print(f"日付: {record_date}")
                    print(f"BMI: {bmi}")
                    print(f"標準体重: {standard_weight} kg")
                    print(f"肥満度: {fat_level}")
                    print()

                result_confirm = db_util.confirming(
                    "削除してもよろしいですか？ [y/n] : "
                )

                if result_confirm:
                    access_weight_records.delete_records_by_id(cursor, id)

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
