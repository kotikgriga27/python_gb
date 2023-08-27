# Задача 1. Создайте пользовательский аналог метода map().
def custom_map(func, numbers):
    return [func(x) for x in numbers]

def square(x):
    return x ** 2


numbers = [2, 3, 4, 5, 6, 7]
print(custom_map(square, numbers)) # [4, 9, 16, 25, 36, 49]