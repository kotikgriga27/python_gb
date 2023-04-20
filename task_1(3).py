# Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.

def fib(n):
    result = []
    a, b = 1, 1
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    return result

print(fib(6))