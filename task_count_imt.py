import sys

def input_dates():
    """Ввод и проверка исходных данных для расчета ИМТ"""
    dict_ = {"возраст": "полных лет", "пол": "м/ж", "рост": "см", "вес": "кг"}
    dict_in = {}
    s1, s2 = " ", "_"
    print(f"\n\n{s1 * 20} Приложение {s1 * 20}")
    print("по рассчёту индекса массы тела (ИМТ) мужчин и женщин")
    print(f"{s1 * 19} (возраст 19+) {s1 * 18}")
    print(s2 * 52)
    for key, value in dict_.items():
        while True:
            val_ = input(f"Укажите {key} ({value}): ")
            if key == "пол":
                if (val_ == "м" or val_ == "ж"): break
                else: continue
            elif not val_.isdigit() or float(val_) == 0:
                print(f"Ошибка, {key} должен быть натуральным числом.")
                continue
            elif key == "возраст" and float(val_) < 19:
                print(f"Ошибка, расчет ИМТ производится для возраста 19+.")
                continue
            # мальчики, 12 лет: не менее 143 см, максимальный известный рост 272 см:
            elif key == "рост"and (float(val_) < 143 or float(val_) > 272):
                print(f"Ошибка, укажите рост от 140 до 272 см.")
                continue
            # мальчики, 12 лет: не менее 33 кг, максимальный известный вес: 645 кг
            elif key == "вес"and (float(val_) < 33 or float(val_) > 645):
                print(f"Ошибка, укажите вес от 33 до 645 кг.")
                continue
            break
        dict_in[key]= val_
    return dict_in


def imt(d1, d2):
    """Поиск в таблице ИМТ в соответствии с исходными данными"""
    print("_" * 52)
    border_max = len(d1["age_min"]) - 1
    if not int(d2["возраст"]) >= int(d1["age_min"] [border_max]):
        border_mid = border_max // 2
        while True:
            if border_mid > 0 and int(d2["возраст"]) < int(d1["age_min"] [border_mid]):
                border_max = border_mid
                border_mid = border_mid // 2
                continue
            elif border_mid < border_max and int(d2["возраст"]) > int(d1["age_max"] [border_mid]):
                border_mid = border_mid + (border_max - border_mid) // 2
                continue
            break
        border_max = border_mid
    # искомая строка - возрастной диапазон:
    idx = d1["age_min"].index(d1["age_min"] [border_max])
    if d2["пол"] == "м":
        # ИМТ - мужчины:
        min_, max_ = "mid_min", "mid_max"
    else:
        # ИМТ - женщины:
        min_, max_ = "wid_min", "wid_max"
    count_ = int(d2["вес"]) / (int(d2["рост"]) / 100) ** 2
    if int(d1[min_] [idx]) <= count_ <= int(d1[max_] [idx]):
        print("Вес в норме \n\n")
    elif count_ > int(d1[max_] [idx]):
        x = round(((count_ - (int(d1[max_] [idx]))) * (int(d2["рост"]) / 100) ** 2), 2)
        y = round((int(d2["вес"]) - x), 2)
        print(f"Избыточный вес,\nдо нормы необходимо уменьшить вес на {x} кг до {y} кг \n\n")
    elif count_ < int(d1[min_] [idx]):
        x = round((((int(d1[min_] [idx])) - count_) * (int(d2["рост"]) / 100) ** 2), 2)
        y = round((int(d2["вес"]) + x), 2)
        print(f"Недостаточный вес,\nдо нормы необходимо добавить вес на {x} кг до {y} кг \n\n")
    return

# Таблица 1
dict_id_weight: dict[str, list[int]] = {
    "age_min": [19, 25, 35, 45, 55, 65], # Возраст
    "age_max": [24, 34, 44, 54, 64, 65],
    "mid_min": [20, 21, 22, 23, 24, 25], # Норма ИМТ для мужчин
    "mid_max": [25, 26, 27, 28, 29, 30],
    "wid_min": [19, 20, 21, 22, 23, 24], # Норма ИМТ для женщин
    "wid_max": [24, 25, 26, 27, 28, 29]
}

# Запуск приложения и корректный останов до завершения
try:
    # Запуск приложения
    imt(dict_id_weight, input_dates())
except KeyboardInterrupt:
    print("\n[!!!] Процесс прерван пользователем.")
    sys.exit(0) # Обработка прерывания и завершение приложения
