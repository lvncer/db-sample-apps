from .users import menu_user
from .todo_records import menu_todo_records
from .quests import main as quests_main
from .util import input_util


def execute():
    print("###############")
    print(" TODOアプリ")
    print("###############")
    print()
    print("=== メイン メニュー ===")

    while True:
        print_menu()
        no = input_util.input_int("メニューを選択してください : ")
        match no:
            case 1:
                menu_user.execute()
            case 2:
                menu_todo_records.execute()
            case 3:
                quests_main.execute()
            case 4:
                break
            case _:
                print("無効な値です")

    print("終了します")


def print_menu():
    print()
    print("1. ユーザ管理")
    print("2. TODO管理")
    print("3. クエスト")
    print("4. 終了")
    print()


if __name__ == "__main__":
    execute()
