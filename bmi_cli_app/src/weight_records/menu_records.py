# 学生管理プログラム
# キーボードで入力した情報でstudentテーブルを操作

from . import record_weight
from . import show_records
from . import delete_record
from . import output_records
from ..util import input_util


def execute():
    print("=== 体重管理 メニュー ===")

    # メニューの表示
    print_menu()

    while True:
        # キーボードからメニュー番号を入力させる
        no = input_util.input_int("メニューを選択してください : ")

        # 番号によってモジュールの関数を実行
        if no == 1:
            record_weight.execute()
        elif no == 2:
            show_records.execute()
        elif no == 3:
            delete_record.execute()
        elif no == 4:
            output_records.execute()
        else:
            print("操作を終了します")
            print()
            break


def print_menu():
    print("1. 体重記録")
    print("2. 記録表示")
    print("3. 記録削除")
    print("4. 記録出力")
    print("5. 終了")


if __name__ == "__main__":
    execute()
