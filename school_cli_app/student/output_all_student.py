# 学生出力プログラム
# studentテーブルからすべてのレコードを取得してHTML形式で出力

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from util import dbutil
from db import dbaccess_student


def execute():
    # 1) 初期処理

    # mysqlに接続

    try:
        cnx = dbutil.connect()

        # カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        # データベースから学生情報を全件取得
        rows = dbaccess_student.select_all(cursor)

        # HTML形式でファイル出力
        output_html(rows)

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 5) 終了処理

    finally:
        cursor.close()
        cnx.close()


# HTML形式でファイル出力
def output_html(rows):
    file_name = "all_student.html"

    with open(file_name, mode="w", encoding="utf-8", newline="\n") as file:
        file.write("<html>\n")
        file.write("<head>\n")
        file.write("<title>学生一覧</title>\n")

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
        file.write("<h1>学生一覧</h1>\n")
        file.write("<hr/>\n")

        # テーブルで出力
        file.write("<table border=1>\n")  # テーブルの外枠を作る
        file.write("<tr>\n")  # テーブルの行を作る
        file.write("<td>ID</td>\n")  # 行に列を作る
        file.write("<td>名前</td>\n")
        file.write("<td>生年月日</td>\n")
        file.write("<td>クラス</td>\n")
        file.write("</tr>\n")

        # selectしたレコードを出力
        for row in rows:
            file.write("<tr>\n")
            file.write(f"<td>{row['id']}\n")
            file.write(f"<td>{row['name']}\n")
            file.write(f"<td>{row['birthday']}</td>\n")
            file.write(f"<td>{row['class']}</td>\n")
            file.write("</tr>\n")

        file.write("</table>")

        file.write("</body>\n")
        file.write("</html>\n")


if __name__ == "__main__":
    execute()
