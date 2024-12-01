
# import mysql.connector


def find_by_id_student(cursor, id):
    # 3) 検索用sqlを作成

    # あとから設定したい値には%sに置き換える
    sql = "SELECT * FROM student WHERE id = %s"

    # 設定したい値はリストにする
    data = [id]

    # sqlを実行
    cursor.execute(sql, data)

    # 5) 取得したレコードを表示

    rows = cursor.fetchall()

    return rows


def select_all(cursor):
    # 2) 検索用sqlを作成

    sql = "SELECT * FROM student ORDER BY id"

    # 3) sqlを実行する

    # sqlを実行
    cursor.execute(sql)

    # 4) 取得したレコードを全て表示

    rows = cursor.fetchall()

    return rows


def pre_delete_showtable_school(cursor, id):
    print("以下の対象を削除します")

    sql = "SELECT * FROM student WHERE id = %s ORDER BY id DESC"

    # 設定したい値はリストにする
    data = [id]

    # sqlを実行(SQLの文字列、値のリスト)
    cursor.execute(sql, data)

    # 5) 取得したレコードを表示

    rows = cursor.fetchall()

    if len(rows) != 0:
        for row in rows:
            print(f"ID={row['id']} : ", end=' ')
            print(f"name={row['name']} : ", end=' ')
            print(f"birthday={row['birthday']} :", end=' ')
            print(f"class={row['class']}")
