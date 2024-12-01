

# 入力したユーザ名がusersテーブルに存在しているか確認
def find_by_name_user(cursor, name):
    # あとから設定したい値には%sに置き換える
    sql = "SELECT * FROM users WHERE name = %s ORDER BY id DESC"

    # 設定したい値はリストにする
    data = [name]

    # sqlを実行
    cursor.execute(sql, data)

    # 5) 取得したレコードを表示
    rows = cursor.fetchall()

    return rows


# usersテーブルにユーザを追加する
def create_user(cursor, name, birthday, height, target_weight):

    # あとから設定したい値には%sに置き換える
    sql = (
        '''
        INSERT INTO users
        (name, birthday, height, target_weight)
        VALUES (%s, %s, %s, %s);
        '''
    )

    # 設定したい値はリストにする
    data = [name, birthday, height, target_weight]

    # 4) sqlを実行する
    cursor.execute(sql, data)


# 身長を更新する
def update_height(cursor, height, name):
    # あとから設定したい値には%sに置き換える
    sql = (
        "UPDATE users SET height = %s WHERE name = %s"
    )

    # 設定したい値はリストにする
    data = [height, name]

    # sqlを実行(SQLの文字列、値のリスト)
    cursor.execute(sql, data)


# 目標体重を更新する
def update_target_weight(cursor, target_weight, name):
    # あとから設定したい値には%sに置き換える
    sql = (
        "UPDATE users SET target_weight = %s WHERE name = %s"
    )

    # 設定したい値はリストにする
    data = [target_weight, name]

    # sqlを実行(SQLの文字列、値のリスト)
    cursor.execute(sql, data)


# usersテーブルから指定されたユーザを削除する
def delete_user(cursor, name):
    # あとから設定したい値には%sに置き換える
    sql = (
        "DELETE FROM users WHERE name = %s;"
    )

    # 設定したい値はリストにする
    data = [name]

    # sqlを実行(SQLの文字列、値のリスト)
    cursor.execute(sql, data)


def find_delete_id(cursor, name, id):

    sql = (
        '''
        SELECT weight_records.id AS id
        FROM weight_records LEFT OUTER JOIN users
        ON weight_records.user_id = users.id
        WHERE name = %s AND weight_records.id = %s;
        '''
    )

    # 設定したい値はリストにする
    data = [name, id]

    # sqlを実行(SQLの文字列、値のリスト)
    cursor.execute(sql, data)

    # 5) 取得したレコードを表示
    rows = cursor.fetchall()

    return rows


# u5_delete_userで削除するユーザのweight_recordsに記録されている体重の件数を返す
def find_weight_records(cursor, name):

    sql = (
        '''
        SELECT weight_records.id AS id
        FROM weight_records LEFT OUTER JOIN users
        ON weight_records.user_id = users.id
        WHERE name = %s;
        '''
    )

    # 設定したい値はリストにする
    data = [name]

    # sqlを実行(SQLの文字列、値のリスト)
    cursor.execute(sql, data)

    # 5) 取得したレコードを表示
    rows = cursor.fetchall()

    return rows


def find_id_by_name(cursor, name):

    sql = (
        "SELECT id FROM users WHERE name = %s;"
    )

    # 設定したい値はリストにする
    data = [name]

    # sqlを実行(SQLの文字列、値のリスト)
    cursor.execute(sql, data)

    # 5) 取得したレコードを表示
    rows = cursor.fetchall()

    return rows[0]['id']
