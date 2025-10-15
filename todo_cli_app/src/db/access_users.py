
# usersテーブルにユーザを追加する
def create_user(cursor, name, birthday):

    sql = (
        '''
        INSERT INTO users (name, birthday, experience, progress)
        VALUES (%s, %s, 0, 1);
        '''
    )

    data = [name, birthday]

    cursor.execute(sql, data)


# 登録するときに入力したユーザ名がusersテーブルに存在しているか確認
def find_by_name_user(cursor, name):
    sql = (
        'SELECT * FROM users WHERE name = %s ORDER BY id DESC'
    )

    data = [name]

    cursor.execute(sql, data)

    rows = cursor.fetchall()

    return rows


# 生年月日を更新する
def update_birthday(cursor, birthday, name):
    sql = (
        "UPDATE users SET birthday= %s WHERE name = %s"
    )

    data = [birthday, name]

    cursor.execute(sql, data)


# usersテーブルから指定されたユーザを削除する
def delete_user(cursor, name):
    sql = (
        "DELETE FROM users WHERE name = %s;"
    )

    data = [name]

    cursor.execute(sql, data)


# 完了したユーザの経験値を更新する
def update_experience(cursor, name, now_experience):
    sql = (
        '''
        UPDATE users
        SET experience = experience + %s
        WHERE name = %s;
        '''
    )

    data = [now_experience, name]

    cursor.execute(sql, data)


# 完了したユーザの進捗を更新する
def update_progress(cursor, name, now_progress):
    sql = (
        '''
        UPDATE users
        SET progress = %s
        WHERE name = %s;
        '''
    )

    data = [now_progress, name]

    cursor.execute(sql, data)
