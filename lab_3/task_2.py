# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, sign = ','):
    mn1 = set(group1.split(sign))
    mn2 = set(group2.split(sign))
    return sorted(mn1.intersection(mn2))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))