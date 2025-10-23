def find_by_id_student(cursor, id):
    sql = "SELECT * FROM student WHERE id = %s"

    data = [id]
    cursor.execute(sql, data)
    rows = cursor.fetchone()

    return rows


def select_all(cursor):
    sql = "SELECT * FROM student ORDER BY id"

    cursor.execute(sql)
    rows = cursor.fetchall()

    return rows


def pre_delete_showtable_school(cursor, id):
    print("以下の対象を削除します")
    sql = "SELECT * FROM student WHERE id = %s ORDER BY id DESC"

    data = [id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    if len(rows) != 0:
        for row in rows:
            print(f"ID={row['id']} : ", end=" ")
            print(f"name={row['name']} : ", end=" ")
            print(f"birthday={row['birthday']} :", end=" ")
            print(f"class={row['class']}")
