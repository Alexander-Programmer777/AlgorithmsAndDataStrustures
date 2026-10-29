"""
1. Массив разбивается на отсортированную и неотсортированную части
2. Берем элемент в неотсортированной части массива
3. Находим место элемента в отсорованной части массива и вставляем
"""

#O(n^2), sustainable

from random import randint
N = 100
a = []
for i in range(N):
    a.append(randint(-100, 100))

print(a)

# более очев, но много ненужных свопов
for i in range(1, N):
    j = i
    while (j != 0) and (a[j] < a[j - 1]):
        a[j - 1], a[j] = a[j], a[j - 1]
        j -= 1

# меньше свопов
for i in range(1, N):
    j = i
    pivot = a[i]
    while (j != 0) and (a[j - 1] > pivot):
        a[j] = a[j - 1]
        j -= 1
    a[j] = pivot

print(a)

print(a == sorted(a))
