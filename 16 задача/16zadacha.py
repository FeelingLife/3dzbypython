# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.


import random

N = int(input("Введите число N - "))
list_1 = [random.randint(1, 20) for i in range(N)]
print("Введеный массив - ", list_1)
array = list(map(int, list_1))
X = int(input("Введите число X - "))
count = 0
for i in range(N):
    if array[i] == X:
        count += 1
print(f"Число {X} встречается в списке А {count} раз(а)")