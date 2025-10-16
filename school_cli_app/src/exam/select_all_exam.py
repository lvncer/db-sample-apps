import mysql.connector
from ..util import dbutil


def execute():
    try:
        # mysqlに接続
        cnx = dbutil.connect()
        cursor = cnx.cursor(dictionary=True)

        sql = "SELECT * FROM exam ORDER BY id, score DESC"

        cursor.execute(sql)
        rows = cursor.fetchall()

        print("*** 成績の全件表示 ***")

        for row in rows:
            print(f"{row['id']}: {row['subject']} {row['score']}点")

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    finally:
        cursor.close()
        cnx.close()


if __name__ == "__main__":
    execute()
