# TODO管理プログラム
# 入力されたメニュー選択番号ででtodo_recordsのモジュールを呼び出す

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util import input_util
from todo_records import t1_create_todo_record
from todo_records import t2_show_todo_records
from todo_records import t3_update_todo_record
from todo_records import t4_delete_todo_record
from todo_records import t5_output_todo_record
from todo_records import t6_check_todo_records


def execute():
    print("=== TODO管理 メニュー ===")

    # メニューの表示
    print_menu()

    while True:
        no = input_util.input_int("メニューを選択してください : ")

        if no == 1:
            t1_create_todo_record.execute()
        elif no == 2:
            t2_show_todo_records.execute()
        elif no == 3:
            t3_update_todo_record.execute()
        elif no == 4:
            t4_delete_todo_record.execute()
        elif no == 5:
            t5_output_todo_record.execute()
        elif no == 6:
            t6_check_todo_records.execute()
        elif no == 7:
            print("終了します")
            break
        else:
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
