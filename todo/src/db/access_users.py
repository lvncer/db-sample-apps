from .user import User


def find_by_name(cursor, name: str) -> User | None:
    sql = """
        SELECT * FROM users WHERE name = %s
        ORDER BY id DESC;
    """

    data = [name]
    cursor.execute(sql, data)
    row = cursor.fetchone()

    if row:
        return User(**row)
    return None


def create_user(cursor, name, birthday) -> None:
    sql = """
        INSERT INTO users (name, birthday, experience, progress)
        VALUES (%s, %s, 0, 1);
    """

    data = [name, birthday]
    cursor.execute(sql, data)


def update_birthday(cursor, birthday, name) -> None:
    sql = """
        UPDATE users SET birthday= %s
        WHERE name = %s;
    """

    data = [birthday, name]
    cursor.execute(sql, data)


def update_experience(cursor, name, now_experience) -> None:
    sql = """
        UPDATE users
        SET experience = experience + %s
        WHERE name = %s;
    """

    data = [now_experience, name]
    cursor.execute(sql, data)


def update_progress(cursor, name, now_progress) -> None:
    sql = """
        UPDATE users
        SET progress = %s
        WHERE name = %s;
    """

    data = [now_progress, name]
    cursor.execute(sql, data)


def delete_user(cursor, name) -> None:
    sql = """
        DELETE FROM users WHERE name = %s;
    """

    data = [name]
    cursor.execute(sql, data)
