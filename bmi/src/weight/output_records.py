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

        print("記録出力")

        name = input_util.input_replace("ユーザ名を入力してください : ")
        date = input_util.input_month("出力する年月を入力してください:")
        date = date + "-01"

        user_obj = access_users.find_by_name(cursor, name)
        if user_obj:
            user_id = user_obj.id
            birthday = user_obj.birthday

            # データベースから該当する体重記録を全件取得
            rows = access_weight_records.select_all_by_user_id_and_date(
                cursor, user_id, date
            )

            # HTML形式でファイル出力
            output_html(birthday, rows)

            print()
            print("ファイルに出力しました")
            print()
        else:
            print("[Error] そのユーザ名は存在しません")
            print()

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


def output_html(birthday, rows):
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

        for row in rows:
            height_cm = float(row.height)
            weight_kg = float(row.weight)
            target_weight = float(row.target_weight)

            height_m = height_cm / 100

            bmi = round(weight_kg / (height_m**2.0), 1)
            standard_weight = round(height_m**2 * 22, 1)

            d_today = datetime.datetime.now()
            age = (
                d_today.year
                - birthday.year
                - ((d_today.month, d_today.day) <
                   (birthday.month, birthday.day))
            )

            fat_level = calc_util.calc_fat_level(bmi, age)

            remain_standard = calc_util.calc_remain_standard(
                weight_kg, standard_weight
            )
            remain_target = calc_util.calc_remain_target(
                weight_kg, target_weight
            )

            file.write("<tr>\n")
            file.write(f"<td>{row.id}\n")
            file.write(f"<td>{row.record_date}\n")
            file.write(f"<td>{height_cm}\n")
            file.write(f"<td>{weight_kg}\n")
            file.write(f"<td>{bmi}\n")
            file.write(f"<td>{standard_weight} (あと{remain_standard}kg)\n")
            file.write(f"<td>{fat_level}</td>\n")
            file.write(f"<td>{target_weight} (あと{remain_target}kg)</td>\n")
            file.write("</tr>\n")

        file.write("</table>")
        file.write("</body>\n")
        file.write("</html>\n")


if __name__ == "__main__":
    execute()
