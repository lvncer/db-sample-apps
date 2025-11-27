def create_student_multi():
    """複数の学生情報を入力して辞書のリストに保存し、登録内容を表示する"""
    print("#-- 学生登録 --#")

    # 登録人数を入力
    count = int(input("登録人数を入力してください: "))
    print()

    # 学生情報を格納するリスト
    students = []

    # 指定された人数分ループ
    for i in range(count):
        print(f"-- {i + 1}人目 --")

        # 各項目の入力を受け取る
        student_id = input("IDを入力してください: ")
        name = input("名前を入力してください: ")
        birth_date = input("生年月日を入力してください: ")
        class_name = input("クラスを入力してください: ")

        # 辞書に保存
        student = {
            "id": student_id,
            "name": name,
            "birth_date": birth_date,
            "class": class_name,
        }

        # リストに追加
        students.append(student)
        print()

    # 登録内容を表示
    print("-- 以下の内容を登録しました --")
    for student in students:
        print(
            f"ID: {student['id'].rjust(2)}, 名前:{student['name']}, 生年月日: {student['birth_date']} クラス: {student['class']}"
        )

    return students


if __name__ == "__main__":
    create_student_multi()
