# В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.

def task_2():
    fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'peach', 'pear', 'pineapple', 'strawberry']
    letter = input('Введите букву: ')
    for fruit in fruits:
        if fruit.startswith(letter): # проверяем, начинается ли название фрукта с заданной буквы
            print(fruit) 

task_2()