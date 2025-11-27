from .user import menu_users
from .weight import menu_records
from .util import input_util


def execute():
    print("=== メイン メニュー ===")
    print_menu()

    while True:
        no = input_util.input_int("メニューを選択してください : ")

        # 番号によってモジュールの関数を実行
        if no == 1:
            menu_users.execute()
        elif no == 2:
            menu_records.execute()
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
