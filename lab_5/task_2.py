# TODO импортировать необходимые модули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """Функция осуществляет конвертирование файла input.csv в файл output.json"""
    # Открыть файл input.csv на чтение и файл output.json (будет создан) на запись
    with open(INPUT_FILENAME, 'r', encoding="utf-8") as input_f,\
        open('output.json', mode='w', encoding='utf-8') as output_f:
        # TODO считать содержимое csv файла
        read_ = csv.DictReader(input_f, delimiter=',', lineterminator='\n')
        # Преобразование в список (словарей)
        data_ = list(read_)
        # TODO Сериализовать в файл с отступами равными 4
        json.dump(data_, output_f, indent=4, ensure_ascii=False)
    return


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")