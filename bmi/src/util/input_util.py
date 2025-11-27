import datetime


# キーボードの入力内容を整数で返します
def input_int(prompt):
    while True:
        str = input(prompt)

        # 整数チェック
        if not str.isdigit():
            print("[Error] 整数で入力してください")
            continue

        break

    return int(str)


def confirming(prompt):
    while True:
        message = input(prompt).strip().lower()

        if message == "y":
            return True
        elif message == "n":
            return False
        else:
            print("Yかnで入力してください")


# キーボードの入力内容を小数で返します
def input_float(prompt):
    while True:
        str = input(prompt)

        # 整数チェック
        if not str.isdigit():
            print("[Error] 整数か小数で入力してください")
            continue

        break

    return float(str)


# キーボードの入力内容を日付で返します
def input_date(prompt):
    while True:
        str = input(prompt)

        try:
            datetime.datetime.strptime(str, "%Y-%m-%d")

        except ValueError:
            print("[Error] 指定された日付で入力してください [%Y-%m-%d]")
            continue

        break

    return str


# 入力された日付の形式で入力させる
def input_month(prompt):
    while True:
        str = input(prompt)

        try:
            datetime.datetime.strptime(str, "%Y-%m")
        except ValueError:
            print("[Error] 指定された日付の形式で入力してください [%Y-%m]")
            continue

        break

    return str


# 前後のスペースを取り除き、返す
def input_replace(prompt):
    str = input(prompt).strip()

    return str
