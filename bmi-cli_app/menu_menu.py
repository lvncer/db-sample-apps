import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from users import u6_menu_users
from weight_records import w5_menu_records
from util import input_util


def execute():
    print("=== メイン メニュー ===")

    # メニューの表示
    print_menu()

    while True:
        # キーボードからメニュー番号を入力させる
        no = input_util.input_int("メニューを選択してください : ")

        # 番号によってモジュールの関数を実行
        if no == 1:
            u6_menu_users.execute()
        elif no == 2:
            w5_menu_records.execute()
        elif no == 3:
            print("終了します")
            break
        else:
            print("無効な値です")


def print_menu():
    print("1: ユーザ管理")
    print("2: 体重管理")
    print("3: 終了")


if __name__ == "__main__":
    execute()
