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
