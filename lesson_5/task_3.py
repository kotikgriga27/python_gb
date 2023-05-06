# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают 
# Список уникальных элементов [1, 4, 2, 3, 6, 7]

import random

def count_duplicates(lst):
    if not lst:
        return 0
    else:
        count = count_duplicates(lst[1:])
        if lst[0] in lst[1:]:
            return count + 1
        else:
            return count

def remove_duplicates(lst):
    if not lst:
        return []
    else:
        rest = remove_duplicates(lst[1:])
        if lst[0] in rest:
            return rest
        else:
            return [lst[0]] + rest

# генерируем случайный список чисел
lst = [random.randint(1, 10) for _ in range(10)]

# выводим список и количество совпадающих элементов
print("Исходный список:", lst)
print("Количество совпадающих элементов:", count_duplicates(lst))

# удаляем повторяющиеся элементы
lst = remove_duplicates(lst)

# выводим список без повторяющихся элементов
print("Список без повторяющихся элементов:", lst)
