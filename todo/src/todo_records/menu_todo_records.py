from ..util import input_util
from . import create_todo_record
from . import show_todo_records
from . import update_todo_record
from . import delete_todo_record
from . import output_todo_record
from . import check_todo_records


def execute():
    print("=== TODO管理 メニュー ===")
    print_menu()

    while True:
        no = input_util.input_int("メニューを選択してください : ")
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
                print("終了します")
                break
            case _:
                print("無効な値です")
                print_menu()


def print_menu():
    print("1. TODO登録")
    print("2. TODO表示")
    print("3. TODO更新")
    print("4. TODO削除")
    print("5. TODO出力")
    print("6. TODO終了報告")
    print("7. 終了")


if __name__ == "__main__":
    execute()
