
# 登録する
def insert_todo_records(
    cursor, user_id, title, deadline, priority
):
    sql = (
        '''
        INSERT INTO todo_records
        (user_id, title, deadline, priority)
        VALUES (%s, %s, %s, %s);
        '''
    )

    data = [user_id, title, deadline, priority]

    cursor.execute(sql, data)


# 表示するために必要な情報をuser_idで検索する
def find_by_user_id_todo_records(cursor, user_id, sort_prompt):
    sql = (
        '''
        SELECT id, title, deadline, priority
        FROM todo_records
        WHERE user_id = %s
        ORDER BY {}
        LIMIT 5;
        '''.format(sort_prompt)
    )

    data = [user_id]

    cursor.execute(sql, data)

    rows = cursor.fetchall()

    return rows


# IDから検索したレコードを取得する
def find_by_id_todo(cursor, id):
    sql = (
        '''
        SELECT id, user_id, title, deadline, priority
        FROM todo_records
        WHERE id = %s;
        '''
    )

    data = [id]

    cursor.execute(sql, data)

    rows = cursor.fetchall()

    return rows


# ユーザIDから検索したレコードを取得する
def find_by_user_id(cursor, user_id):
    sql = (
        '''
        SELECT id, user_id, title, deadline, priority
        FROM todo_records
        WHERE user_id = %s;
        '''
    )

    data = [user_id]

    cursor.execute(sql, data)

    rows = cursor.fetchall()

    return rows


# 更新する
def update_todo_records(cursor, id, title, deadline, priority):
    sql = (
        '''
        UPDATE todo_records
        SET title = %s, deadline = %s, priority = %s
        WHERE id = %s;
        '''
    )

    data = [title, deadline, priority, id]

    cursor.execute(sql, data)


# TODO記録を削除する
def delete_todo_records(cursor, id):
    sql = (
        '''
        DELETE FROM todo_records
        WHERE id = %s;
        '''
    )

    data = [id]

    cursor.execute(sql, data)


# ユーザ管理で指定されたユーザ名のTODO記録を削除する
def delete_by_user_id_todo_records(cursor, user_id):
    sql = (
        '''
        DELETE FROM todo_records
        WHERE user_id = %s;
        '''
    )

    data = [user_id]

    cursor.execute(sql, data)
