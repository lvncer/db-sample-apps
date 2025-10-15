# ユーザ検索プログラム
# usersテーブルからキーボードで入力したユーザ名を条件にレコードを取得して表示

import os
import sys
import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import mysql.connector
import base64
from matplotlib.font_manager import FontProperties

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util import db_util
from util import input_util
from db import access_weight_records


def execute():
    # mysqlに接続
    cnx = db_util.connect()

    try:
        # カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        print('記録出力')

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # 指定された日付の形式で入力させる [%Y-%m]
        date = input_util.input_month("出力する年月を入力してください:")
        # 入力された月のはじめをdateに入れる
        date = date + "-01"

        # データベースから該当する体重記録を全件取得
        rows = access_weight_records.select_all(cursor, name, date)

        # HTML形式でファイル出力
        output_html(rows)

        print()
        print('ファイルに出力しました')
        print()

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 5) 終了処理

    finally:
        cursor.close()
        cnx.close()


def output_html(rows):
    file_name = "all_records.html"

    with open(file_name, mode="w", encoding="utf-8", newline="\n") as file:
        file.write("<html>\n")
        file.write("<head>\n")
        file.write("<title>体重記録出力</title>\n")

        file.write("<style>\n")
        file.write("table {\n")
        file.write("border-collapse: collapse;\n")
        file.write("border-spacing: 0;\n")
        file.write("}\n")
        file.write("td {\n")
        file.write("border: 1px solid #000;\n")
        file.write("padding: 8px;\n")
        file.write("}\n")
        file.write("</style>\n")

        file.write("</head>\n")
        file.write("<body>\n")
        file.write("<h1>体重記録</h1>\n")
        file.write("<hr/>\n")

        # テーブルで出力
        file.write("<table border=1>\n")  # テーブルの外枠を作る
        file.write("<tr>\n")  # テーブルの行を作る
        file.write("<td>ID</td>\n")  # 行に列を作る
        file.write("<td>日付</td>\n")
        file.write("<td>身長</td>\n")
        file.write("<td>体重</td>\n")
        file.write("<td>BMI</td>\n")
        file.write("<td>標準体重</td>\n")
        file.write("<td>肥満度</td>\n")
        file.write("<td>目標体重</td>\n")
        file.write("</tr>\n")

        # selectしたレコードを出力
        for row in rows:
            height_cm = float(row['height'])
            weight_kg = float(row['weight'])
            target_weight = float(row['target_weight'])
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

            remain_standard = db_util.calc_remain_standard(
                weight_kg, standard_weight
            )

            remain_target = db_util.calc_remain_target(
                weight_kg, target_weight
            )

            file.write("<tr>\n")
            file.write(f"<td>{row['id']}\n")
            file.write(f"<td>{row['record_date']}\n")
            file.write(f"<td>{height_cm}\n")
            file.write(f"<td>{weight_kg}\n")
            file.write(f"<td>{bmi}\n")
            file.write(f"<td>{standard_weight} (あと{remain_standard}kg)\n")
            file.write(f"<td>{fat_level}</td>\n")
            file.write(f"<td>{target_weight} (あと{remain_target}kg)</td>\n")
            file.write("</tr>\n")

        file.write("</table>")

        # グラフの埋め込み
        file.write("<h2>体重の変化</h2>")
        file.write('<img src="data:image/png;base64,{}" alt="体重の変化">'.format(
            plot_weight_changes(rows))
        )

        file.write("</body>\n")
        file.write("</html>\n")


def plot_weight_changes(rows):
    # 体重の変化をグラフに描画
    dates = [row['record_date'] for row in rows]
    weights = [float(row['weight']) for row in rows]

    plt.figure(figsize=(10, 5))

    # フォントの指定
    font_path = "C:/Windows/Fonts/msgothic.ttc"
    font_prop = FontProperties(fname=font_path)
    plt.rcParams['font.family'] = font_prop.get_name()

    plt.plot(dates, weights, marker='o')
    plt.title('体重の変化')
    plt.xlabel('日付')
    plt.ylabel('体重(kg)')
    plt.grid(True)

    # グラフをバイト列に変換してbase64エンコード
    img_data = BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    img_base64 = base64.b64encode(img_data.read()).decode('utf-8')

    plt.close()  # メモリリークを防ぐためにクローズ

    return img_base64


if __name__ == "__main__":
    execute()
