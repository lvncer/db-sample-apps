from ..db import weight_record
from typing import List
import datetime


def find_by_id(cursor, id) -> weight_record.WeightRecord | None:
    sql = """
        SELECT * FROM weight_records WHERE id = %s;
    """

    weight_record_obj = None

    data = [id]
    cursor.execute(sql, data)
    row = cursor.fetchone()
    if row:
        weight_record_obj = weight_record.WeightRecord(**row)
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
            weight_record_list.append(weight_record.WeightRecord(**row))
    return weight_record_list


# 出力用の全てのレコードを取得する
def select_all_by_user_id_and_date(
    cursor, user_id, dates
) -> List[weight_record.WeightRecord]:
    sql = """
        SELECT * FROM weight_records
        WHERE
            user_id = %s AND record_date BETWEEN %s AND LAST_DAY(%s);
    """

    data = [user_id, dates, dates]
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    weight_record_list = []
    if rows:
        for row in rows:
            weight_record_list.append(weight_record.WeightRecord(**row))
    return weight_record_list


def insert_weight_records(
    cursor,
    user_id,
    height_cm,
    weight_kg,
    target_weight,
):
    sql = """
        INSERT INTO weight_records
        (user_id, record_date, height, weight, target_weight)
        VALUES (%s, %s, %s, %s, %s);
    """
    d_today = datetime.datetime.now()

    data = [user_id, d_today, height_cm, weight_kg, target_weight]
    cursor.execute(sql, data)


def delete_by_user_id(cursor, user_id):
    sql = """
        DELETE FROM weight_records WHERE user_id = %s;
    """

    data = [user_id]
    cursor.execute(sql, data)


def delete_by_id(cursor, id):
    sql = """
        DELETE FROM weight_records WHERE id = %s;
    """

    data = [id]
    cursor.execute(sql, data)
