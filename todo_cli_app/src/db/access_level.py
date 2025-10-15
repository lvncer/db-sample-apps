
# ステータスの取得
def find_status(cursor, my_level):
    sql = (
        '''
        SELECT * FROM levels
        WHERE level = %s
        '''
    )

    data = [my_level]

    cursor.execute(sql, data)

    rows = cursor.fetchall()

    return rows
