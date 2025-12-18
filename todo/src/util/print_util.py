from ..db.user import User
from ..db.todo_record import TodoRecord


def print_user(user: User | None) -> None:
    if user:
        print()
        print(f"ユーザ名: {user.name}")
        print(f"生年月日: {user.birthday}")
        print(f"経験値: {user.experience}")
        print(f"敵撃破状況: {user.progress - 1} 体")
    else:
        print()
        print("[Error] そのユーザ名は存在しません")


def print_todo_record(todo_record: TodoRecord) -> None:
    if todo_record:
        print()
        print(f"id: {todo_record.id}")
        print(f"タイトル: {todo_record.title}")
        print(f"日付: {todo_record.deadline}")
        print(f"優先度: {todo_record.priority}")
