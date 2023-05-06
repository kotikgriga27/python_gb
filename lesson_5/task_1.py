# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random

def task_1():
    list_ = []
    for i in range(10):
        list_.append(random.randint(1, 10))
    print(list_)
    print(list(filter(lambda x: x > 5, list_)))

task_1()