import mysql.connector


def connect():
    cnx = mysql.connector.connect(
        host="localhost", user="root", password="password", database="bmiapp"
    )

    # コネクションが切れたときに再接続する
    cnx.ping(reconnect=True)

    return cnx


def confirming(prompt):
    while True:
        message = input(prompt).strip().lower()

        if message == "y":
            return True
        elif message == "n":
            return False
        else:
            print("Yかnで入力してください")


# BMIによる肥満度の判定
def calc_fat_level(bmi, age):
    fat_level = ""

    if age < 18:
        fat_level = "未計算"
    elif 18 <= age < 50:
        if bmi < 18.5:
            fat_level = "痩せ"
        elif 18.5 <= bmi < 25:
            fat_level = "普通"
        elif 25 <= bmi < 30:
            fat_level = "やや肥満"
        else:
            fat_level = "肥満"
    elif 50 <= age < 70:
        if bmi < 20:
            fat_level = "痩せ"
        elif 20.0 <= bmi < 25:
            fat_level = "普通"
        elif 25 <= bmi < 30:
            fat_level = "やや肥満"
        else:
            fat_level = "肥満"
    elif age >= 70:
        if bmi < 21.5:
            fat_level = "痩せ"
        elif 21.5 <= bmi < 25:
            fat_level = "普通"
        elif 25 <= bmi < 30:
            fat_level = "やや肥満"
        else:
            fat_level = "肥満"

    return fat_level


# 残りの平均体重への体重の差を計算する
def calc_remain_standard(weight_kg, standard_weight):
    # 残りの平均体重への体重の差
    remain_standard = weight_kg - standard_weight
    # 小数点以下第1桁まで表示する
    remain_standard = round(remain_standard, 1)

    # もし差がマイナスならば絶対値をとってプラスにしておく
    remain_standard = abs(remain_standard)

    return remain_standard


def calc_remain_target(weight_kg, target_weight):
    # 残りの目標体重への体重の差
    remain_target = weight_kg - target_weight
    # 小数点以下第1桁まで表示する
    remain_target = round(remain_target, 1)

    # もし差がマイナスならば絶対値をとってプラスにしておく
    remain_target = abs(remain_target)

    return remain_target


def play_sound(texts):
    import time

    for text in texts:
        for n in text:
            print(n, end="")

        print()
        time.sleep(1)
