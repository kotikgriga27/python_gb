# Задача 4*. Даны два списка, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 2. 3x^2 + x + 8
# 3. Результат: 8x^2 + 4x + 8

def task_4():
    first_polynomial = [5, 3, 0]
    second_polynomial = [3, 1, 8]
    result = []
    for i in range(len(first_polynomial)):
        result.append(first_polynomial[i] + second_polynomial[i])
    print(f'Результат: {result[0]}x^2 + {result[1]}x + {result[2]}')

task_4()