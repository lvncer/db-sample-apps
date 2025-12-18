import mysql.connector
import datetime
from ..util import db_util
from ..util import input_util
from ..db import access_users
from ..db import access_todo_records
from ..db.user import User


def execute():
    try:
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print("*** TODO出力 ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        user = access_users.find_by_name(cursor, name)
        if user:
            output_html(cursor, user)

            print()
            print("ファイルに出力しました")
            print()
        else:
            print()
            print("[Error] そのユーザ名は存在しません")
            print()

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


def output_html(cursor, user: User):
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

        print("並び順")
        print("1: 優先度高い順")
        print("2: 期限短い順")
        print("を入力してください: ", end="")

        sort_prompt = input_util.input_sort_order()

        user_id = user.id

        todo_records = access_todo_records.find_by_user_id_sort_order(
            cursor, user_id, sort_prompt
        )

        for todo_record in todo_records:
            deadline = input_util.change_deadline_to_empty_string(todo_record.deadline)
            priority_str = input_util.change_priority_to_string(todo_record.priority)

            file.write("<tr>\n")
            file.write(f"<td>{todo_record.id}\n")
            file.write(f"<td>{todo_record.title}\n")
            file.write(f"<td>{deadline}\n")
            file.write(f"<td>{priority_str}\n")
            file.write("</tr>\n")

        file.write("</table>")

        file.write("</body>\n")
        file.write("</html>\n")


if __name__ == "__main__":
    execute()
