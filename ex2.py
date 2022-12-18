# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];
size = int(input('enter size of the list: '))
import random
list = [random.randint(-10, 10) for i in range(size)]
print(*list)
ProductOfNumbers = []
if size % 2 == 0:
    for j in range(int(size/2)):
        ProductOfNumbers.append(list[j] * list[size-1-j])
else:
    for j in range(int(size/2)):
        ProductOfNumbers.append(list[j] * list[size-1-j])
    ProductOfNumbers.append(list[int(size/2)])
print(ProductOfNumbers)



