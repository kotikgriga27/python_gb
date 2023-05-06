# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

for i in range(2):
        for j in range(2):
            for k in range(2):
                print(f"{i}\t{j}\t{k}\t{int( not (i and j) or k) }")