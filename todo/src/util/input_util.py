import datetime


# 前後のスペースを取り除き、返す
def input_replace(prompt):
    str = input(prompt).strip()

    return str


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


def input_deadline(prompt):
    str = input(prompt)

    try:
        datetime.datetime.strptime(str, "%Y-%m-%d")
    except ValueError:
        print("指定された日付で入力されていないため期限を未定義にしました")
        return "9999-12-31"
    return str


def is_confirm(prompt) -> bool:
    user_input = input(prompt).strip().lower()
    if user_input == "y":
        return True
    return False


def input_priority(prompt):
    while True:
        str = input(prompt)

        if str not in ["1", "2", "3"]:
            print("[Error] 数値は1, 2, 3から選んでください")
            continue
        break
    return str


def input_sort_order():
    while True:
        sort_order = input()

        if sort_order == "1":
            sort_prompt = "priority"
            break
        elif sort_order == "2":
            sort_prompt = "deadline"
            break
        else:
            print("1か2を入力してください")
            print("もう一度入力してください : ", end="")
            continue
    return sort_prompt
