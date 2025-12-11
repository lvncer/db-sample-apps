def print_weight_metrics(**kwargs):
    print()

    if "id" in kwargs:
        print(f"id: {kwargs['id']}")
    if "record_date" in kwargs:
        print(f"日付: {kwargs['record_date']}")
    if "height_cm" in kwargs:
        print(f"身長: {kwargs['height_cm']}")
    if "weight_kg" in kwargs:
        print(f"体重: {kwargs['weight_kg']}")
    if "bmi" in kwargs:
        print(f"BMI: {kwargs['bmi']}")
    if "standard_weight" in kwargs and "remain_standard" in kwargs:
        print(
            f"標準体重: {kwargs['standard_weight']} (あと{kwargs['remain_standard']}kg)"
        )
    if "fat_level" in kwargs:
        print(f"肥満度: {kwargs['fat_level']}")
    if "target_weight" in kwargs and "remain_target" in kwargs:
        print(f"目標体重: {kwargs['target_weight']} (あと{kwargs['remain_target']}kg)")

    print()
    return
