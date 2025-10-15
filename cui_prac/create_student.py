def create_student():
    """学生情報を入力して辞書に保存し、登録内容を表示する"""
    print("#-- 学生登録 --#")

    # 各項目の入力を受け取る
    student_id = input("IDを入力してください: ")
    name = input("名前を入力してください: ")
    birth_date = input("生年月日を入力してください: ")
    class_name = input("クラスを入力してください: ")

    # 登録内容を表示
    print("\n-- 以下の内容を登録しました --")
    print(f"ID: {student_id}, 名前:{name}, 生年月日: {birth_date} クラス: {class_name}")

    return


if __name__ == "__main__":
    create_student()
