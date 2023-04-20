# Задача 1. Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.

def prime_factors(n):
    result = []
    i = 2
    while i <= n:
        if n % i == 0:
            result.append(i)
            n /= i
        else:
            i += 1
    return result

print(prime_factors(60))