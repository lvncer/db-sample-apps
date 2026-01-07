from . import create_user
from . import show_user
from . import update_user
from . import delete_user
from ..util import input_util


def execute():
    print()
    print("=== ユーザ管理 メニュー ===")

    while True:
        print()
        print_menu()
        print()
        no = input_util.input_int("メニューを選択してください : ")
        print()
        match no:
            case 1:
                create_user.execute()
            case 2:
                show_user.execute()
            case 3:
                update_user.execute()
            case 4:
                delete_user.execute()
            case 5:
                break
            case _:
                print("無効な値です")

    print("終了します")


def print_menu():
    print("1. ユーザ登録")
    print("2. ユーザ表示")
    print("3. ユーザ更新")
    print("4. ユーザ削除")
    print("5. 終了")


if __name__ == "__main__":
    execute()
