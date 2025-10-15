
# 敵の進捗状況を取得
def find_by_progress(cursor, progress):
    sql = (
        '''
        SELECT * FROM enemies
        WHERE level = %s
        '''
    )

    data = [progress]

    cursor.execute(sql, data)

    rows = cursor.fetchall()

    return rows
