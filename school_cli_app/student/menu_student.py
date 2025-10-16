import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from student import select_all_student
from student import find_by_id_student
from student import create_student2
from student import update_student
from student import delete_student
from util import inpututil


def execute():
    print("*** 学生管理 ***")
    print_menu()

    while True:
        print("1~6までの整数を入力してください")
        no = inpututil.input_int("メニュー番号を入力してください : ")

        # 番号によってモジュールの関数を実行
        if no == 1:
            select_all_student.execute()
        elif no == 2:
            find_by_id_student.execute()
        elif no == 3:
            create_student2.execute()
        elif no == 4:
            update_student.execute()
        elif no == 5:
            delete_student.execute()
        elif no == 6:
            print("操作を終了します")
            break
        else:
            print("無効な値です")


def print_menu():
    print("1: 一覧表示")
    print("2: 検索")
    print("3: 登録")
    print("4: 更新")
    print("5: 削除")
    print("6: 終了")


if __name__ == "__main__":
    execute()
