# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

import random

def check_sequence(array, number):
    for i in range(len(array) - 2):
        if array[i] == number // 100 and array[i + 1] == number // 10 % 10 and array[i + 2] == number % 10:
            return True
    return False

array = [random.randint(0, 9) for _ in range(15)]
number = int(input('Введите трёхзначное число: '))
print(array)
print('Да' if check_sequence(array, number) else 'Нет')