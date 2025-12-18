from .users import menu_user
from .todo_records import menu_todo_records
from .quests import menu_quest
from .util import input_util


def execute():
    print("###############")
    print(" TODOアプリ")
    print("###############")
    print()
    print("=== メイン メニュー ===")
    print_menu()

    while True:
        no = input_util.input_int("メニューを選択してください : ")
        match no:
            case 1:
                menu_user.execute()
            case 2:
                menu_todo_records.execute()
            case 3:
                menu_quest.execute()
            case 4:
                print("終了します")
                break
            case _:
                print("無効な値です")
                print_menu()


def print_menu():
    print()
    print("1. ユーザ管理")
    print("2. TODO管理")
    print("3. クエスト")
    print("4. 終了")
    print()


if __name__ == "__main__":
    execute()
