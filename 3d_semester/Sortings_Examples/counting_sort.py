"""
Применение сортировки подсчётом целесообразно лишь тогда,
когда сортируемые числа имеют (или их можно отобразить в)
диапазон возможных значений, который достаточно мал по сравнению
с сортируемым множеством, например, миллион натуральных чисел меньших 1000.
"""

# O(n) but efficient rarely, unsustainable
# можно сделать устойчивой и использовать в ЛСД сортировке


import random

# for 0 and positive numbers

#N = random.randint(10, 100)
N = 10_000
a = []
for i in range(N):
    a.append(random.randint(0, 100))
print(a)

cnt = [0] * (max(a) + 1)  # O(k)

for elem in a:      # O(n)
    cnt[elem] += 1

result = []
# O(n + k)
for i in range(len(cnt)): # k итераций
    for j in range(cnt[i]): # в сумме здесь n итераций для всех k
        result.append(i)

print(result)


"""
# Для работы с отрицательными числами
min_val = min(a)
max_val = max(a)
cnt = [0] * (max_val - min_val + 1)

for elem in a:
    cnt[elem - min_val] += 1  # смещение индекса min from 0

result = []
for i in range(len(cnt)):
    for j in range(cnt[i]):
        result.append(i + min_val)  # обратное смещение
"""

