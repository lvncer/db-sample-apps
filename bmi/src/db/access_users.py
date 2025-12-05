from .user import User


def find_by_name(cursor, name) -> User | None:
    sql = """
        SELECT * FROM users
        WHERE name = %s;
    """

    data = [name]
    cursor.execute(sql, data)
    row = cursor.fetchone()

    if row:
        return User(**row)
    return None


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


def delete_by_id(cursor, id):
    sql = """
        DELETE FROM users WHERE id = %s;
    """

    data = [id]
    cursor.execute(sql, data)
