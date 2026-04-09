# TODO решите задачу
import json


def task() -> float:
    """функция осуществляет преобразование содержимого файла input.json
    в список словарей, находит сумму произведений двух значений каждого
    словаря по ключам "score" и "weight", суммирует произведения и
    возвращает результат округлённый до 3-х знаков после запятой"""
    filename = "input.json"
    # открыть файл json для чтения и преобразовать в список
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
    count = 0

    # перебор элементов списка (словарей) по ключам "score" и "weight"
    for item in data:
        count += (item["score"] * item["weight"])

    return round(count, 3)


print(task())
