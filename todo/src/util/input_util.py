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


def input_sort_order() -> str:
    while True:
        sort_order = input()
        match sort_order:
            case "1":
                return "priority"
            case "2":
                return "deadline"
            case _:
                print("1か2を入力してください")
                print("もう一度入力してください : ", end="")


def change_priority_to_string(priority: int) -> str | None:
    match priority:
        case 1:
            return "高"
        case 2:
            return "中"
        case 3:
            return "低"
        case _:
            return None


def change_deadline_to_empty_string(deadline: datetime.date) -> str | datetime.date:
    if deadline == datetime.date(9999, 12, 31):
        return ""
    return deadline
