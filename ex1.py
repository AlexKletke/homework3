# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

size = int(input('enter quantity of the numbers: '))
import random
list = [random.randint(-100, 100) for i in range(size)]
print(*list)
summa = 0
for j in range(1, size, 2):
    summa += list[j]
    j += 2
print(f'the sum of numbers with an odd index in the list = {summa}')
