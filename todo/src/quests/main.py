from pickle import TRUE
from ..db import access_enemy
from ..db import access_level
from ..db import access_users
from ..util import input_util
from ..util import db_util
import mysql.connector
import random


CRITICAL_PROBABILITY = 0.2


def execute():
    try:
        cnx = db_util.connect()
        cursor = cnx.cursor(dictionary=True)

        print()
        print("クエスト")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        user = access_users.find_by_name(cursor, name)
        if user:
            (
                user_level,
                user_power,
                user_hp,
                progress,
                enemies_name,
                enemies_level,
                enemies_power,
                enemies_hp,
            ) = get_user_stats(cursor, user)

            print()
            print(f"敵の名前 : {enemies_name}")
            print(f"敵のレベル : {enemies_level}")
            print()

            confirm = input_util.is_confirm("クエストを開始しますか? [y/n] : ")
            if confirm:
                is_user_defence = False
                is_user_critical = False
                is_user_boost = False
                is_enemies_defence = False
                is_enemies_critical = False
                is_enemies_boost = False

                while True:
                    print()
                    print(f"主人公のHP : {user_hp}")
                    print(f"敵のHP : {enemies_hp}")
                    print()
                    print_my_menu()
                    print()

                    # 主人公のターン
                    user_action_result = user_action(
                        enemies_hp,
                        user_power,
                        is_user_boost,
                        is_user_critical,
                        is_enemies_defence,
                    )
                    if user_action_result[0] == "attack":
                        enemies_hp = user_action_result[1]

                    # 初期化
                    is_user_defence = False
                    is_user_boost = False

                    if user_action_result == "victory":
                        print("敵のHPが0になりました。")
                        print()
                        print("クエストクリアしました。")

                        victory(progress, cursor, name)
                        print("進捗を更新しました。")
                        break
                    elif user_action_result == "heal":
                        user_hp += user_power
                        print(f"{user_power}hp 回復しました")
                    elif user_action_result == "defence":
                        is_user_defence = True
                    elif user_action_result == "boost":
                        is_user_boost = True
                    elif user_action_result == "quit":
                        print("クエストをあきらめます")
                        break

                    # 初期化
                    is_enemies_defence = False
                    is_enemies_boost = False

                    # 敵のターン
                    enemies_action_result = enemies_action(
                        user_hp,
                        enemies_power,
                        is_enemies_boost,
                        is_enemies_critical,
                        is_user_defence,
                    )
                    if enemies_action_result == "loss":
                        print("敵のHPが0になりました")
                        print("クエスト失敗")
                        break
                    elif enemies_action_result[0] == "attack":
                        user_hp = enemies_action_result[1]
                    elif enemies_action_result == "heal":
                        enemies_hp += enemies_power
                        print(f"{enemies_power}hp 回復しました")
                    elif enemies_action_result == "defence":
                        is_enemies_defence = True
                    elif enemies_action_result == "boost":
                        is_enemies_boost = True
            else:
                print("クエストをキャンセルしました")
                print()
        else:
            print("[Error] そのユーザ名は存在しません")
            print()

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    else:
        cnx.commit()

    finally:
        cursor.close()
        cnx.close()


def user_attack(
    enemies_hp, user_attack_power, is_user_boost, is_user_critical, is_enemies_defence
):
    if is_user_boost:
        user_attack_power *= 3
    if is_user_critical:
        user_attack_power *= 2
    if is_enemies_defence:
        user_attack_power /= 2
    enemies_hp -= user_attack_power
    print(f"{user_attack_power}ダメージ与えました")
    return enemies_hp


def enemies_attack(
    user_hp, enemies_power, is_enemies_boost, is_enemies_critical, is_user_defence
):
    if is_enemies_boost:
        enemies_power *= 3
    if is_enemies_critical:
        enemies_power *= 2
    if is_user_defence:
        enemies_power /= 2
    user_hp -= enemies_power
    print(f"{enemies_power}ダメージ受けました")
    return user_hp


def print_my_menu():
    print("*** 主人公のターン ***")
    print()
    print("1. 攻撃")
    print("2. 回復")
    print("3. 防御")
    print("4. ダメージブースト")
    print("5. あきらめる")


def get_user_stats(cursor, user):
    now_exp = user.experience
    user_level = 1
    while True:
        required_exp = access_level.find_status(cursor, user_level)
        required_exp = required_exp[0]["required_experience"]
        if now_exp < required_exp:
            user_level -= 1
            break
        user_level += 1
    user_status = access_level.find_status(cursor, user_level)
    user_power = user_status[0]["power"]
    user_hp = user_status[0]["health"]

    # 進捗から敵の情報を取得する
    progress = user.progress
    enemies_info = access_enemy.find_by_progress(cursor, progress)
    enemies_name = enemies_info[0]["name"]
    enemies_level = enemies_info[0]["level"]
    enemies_status = access_level.find_status(cursor, enemies_level)
    enemies_power = enemies_status[0]["power"]
    enemies_hp = enemies_status[0]["health"]

    return (
        user_level,
        user_power,
        user_hp,
        progress,
        enemies_name,
        enemies_level,
        enemies_power,
        enemies_hp,
    )


# 主人公のコマンド入力
def user_action(
    enemies_hp, user_attack_power, is_user_boost, is_user_critical, is_enemies_defence
) -> str | tuple[str, int]:
    ATTACK_COMMAND = 1  # 攻撃
    HEAL_COMMAND = 2  # 回復
    DEFEND_COMMAND = 3  # 防御
    BOOST_COMMAND = 4  # ダメージブースト
    QUIT_COMMAND = 5  # あきらめる

    while True:
        command = input_util.input_int("コマンドを入力してください : ")
        if command in [
            ATTACK_COMMAND,
            HEAL_COMMAND,
            DEFEND_COMMAND,
            BOOST_COMMAND,
            QUIT_COMMAND,
        ]:
            break
        print("入力は1, 2, 3, 4, 5から選んでください")
        print_my_menu()
    print()

    if command == ATTACK_COMMAND:
        print("*** 主人公が攻撃しました ***")
        if random.uniform(0, 1) < CRITICAL_PROBABILITY:
            print("クリティカル攻撃！")
            is_user_critical = True

        enemies_hp = user_attack(
            enemies_hp,
            user_attack_power,
            is_user_boost,
            is_user_critical,
            is_enemies_defence,
        )
        if enemies_hp <= 0:
            return "victory"
        else:
            return "attack", enemies_hp

    elif command == HEAL_COMMAND:
        print("回復します")
        return "heal"

    elif command == DEFEND_COMMAND:
        print("防御します")
        return "defence"

    elif command == BOOST_COMMAND:
        print("ダメージブーストします")
        print("次のターンで攻撃力が3倍になります!")
        return "boost"

    elif command == QUIT_COMMAND:
        return "quit"


def enemies_action(
    user_hp, enemies_power, is_enemies_boost, is_enemies_critical, is_user_defence
) -> str | tuple[str, int]:
    print("*** 敵のターン ***")
    print()

    ENEMIES_ACTIONS = ["attack", "heal", "defend", "boost", "rest"]
    ENEMIES_ATTACK_PROBABILITY = 0.6
    ENEMIES_HEAL_PROBABILITY = 0.15
    ENEMIES_DEFEND_PROBABILITY = 0.1
    ENEMIES_BOOST_PROBABILITY = 0.1
    ENEMIES_REST_PROBABILITY = 0.05

    action = random.choices(
        ENEMIES_ACTIONS,
        weights=[
            ENEMIES_ATTACK_PROBABILITY,
            ENEMIES_HEAL_PROBABILITY,
            ENEMIES_DEFEND_PROBABILITY,
            ENEMIES_BOOST_PROBABILITY,
            ENEMIES_REST_PROBABILITY,
        ],
    )[0]

    if action == "attack":
        print("敵が攻撃しました！")
        if random.uniform(0, 1) < CRITICAL_PROBABILITY:
            print("クリティカル攻撃！")
            is_enemies_critical = True
        user_hp = enemies_attack(
            user_hp,
            enemies_power,
            is_enemies_boost,
            is_enemies_critical,
            is_user_defence,
        )
        if user_hp <= 0:
            print()
            print("あなたのHPが0になりました")
            print("クエスト失敗")
            print()
            return "loss"
        else:
            return "attack", user_hp
    elif action == "heal":
        print("敵が回復しました！")
        return "heal"
    elif action == "defend":
        print("敵が防御しました！")
        return "defence"
    elif action == "boost":
        print("敵がダメージブーストしました！")
        return "boost"
    elif action == "rest":
        print("敵は休んでいる...")
        return "rest"


def victory(progress, cursor, name):
    progress += 1
    access_users.update_progress(cursor, name, progress)


if __name__ == "__main__":
    execute()
