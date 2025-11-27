students = [
    {"id": "1", "name": "佐藤 琢磨", "birthday": "1977-01-28", "class": "CG"},
    {"id": "2", "name": "大塚 愛", "birthday": "1982-09-09", "class": "Web"},
    {"id": "3", "name": "藤井 隆", "birthday": "1972-03-10", "class": "Web"},
    {"id": "4", "name": "福原 愛", "birthday": "1988-11-01", "class": "CG"},
    {"id": "5", "name": "大黒 将志", "birthday": "1980-05-04", "class": None},
]


def find_student():
    """学生情報を検索する"""
    print("#-- 学生検索 --#")

    id = input("IDを入力してください: ")

    for student in students:
        if student["id"] == id:
            print(
                f"ID: {student['id']}, 名前: {student['name']}, 生年月日: {student['birthday']}, クラス: {student['class']}"
            )
            return

    print("そのIDの学生は存在しません")


if __name__ == "__main__":
    find_student()
