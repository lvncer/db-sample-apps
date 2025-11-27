from .user import User


def find_by_name_user(cursor, name) -> User | None:
    sql = """
        SELECT * FROM users WHERE name = %s
        ORDER BY id DESC;
    """

    data = [name]
    cursor.execute(sql, data)
    rows = cursor.fetchone()

    return rows


def create_user(cursor, user: User) -> None:
    sql = """
        INSERT INTO users (name, birthday, height, target_weight)
        VALUES (%s, %s, %s, %s);
    """

    data = [user.name, user.birthday, user.height, user.target_weight]
    cursor.execute(sql, data)


def update_height(cursor, height, name):
    sql = """
        UPDATE users SET height = %s
        WHERE name = %s;
    """

    data = [height, name]
    cursor.execute(sql, data)


def update_target_weight(cursor, target_weight, name):
    sql = """
        UPDATE users SET target_weight = %s
        WHERE name = %s;
    """

    data = [target_weight, name]
    cursor.execute(sql, data)


def delete_user(cursor, name):
    sql = """
        DELETE FROM users WHERE name = %s;
    """

    data = [name]
    cursor.execute(sql, data)


# 削除する前に該当する行を表示する
def find_delete_id(cursor, name, id):
    sql = """
        SELECT weight_records.id AS id
        FROM weight_records LEFT OUTER JOIN users
        ON weight_records.user_id = users.id
        WHERE name = %s AND weight_records.id = %s;
    """

    data = [name, id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    return rows


# delete_userで削除するユーザのweight_recordsに記録されている体重の件数を返す
def find_weight_records(cursor, name):
    sql = """
        SELECT weight_records.id AS id
        FROM weight_records LEFT OUTER JOIN users
        ON weight_records.user_id = users.id
        WHERE name = %s;
    """

    data = [name]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    return rows


# ユーザ名からidを取得する
def find_id_by_name(cursor, name):
    sql = """
        SELECT id FROM users WHERE name = %s;
    """

    data = [name]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    return rows[0]["id"]
