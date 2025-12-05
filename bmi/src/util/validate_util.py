def validate_weight(weight: float) -> bool:
    if weight <= 0:
        print("体重は正の値を入力してください")
        return False
    elif weight > 1000:
        print("体重は1000kg未満の値を入力してください")
        return False
    else:
        return True
