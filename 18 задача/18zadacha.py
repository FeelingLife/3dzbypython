# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


import random


N = int(input("Введите число N - "))
list_1 = [random.randint(1, 20) for i in range(N)]
print("Массив - ", list_1)
x = int(input("Введите число X - "))
count = 0
min_number = abs(x - list_1[0])
for i in range(1, N):
    time_number = abs(x - list_1[i])
    if time_number < min_number:
        min_number = time_number
        count = i
print(f"Самый близкий по величине элемент к заданному числу {list_1[count]}")