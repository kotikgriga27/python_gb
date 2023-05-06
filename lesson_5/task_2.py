# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

import random

lst = [random.randint(0, 20) for _ in range(10)]
print(lst)

def increasing_subsequences(lst):
    if not lst:
        return [[]]
    incl_subseq = []
    for i, item in enumerate(lst): # enumerate() - возвращает кортеж (индекс, значение)
        subseq = increasing_subsequences(lst[i+1:])
        for seq in subseq:
            if not seq or item <= seq[0]:
                incl_subseq.append([item] + seq)
    return incl_subseq # возвращает список возрастающих последовательностей

subsequences = increasing_subsequences(lst)
result = max(subsequences, key=len) # возвращает самую длинную последовательность
print(result)
