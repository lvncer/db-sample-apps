import datetime


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


def calc_age(birthday):
    d_today = datetime.datetime.now()
    age = (
        d_today.year
        - birthday.year
        - ((d_today.month, d_today.day) < (birthday.month, birthday.day))
    )
    return age


def calc_metrics_from_values(
    height_cm, weight_kg, target_weight, birthday, record_date
):
    height_cm = float(height_cm)
    weight_kg = float(weight_kg)
    target_weight = float(target_weight)

    height_m = height_cm / 100
    bmi = round(weight_kg / (height_m**2), 1)
    standard_weight = round(height_m**2 * 22, 1)

    age = calc_age(birthday)
    fat_level = calc_fat_level(bmi, age)
    remain_standard = calc_remain_standard(weight_kg, standard_weight)
    remain_target = calc_remain_target(weight_kg, target_weight)

    return (
        height_cm,
        weight_kg,
        target_weight,
        record_date,
        bmi,
        standard_weight,
        fat_level,
        remain_standard,
        remain_target,
    )


def calc_weight_record_metrics(weight_record, birthday):
    return calc_metrics_from_values(
        weight_record.height,
        weight_record.weight,
        weight_record.target_weight,
        birthday,
        weight_record.record_date,
    )


def is_birthday_today(birthday):
    d_today = datetime.datetime.now()
    return d_today.month == birthday.month and d_today.day == birthday.day
