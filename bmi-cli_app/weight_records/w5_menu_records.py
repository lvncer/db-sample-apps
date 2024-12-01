# 学生管理プログラム
# キーボードで入力した情報でstudentテーブルを操作

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from weight_records import w1_record_weight
from weight_records import w2_show_records
from weight_records import w3_delete_record
from weight_records import w4_output_records
from util import input_util


def execute():
    print("=== 体重管理 メニュー ===")

    # メニューの表示
    print_menu()

    while True:
        # キーボードからメニュー番号を入力させる
        no = input_util.input_int("メニューを選択してください : ")

        # 番号によってモジュールの関数を実行
        if no == 1:
            w1_record_weight.execute()
        elif no == 2:
            w2_show_records.execute()
        elif no == 3:
            w3_delete_record.execute()
        elif no == 4:
            w4_output_records.execute()
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
