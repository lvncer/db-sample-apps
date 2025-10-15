import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from student import menu_student
from exam import menu_exam
from util import inpututil


def execute():
    print("*** 学生成績管理 ***")

    # メニューの表示
    print_menu()

    while True:
        # キーボードからメニュー番号を入力させる
        print("1~3までの整数を入力してください")
        no = inpututil.input_int("メニュー番号を入力してください : ")

        # 番号によってモジュールの関数を実行
        if no == 1:
            menu_student.execute()
        elif no == 2:
            menu_exam.execute()
        elif no == 3:
            print("操作を終了します")
            break
        else:
            print("無効な値です")


def print_menu():
    print("1: 学生管理")
    print("2: 成績管理")
    print("3: 終了")


if __name__ == "__main__":
    execute()
