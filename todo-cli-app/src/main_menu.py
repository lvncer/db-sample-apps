# メインメニュープログラム
# usersとtodo_recordsのメニューを出力する

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from users import u5_menu_user
from todo_records import t7_menu_todo_records
import quest
from util import input_util


def execute():
    print('###############')
    print(' TODOアプリ')
    print('###############')
    print()
    print("=== メイン メニュー ===")

    # メニューの表示
    print_menu()

    while True:
        # キーボードからメニュー番号を入力させる
        no = input_util.input_int("メニューを選択してください : ")

        # 番号によってモジュールの関数を実行
        if no == 1:
            u5_menu_user.execute()
        elif no == 2:
            t7_menu_todo_records.execute()
        elif no == 3:
            quest.execute()
        elif no == 4:
            print()
            print("終了します")
            break
        else:
            print()
            print("無効な値です")
            print_menu()
            print()


def print_menu():
    print()
    print("1. ユーザ管理")
    print("2. TODO管理")
    print("3. クエスト")
    print("4. 終了")
    print()


if __name__ == "__main__":
    execute()
