# ユーザ検索プログラム
# usersテーブルからキーボードで入力したユーザ名を条件にレコードを取得して表示

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from util import db_util
from util import input_util
from db import access_users
from db import access_weight_records
import datetime


def execute():
    # mysqlに接続
    cnx = db_util.connect()

    try:
        # カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        print("*** 記録削除 ***")

        # 2) キーボードから入力させる
        name = input_util.input_replace("ユーザ名を入力してください : ")

        # usersテーブルに指定されたユーザ名が存在するかを確認
        user_row = access_users.find_by_name_user(cursor, name)

        # usersテーブルにユーザが存在し、整合性がとれたなら以下を実行する
        if len(user_row) != 0:
            id = input_util.input_int('削除するIDを入力してください : ')

            # 5) 取得したレコードを表示
            rows = access_weight_records.preshow_delete_records(cursor, id, name)

            if len(rows) != 0:
                for row in rows:

                    id = row['id']
                    height_cm = float(row['height'])
                    weight_kg = float(row['weight'])
                    record_date = row['record_date']
                    birthday = row['birthday']

                    # 身長をセンチからメートル単位に変更する
                    height_m = height_cm / 100

                    # BMI計算
                    bmi = weight_kg / (height_m ** 2.0)
                    # 小数点以下第1桁まで表示する
                    bmi = round(bmi, 1)

                    # 標準体重計算
                    standard_weight = height_m ** 2 * 22
                    # 小数点以下第1桁まで表示する
                    standard_weight = round(standard_weight, 1)

                    # 現在時刻の取得[%Y-%m-%d %H:%M:%S]
                    d_today = datetime.datetime.now()

                    # 年齢を計算する
                    age = d_today.year - birthday.year - (
                        (d_today.month, d_today.day) < (birthday.month, birthday.day)
                    )

                    # BMIによる肥満度の判定
                    fat_level = db_util.calc_fat_level(bmi, age)

                    print()
                    print(f'id: {id}')
                    print(f'日付: {record_date}')
                    print(f'BMI: {bmi}')
                    print(f'標準体重: {standard_weight} kg')
                    print(f'肥満度: {fat_level}')
                    print()

                # 削除確認（Yを入力すると削除が確定される)
                result_confirm = db_util.confirming("削除してもよろしいですか？ [y/n] : ")

                # Yが入力されたならば以下を実行する
                if result_confirm:

                    access_weight_records.delete_records_by_id(cursor, id)

                    # 削除を確定する
                    cnx.commit()

                    print('削除しました')
                    print()

                # nが入力されたならば以下を実行する
                else:
                    print("削除をキャンセルしました")
                    print()

            # weight_recordsテーブルに該当するidが存在しない場合は以下を実行する
            else:
                print('[Error] 指定されたIDは存在しません')

        # usersテーブルに該当するユーザ名が存在しない場合は以下を実行する
        else:
            print("[Error] そのユーザ名は存在しません")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 6) 終了処理
    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
