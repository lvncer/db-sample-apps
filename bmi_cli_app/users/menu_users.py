# ユーザ管理プログラム
# キーボードで入力した情報でusersモジュールを呼び出す

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from users import create_user
from users import find_by_name_users
from users import update_height
from users import update_target_weight
from users import delete_user
from util import input_util


def execute():
    print("=== ユーザ管理 メニュー ===")

    # メニューの表示
    print_menu()

    while True:
        no = input_util.input_int("メニューを選択してください : ")

        # 番号によってモジュールの関数を実行
        if no == 1:
            create_user.execute()
        elif no == 2:
            find_by_name_users.execute()
        elif no == 3:
            update_height.execute()
        elif no == 4:
            update_target_weight.execute()
        elif no == 5:
            delete_user.execute()
        elif no == 6:
            print("操作を終了します")
            break
        else:
            print("無効な値です")
            print_menu()


def print_menu():
    print("1. ユーザ登録")
    print("2. ユーザ表示")
    print("3. 身長更新")
    print("4. 目標体重更新")
    print("5. ユーザ削除")
    print("6. 終了")


if __name__ == "__main__":
    execute()
