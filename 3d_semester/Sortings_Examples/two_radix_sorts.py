# LSD - least significant digit - sustainable
# MSD - most significant digit - unsustainable

import random

# Сортировка подсчетом для LSD (устойчивая!)
def counting_sort_by_digit(arr, digit_pos):
    count = [0] * 10  # для цифр 0-9 массив частот
    output = [0] * len(arr)


    # Подсчет частот
    for num in arr:
        digit = (num // (10 ** digit_pos)) % 10
        count[digit] += 1

    # Накопительные суммы (обеспечивает устойчивость!)
    for i in range(1, 10):
        count[i] += count[i - 1] # прибавляем

    # Распределение элементов (в обратном порядке для устойчивости)
    for i in range(len(arr) - 1, -1, -1):
        digit = (arr[i] // (10 ** digit_pos)) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1


    return output

#
# N = int(input("len of digits? = "))
# a = []
# for i in range(15):
#     a.append(random.randint(10 ** (N - 1), 10 ** N))
#
# print(a)
# for i in range(N):
#     a = counting_sort_by_digit(a, i)
#     print(a)
#
# print(a == sorted(a))


