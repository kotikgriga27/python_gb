# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396
# с помощью списков


def task_1():
    n = input('Введите число: ')
    n_list = list(n)
    n_list_2 = n_list + n_list
    n_list_3 = n_list_2 + n_list
    n_list = int(''.join(n_list))
    n_list_2 = int(''.join(n_list_2))
    n_list_3 = int(''.join(n_list_3))
    print(n_list + n_list_2 + n_list_3)

task_1()