# Задача 5*. (Необязательная). Двумерный массив размером 5х5 заполнен случайными нулями и единицами. 
# Игрок может ходить только по полям, заполненным единицами. Проверьте, существует ли путь из точки [0, 0] в точку [4, 4] (эти поля требуется принудительно задать равными единице).

import random
import queue

# Создаем случайный двумерный массив размером 5x5
grid = [[0 for j in range(5)] for i in range(5)]
for i in range(5):
    for j in range(5):
        if random.random() < 0.5:
            grid[i][j] = 1

# Задаем начальную и конечную точки
grid[0][0] = 1
grid[4][4] = 1

start = (0, 0)
end = (4, 4)

# Функция для проверки, можно ли переместиться в заданные координаты
def is_valid_move(x, y):
    if x < 0 or x >= 5 or y < 0 or y >= 5:
        return False
    return grid[x][y] == 1

# Очередь для BFS
q = queue.Queue()
q.put(start)

# Массив для хранения уже посещенных точек
visited = set()
visited.add(start)

# Пока очередь не пуста, продолжаем поиск
while not q.empty():
    curr = q.get()
    if curr == end:
        print("Путь существует")
        break
    x, y = curr
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        new_x, new_y = x + dx, y + dy
        if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
            q.put((new_x, new_y))
            visited.add((new_x, new_y))
else:
    print("Пути не существует")

# Выводим двумерный массив
print("Двумерный массив:")
for row in grid:
    print(row)
