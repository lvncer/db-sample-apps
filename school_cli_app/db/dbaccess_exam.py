def find_by_id_exam(cursor, id):
    sql = "SELECT * FROM exam WHERE id = %s ORDER BY id, score DESC"

    data = [id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    return rows


def update_score(cursor, id, subject):
    sql = "SELECT * FROM exam WHERE id = %s and subject = %s ORDER BY id, score DESC"

    data = [id, subject]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    return rows


def select_all(cursor):
    sql = "SELECT * FROM exam ORDER BY id, score DESC"

    cursor.execute(sql)
    rows = cursor.fetchall()

    return rows


def pre_delete_showtable_exam(cursor, id, subject):
    print("以下の対象を削除します")
    sql = "SELECT * FROM exam WHERE id = %s and subject = %s ORDER BY id DESC"

    data = [id, subject]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    if len(rows) != 0:
        for row in rows:
            print(f"ID={row['id']} :", end=" ")
            print(f"subject={row['subject']} :", end=" ")
            print(f"score={row['score']}")
