# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

n = int(input('Введите число: '))

count = 1
while count <= n:
    if count % 2 == 0:
        print(count)
    count += 1