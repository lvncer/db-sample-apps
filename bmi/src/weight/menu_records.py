from . import record_weight
from . import show_records
from . import delete_record
from . import output_records
from ..util import input_util


def execute():
    print("=== 体重管理 メニュー ===")
    print_menu()

    while True:
        no = input_util.input_int("メニューを選択してください : ")

        match no:
            case 1:
                record_weight.execute()
            case 2:
                show_records.execute()
            case 3:
                delete_record.execute()
            case 4:
                output_records.execute()
            case 5:
                print("操作を終了します")
                return
            case _:
                print("無効な値です")


def print_menu():
    print("1. 体重記録")
    print("2. 記録表示")
    print("3. 記録削除")
    print("4. 記録出力")
    print("5. 終了")


if __name__ == "__main__":
    execute()
