from ..db import weight_record
from typing import List


def find_by_id(cursor, id) -> weight_record.WeightRecord | None:
    sql = """
        SELECT * FROM weight_records WHERE id = %s;
    """

    weight_record_obj = None

    data = [id]
    cursor.execute(sql, data)
    row = cursor.fetchone()
    if row:
        weight_record_obj = weight_record.WeightRecord(
            id=row["id"],
            user_id=row["user_id"],
            record_date=row["record_date"],
            height=row["height"],
            weight=row["weight"],
            target_weight=row["target_weight"],
        )
    return weight_record_obj


def find_by_user_id(cursor, user_id) -> List[weight_record.WeightRecord]:
    sql = """
        SELECT * FROM weight_records WHERE user_id = %s;
    """

    weight_record_list = []

    data = [user_id]
    cursor.execute(sql, data)
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            weight_record_list.append(
                weight_record.WeightRecord(
                    id=row["id"],
                    user_id=row["user_id"],
                    record_date=row["record_date"],
                    height=row["height"],
                    weight=row["weight"],
                    target_weight=row["target_weight"],
                )
            )
    return weight_record_list


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
