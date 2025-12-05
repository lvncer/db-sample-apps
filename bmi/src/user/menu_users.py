from . import create_user
from . import find_by_name_users
from . import update_height
from . import update_target_weight
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
                find_by_name_users.execute()
            case 3:
                update_height.execute()
            case 4:
                update_target_weight.execute()
            case 5:
                delete_user.execute()
            case 6:
                print("操作を終了します")
                return
            case _:
                print("無効な値です")


def print_menu():
    print("1. ユーザ登録")
    print("2. ユーザ表示")
    print("3. 身長更新")
    print("4. 目標体重更新")
    print("5. ユーザ削除")
    print("6. 終了")


if __name__ == "__main__":
    execute()
