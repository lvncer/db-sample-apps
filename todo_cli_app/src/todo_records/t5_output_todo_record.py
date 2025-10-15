# TODO出力プログラム
# 指定されたユーザのTODOを表示する

import os
import sys
import mysql.connector
import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util import db_util
from util import input_util
from db import access_users
from db import access_todo_records


def execute():
    try:
        # mysqlに接続
        cnx = db_util.connect()
        # カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        print('*** TODO出力 ***')

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # userテーブルから該当するユーザの情報を取得する
        user_rows = access_users.find_by_name_user(cursor, name)

        # HTML形式でファイル出力
        output_html(cursor, user_rows)

        print()
        print('ファイルに出力しました')
        print()

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


def output_html(cursor, user_rows):
    file_name = "todo_records.html"

    with open(file_name, mode="w", encoding="utf-8", newline="\n") as file:
        file.write("<html>\n")
        file.write("<head>\n")
        file.write("<title>TODO記録</title>\n")

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
        file.write("<h1>TODO記録</h1>\n")
        file.write("<hr/>\n")

        file.write("<table border=1>\n")
        file.write("<tr>\n")
        file.write("<td>ID</td>\n")
        file.write("<td>タイトル</td>\n")
        file.write("<td>日付</td>\n")
        file.write("<td>優先度</td>\n")
        file.write("</tr>\n")

        print('並び順')
        print('1: 優先度高い順')
        print('2: 期限短い順')
        print('を入力してください: ', end='')

        sort_prompt = input_util.input_sort_order()

        user_id = user_rows[0]["id"]

        # 該当するすべてのレコードを取得する
        todo_rows = access_todo_records.find_by_user_id_todo_records(
            cursor, user_id, sort_prompt
        )

        # selectしたレコードを出力
        for row in todo_rows:
            id = row['id']
            title = row['title']
            deadline = row['deadline']
            priority = row['priority']

            if deadline == datetime.date(9999, 12, 31):
                deadline = ''

            priority = db_util.change_priority(priority)

            file.write("<tr>\n")
            file.write(f"<td>{id}\n")
            file.write(f"<td>{title}\n")
            file.write(f"<td>{deadline}\n")
            file.write(f"<td>{priority}\n")
            file.write("</tr>\n")

        file.write("</table>")

        file.write("</body>\n")
        file.write("</html>\n")


if __name__ == "__main__":
    execute()
