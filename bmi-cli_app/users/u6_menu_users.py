# ユーザ管理プログラム
# キーボードで入力した情報でusersモジュールを呼び出す

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from users import u1_create_user
from users import u2_find_by_name_users
from users import u3_update_height
from users import u4_update_target_weight
from users import u5_delete_user
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
            u2_find_by_name_users.execute()
        elif no == 3:
            u3_update_height.execute()
        elif no == 4:
            u4_update_target_weight.execute()
        elif no == 5:
            u5_delete_user.execute()
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
