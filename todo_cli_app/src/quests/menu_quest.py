from ..db import access_enemy
from ..db import access_level
from ..db import access_users
from ..util import input_util
from ..util import db_util
import mysql.connector
import random


# 主人公攻撃時にフラグを処理して敵のHPを減少させる
def myAttackFlagCheck(
        enemies_hp,
        my_power,
        my_boost_flag,
        my_critical_flag,
        enemies_defence_flag
):
    my_attack_hp = my_power * my_boost_flag * my_critical_flag / enemies_defence_flag
    enemies_hp -= my_attack_hp
    print(f'{my_attack_hp}ダメージ与えました')
    return enemies_hp


# 敵攻撃時にフラグを処理して主人公のHPを減少させる
def enemiesAttackFlagCheck(
        my_hp,
        enemies_power,
        enemies_boost_flag,
        enemies_critical_flag,
        my_defence_flag
):
    enemies_attack_hp = enemies_power * enemies_boost_flag * enemies_critical_flag / my_defence_flag
    my_hp -= enemies_attack_hp
    print(f'{enemies_attack_hp}ダメージ受けました')
    return my_hp


def print_my_menu():
    print("*** 主人公のターン ***")
    print()
    print("1. 攻撃")
    print("2. 回復")
    print("3. 防御")
    print("4. ダメージブースト")
    print("5. あきらめる")
    print()


def execute():
    try:
        # mysqlに接続
        cnx = db_util.connect()
        # カーソルを作成
        cursor = cnx.cursor(dictionary=True)

        print("*** クエスト ***")

        name = input_util.input_replace("ユーザ名を入力してください : ")

        # userテーブルに存在するかを確認する
        user_rows = access_users.find_by_name_user(cursor, name)

        # ユーザが存在し、整合性がとれたならクエストを開始する
        if len(user_rows) != 0:
            # 主人公の情報からステータスを取得する--------------------------------------------------------------------------------------------------------------------
            now_exp = user_rows[0]["experience"]
            my_level = 1
            while True:
                required_exp = access_level.find_status(
                    cursor, my_level
                )
                required_exp = required_exp[0]["required_experience"]
                if now_exp < required_exp:
                    my_level -= 1
                    break
                my_level += 1
            my_status = access_level.find_status(cursor, my_level)
            my_power = my_status[0]["power"]
            my_hp = my_status[0]["health"]

            # 進捗から敵の情報を取得する------------------------------------------------------------------------------------------------------------------------------
            progress = user_rows[0]["progress"]
            enemies_info = access_enemy.find_by_progress(
                cursor, progress
            )
            enemies_name = enemies_info[0]['name']
            enemies_level = enemies_info[0]['level']
            enemies_status = access_level.find_status(
                cursor, enemies_level
            )
            enemies_power = enemies_status[0]["power"]
            enemies_hp = enemies_status[0]["health"]

            print()
            print("*** 次の敵 ***")
            print(f"敵の名前 : {enemies_name}")
            print(f"敵のレベル : {enemies_level}")
            print()

            # 開始確認----------------------------------------------------------------------------------------------------------------------------------------------
            confirm = db_util.confirming(
                "クエストを開始しますか? [y/n]"
            )
            print()

            # Yが入力されたならばクエストを開始する-------------------------------------------------------------------------------------------------------------------
            if confirm:
                print_my_menu()
                my_defence_flag = 1
                my_critical_flag = 1
                my_boost_flag = 1
                enemies_defence_flag = 1
                enemies_critical_flag = 1
                enemies_boost_flag = 1
                heal_used_flag = 0
                # 戦闘を開始する------------------------------------------------------------------------------------------------------------------------------------
                while True:
                    print("*** 戦闘 ***")
                    print(f"主人公のHP : {my_hp}")
                    print(f"敵のHP : {enemies_hp}")
                    print()

                    while True:
                        command = input_util.input_int(
                            "コマンドを入力してください : "
                        )
                        # 主人公の攻撃
                        if command in [1, 2, 3, 4, 5]:
                            break
                        print("入力は1, 2, 3, 4, 5から選んでください")
                        print_my_menu()
                    print()

                    # 攻撃する
                    if command == 1:
                        print('*** 主人公が攻撃しました ***')
                        # 20%の確率でクリティカル攻撃
                        critical_probability = 0.2
                        if random.uniform(0, 1) < critical_probability:
                            print('クリティカル攻撃！')
                            my_critical_flag = 2
                        # 敵のHPを減少させる
                        enemies_hp = myAttackFlagCheck(
                            enemies_hp,
                            my_power,
                            my_boost_flag,
                            my_critical_flag,
                            enemies_defence_flag
                        )
                        # フラグを初期化する
                        enemies_defence_flag = 1
                        my_critical_flag = 1

                        # 敵のHPが0になったらクエストをクリアする
                        if enemies_hp <= 0:
                            print("*** 敵のHPが0になりました ***")
                            # 勝った場合、データベースの進捗に記録する
                            victory(progress, cursor, name, cnx)
                            break

                    # 回復する
                    # すでに1度回復した場合は、もう一度選択させる
                    elif command == 2:
                        if heal_used_flag == 1:
                            print("*** 回復は使えません ***")
                            print()
                            continue
                        else:
                            print("*** 回復します ***")
                            print(f'{my_power}hp 回復しました')
                            my_hp += my_power
                            heal_used_flag = 1

                    # 防御する
                    elif command == 3:
                        my_defence_flag = 10
                        print('防御します')

                    # ダメージブーストする
                    elif command == 4:
                        my_boost_flag = 3
                        print('ダメージブーストします')
                        print('次のターンで攻撃力が3倍になります!')

                    # 5が入力されたらクエストをあきらめる
                    elif command == 5:
                        print('クエストをあきらめます')
                        break
                    print()

                    # 敵のターン-----------------------------------------------------------------------------------------------------------------------------------------
                    print('*** 敵のターン ***')
                    print()

                    attack = 0.6  # 60%の確率で攻撃
                    heal = 0.15   # 15%の確率で回復
                    defend = 0.1  # 10%の確率で防御
                    boost = 0.1   # 10%の確率でダメージブースト
                    rest = 0.05   # 5%の確率で休憩
                    action = random.choices(
                        ['attack', 'heal', 'defend', 'boost', 'rest'],
                        weights=[
                            attack, heal, defend, boost, rest
                        ]
                    )[0]

                    if action == "attack":
                        print('敵が攻撃しました！')
                        # 20%の確率でクリティカル攻撃
                        critical_probability = 0.2
                        if random.uniform(0, 1) < critical_probability:
                            print('クリティカル攻撃！')
                            enemies_critical_flag = 2
                        my_hp = enemiesAttackFlagCheck(
                            enemies_hp,
                            enemies_power,
                            enemies_boost_flag,
                            enemies_critical_flag,
                            my_defence_flag
                        )
                        enemies_boost_flag = 1
                        enemies_critical_flag = 1
                        my_defence_flag = 1
                        if my_hp <= 0:
                            print()
                            print("*** あなたのHPが0になりました ***")
                            # 負けた場合、負けたと表示する
                            print()
                            print("*** クエストクリア失敗 ***")
                            print()
                            break

                    elif action == 'heal':
                        print('敵が回復しました！')
                        enemies_hp += enemies_power

                    elif action == 'defend':
                        print('敵が防御しました！')
                        enemies_defence_flag = 10

                    elif action == 'boost':
                        print('敵がダメージブーストしました！')
                        enemies_boost_flag = 3

                    elif action == 'rest':
                        print('敵は休んでいる...')
                    print()

            # nが入力されたならばクエストをキャンセルする
            else:
                print("クエストをキャンセルしました")
                print()

        # usersテーブルにユーザが存在しないならばクエストを開始しない
        else:
            print("[Error] そのユーザ名は存在しません")
            print()

    except mysql.connector.Error as e:
        print("エラーが発生しました")
        print(e)

    # 終了処理
    finally:
        cursor.close()
        cnx.close()


def victory(progress, cursor, name, cnx):
    print()
    print("*** クエストクリア ***")
    print("*** 進捗を更新します ***")
    print()

    # 進捗を更新する
    progress += 1
    access_users.update_progress(
        cursor, name, progress
    )
    cnx.commit()


if __name__ == "__main__":
    execute()
