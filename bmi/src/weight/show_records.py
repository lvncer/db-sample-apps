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
                    (
                        height_cm,
                        weight_kg,
                        target_weight,
                        record_date,
                        bmi,
                        standard_weight,
                        fat_level,
                        remain_standard,
                        remain_target,
                    ) = calc_util.calc_weight_record_metrics(
                        weight_record, birthday
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
