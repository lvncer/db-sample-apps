
# import mysql.connector


def find_by_id_exam(cursor, id):
    # 3) 検索用sqlを作成

    # あとから設定したい値には%sに置き換える
    sql = "SELECT * FROM exam WHERE id = %s ORDER BY id, score DESC"

    # 設定したい値はリストにする
    data = [id]

    # sqlを実行(SQLの文字列、値のリスト)
    cursor.execute(sql, data)

    # 5) 取得したレコードを表示

    rows = cursor.fetchall()

    return rows


def update_score(cursor, id, subject):
    sql = "SELECT * FROM exam WHERE id = %s and subject = %s ORDER BY id, score DESC"
    data = [id, subject]

    # sqlを実行
    cursor.execute(sql, data)

    rows = cursor.fetchall()

    return rows


def select_all(cursor):
    # 2) 検索用sqlを作成

    sql = "SELECT * FROM exam ORDER BY id, score DESC"

    # 3) sqlを実行する

    # sqlを実行
    cursor.execute(sql)

    # 4) 取得したレコードを全て表示

    rows = cursor.fetchall()

    return rows


def pre_delete_showtable_exam(cursor, id, subject):
    print("以下の対象を削除します")
    sql = "SELECT * FROM exam WHERE id = %s and subject = %s ORDER BY id DESC"

    # 設定したい値はリストにする
    data = [id, subject]

    # sqlを実行(SQLの文字列、値のリスト)
    cursor.execute(sql, data)

    # 5) 取得したレコードを表示

    rows = cursor.fetchall()

    if len(rows) != 0:
        for row in rows:
            print(f"ID={row['id']} :", end=' ')
            print(f"subject={row['subject']} :", end=' ')
            print(f"score={row['score']}")
