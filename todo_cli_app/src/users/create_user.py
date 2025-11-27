# ユーザー登録プログラム
# 入力されたユーザ情報をusersテーブルに登録する

import os
import sys
import mysql.connector

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ..util import db_util
from ..util import input_util
from ..db import access_users


def execute():
    try:
        # mysqlに接続
        cnx = db_util.connect()
        # カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        print('*** ユーザ登録 ***')

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # 入力したユーザ名がテーブルが存在するかチェック
        rows = access_users.find_by_name_user(cursor, name)

        # 登録する
        create_user(rows, cursor, name, cnx)

    except mysql.connector.Error as e:
        print('エラーが発生しました')
        print(e)

    # 終了処理
    finally:
        cursor.close()
        cnx.close()


def create_user(rows, cursor, name, cnx):
    if len(rows) == 0:

        birthday = input_util.input_date('生年月日を入力してください [%Y-%m-%d] : ')

        # sqlを実行する
        access_users.create_user(cursor, name, birthday)

        cnx.commit()

        print()
        print('ユーザを登録しました')

    # 存在していた場合は登録をキャンセルする
    else:
        print()
        print("[Error] そのユーザー名はすでに存在します")


if __name__ == '__main__':
    execute()
