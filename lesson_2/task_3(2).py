# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

s_1 = input('Введите первую строку: ')
s_2 = input('Введите вторую строку: ')

for i in range(len(s_1)):
    count = 0
    for j in range(len(s_2)):
        if s_1[i] == s_2[j]:
            count += 1
    print(f'{count}', end = ' ')