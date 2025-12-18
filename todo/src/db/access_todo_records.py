from .todo_record import TodoRecord


def find_by_user_id_sort_order(cursor, user_id, sort_prompt) -> list[TodoRecord]:
    sql = """
        SELECT * FROM todo_records
        WHERE user_id = %s
        ORDER BY {}
        LIMIT 5;
    """.format(
        sort_prompt
    )

    data = [user_id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    return [TodoRecord(**row) for row in rows]


def find_by_id(cursor, id) -> TodoRecord | None:
    sql = """
        SELECT * FROM todo_records
        WHERE id = %s;
    """

    data = [id]
    cursor.execute(sql, data)
    row = cursor.fetchone()

    if row:
        return TodoRecord(**row)
    return None


def find_by_user_id(cursor, user_id):
    sql = """
        SELECT id, user_id, title, deadline, priority
        FROM todo_records
        WHERE user_id = %s;
    """

    data = [user_id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    return rows


def insert_todo_records(cursor, todo_record: TodoRecord) -> None:
    sql = """
        INSERT INTO todo_records
        (user_id, title, deadline, priority)
        VALUES (%s, %s, %s, %s);
    """

    data = [
        todo_record.user_id,
        todo_record.title,
        todo_record.deadline,
        todo_record.priority,
    ]

    cursor.execute(sql, data)


def update_todo_records(cursor, todo_record: TodoRecord) -> None:
    sql = """
        UPDATE todo_records
        SET title = %s, deadline = %s, priority = %s
        WHERE id = %s;
    """

    data = [
        todo_record.title,
        todo_record.deadline,
        todo_record.priority,
        todo_record.id,
    ]

    cursor.execute(sql, data)


# TODO記録を削除する
def delete_todo_records(cursor, id):
    sql = """
        DELETE FROM todo_records
        WHERE id = %s;
        """

    data = [id]

    cursor.execute(sql, data)


# ユーザ管理で指定されたユーザ名のTODO記録を削除する
def delete_by_user_id_todo_records(cursor, user_id):
    sql = """
        DELETE FROM todo_records
        WHERE user_id = %s;
        """

    data = [user_id]

    cursor.execute(sql, data)
