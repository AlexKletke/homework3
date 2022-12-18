# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input('enter number: '))
ReverseBinaryNumber = []
for i in range(n, 1, -1):
    ReverseBinaryNumber.append(n-((n//2)*2))
    n = n//2
    if n == 1:
        break
ReverseBinaryNumber.append(n)
print(*list(reversed(ReverseBinaryNumber)))   
