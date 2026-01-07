from ..util import input_util
from . import create_todo_record
from . import show_todo_records
from . import update_todo_record
from . import delete_todo_record
from . import output_todo_record
from . import check_todo_records


def execute():
    print()
    print("=== TODO管理 メニュー ===")

    while True:
        print_menu()
        no = input_util.input_int("メニューを選択してください : ")
        print()
        match no:
            case 1:
                create_todo_record.execute()
            case 2:
                show_todo_records.execute()
            case 3:
                update_todo_record.execute()
            case 4:
                delete_todo_record.execute()
            case 5:
                output_todo_record.execute()
            case 6:
                check_todo_records.execute()
            case 7:
                break
            case _:
                print("無効な値です")

    print("終了します")


def print_menu():
    print()
    print("1. TODO登録")
    print("2. TODO表示")
    print("3. TODO更新")
    print("4. TODO削除")
    print("5. TODO出力")
    print("6. TODO終了報告")
    print("7. 終了")
    print()


if __name__ == "__main__":
    execute()
