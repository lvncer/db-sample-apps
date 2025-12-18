from . import create_user
from . import show_user
from . import update_user
from . import delete_user
from ..util import input_util


def execute():
    print("=== ユーザ管理 メニュー ===")
    print_menu()

    while True:
        no = input_util.input_int("メニューを選択してください : ")
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
                print("終了します")
                break
            case _:
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
