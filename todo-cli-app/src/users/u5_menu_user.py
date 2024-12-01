# ユーザ管理プログラム
# 入力されたメニュー選択番号でusersのモジュールを呼び出す

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from users import u1_create_user
from users import u2_show_user
from users import u3_update_user
from users import u4_delete_user
from util import input_util


def execute():
    print("=== ユーザ管理 メニュー ===")

    # メニューの表示
    print_menu()

    while True:
        # キーボードからメニュー番号を入力させる
        no = input_util.input_int("メニューを選択してください : ")

        # 番号によってモジュールの関数を実行
        if no == 1:
            u1_create_user.execute()
        elif no == 2:
            u2_show_user.execute()
        elif no == 3:
            u3_update_user.execute()
        elif no == 4:
            u4_delete_user.execute()
        elif no == 5:
            break
        else:
            print("無効な値です")
            print_menu()


def print_menu():
    print("1. ユーザ登録")
    print("2. ユーザ表示")
    print("3. ユーザ更新")
    print("4. ユーザ削除")
    print("5. 終了")


if __name__ == "__main__":
    execute()
