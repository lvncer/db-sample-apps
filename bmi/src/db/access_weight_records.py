# 指定された名前で結合したテーブルから必要な属性を取得する
def find_by_name_weight_records(cursor, name):
    sql = """
        SELECT
            weight_records.id AS id,
            record_date, weight_records.height,
            weight_records.weight,
            weight_records.target_weight AS target_weight,
            birthday
        FROM weight_records LEFT OUTER JOIN users
        ON weight_records.user_id = users.id
        WHERE name = %s;
    """

    data = [name]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    return rows


# weight_recordsに登録する
def insert_weight_records(
    cursor, user_id, d_today, height_cm, weight_kg, target_weight
):
    sql = """
        INSERT INTO weight_records
        (user_id, record_date, height, weight, target_weight)
        VALUES (%s, %s, %s, %s, %s);
    """

    data = [user_id, d_today, height_cm, weight_kg, target_weight]
    cursor.execute(sql, data)


# 削除する前に該当する行を表示する
def preshow_delete_records(cursor, id, name):
    sql = """
        SELECT
            weight_records.id AS id,
            record_date,
            weight_records.height,
            weight_records.weight,
            weight_records.target_weight,
            birthday
        FROM weight_records LEFT OUTER JOIN  users
        ON weight_records.user_id = users.id
        WHERE weight_records.id = %s AND name = %s;
    """

    data = [id, name]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    return rows


# 入力されたユーザーidで削除を確定する
def delete_records(cursor, user_id):
    sql = """
        DELETE FROM weight_records WHERE user_id = %s;
    """

    data = [user_id]
    cursor.execute(sql, data)


# 入力されたidで削除を確定する
def delete_records_by_id(cursor, id):
    sql = """
        DELETE FROM weight_records WHERE id = %s;
    """

    data = [id]
    cursor.execute(sql, data)


# 入力されたidで削除を確定する
def delete_by_user_id(cursor, id):
    sql = """
        DELETE FROM weight_records WHERE id = %s;
    """

    data = [id]
    cursor.execute(sql, data)


# 出力用の全てのレコードを取得する
def select_all(cursor, name, dates):
    sql = """
        select
            weight_records.id AS id,
            record_date,
            weight_records.height,
            weight_records.weight,
            weight_records.target_weight,
            birthday
        FROM weight_records LEFT OUTER JOIN users
        ON weight_records.user_id = users.id
        WHERE
            users.name = %s AND record_date BETWEEN %s AND LAST_DAY(%s);
        """

    data = [name, dates, dates]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    return rows
