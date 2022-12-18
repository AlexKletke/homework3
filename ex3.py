# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

size = int(input('enter size of the list: '))
import random
list = [random.randint(100, 1000) for i in range(size)]
list1 = []
for j in range(size):
    list1.append(list[j]/100)
print(*list1)

list2 = []
for y in range(size):
    list2.append((list1[y]*100) % 100)
# print(*list2)
max_number = max(list2)
min_number = min(list2)
print((max(list2)-min(list2))/100)