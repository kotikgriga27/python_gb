# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.
def our_repeat(count):   
    def our_format(func):
        def decorator(*args):
            for i in range(count):
                for i in args:
                    print(f'{i} + ', end='')
                print('\b\b= ', end='')
                func(*args)
        return decorator
    return our_format

@our_repeat(3) 
def our_sum(a, b):
    print(a + b)

our_sum(5, 7)

