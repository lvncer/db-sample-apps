from ..db.user import User


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
