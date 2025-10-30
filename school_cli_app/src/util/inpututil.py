import datetime


# キーボードの入力内容を整数で返します
def input_int(prompt: str) -> int:
    while True:
        str = input(prompt)

        # 整数チェック
        if not str.isdigit():
            print("エラー!!!: 整数で入力してください")
            continue

        break

    return int(str)


# キーボードの入力内容を日付で返します
def input_date(prompt: str) -> str:
    while True:
        str = input(prompt)

        try:
            datetime.datetime.strptime(str, "%Y-%m-%d")
        except ValueError:
            print("エラー!!!: 日付で入力してください")
            continue

        break

    return str


def input_replace(prompt: str) -> str:
    str = input(prompt).strip()

    return str
