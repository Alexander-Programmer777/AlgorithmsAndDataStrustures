#  O(nlogn) in general,
#  O(n ^ 2) the worst
# unsustainable


# not optimal memory usage
def quicksort(arr : list[int]) -> list[int]:
    if len(arr) == 0:
        return arr

    pivot = arr.pop()

    l_a = []
    r_a = []
    for elem in arr:  # O(N)
        if elem <= pivot:
            l_a.append(elem)
        else:
            r_a.append(elem)

    return quicksort(l_a) + [pivot] + quicksort(r_a)  # O(log(n))


# res = []
def quicksort_middle_pivot(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid_index = len(arr) // 2
    pivot = arr[mid_index]
    #res.append(pivot)

    left = []
    right = []
    middle = []

    for elem in arr:
        if elem < pivot:
            left.append(elem)
        elif elem == pivot:
            middle.append(elem)
        else:
            right.append(elem)

    return quicksort(left) + middle + quicksort(right)

import random
def qsort_random_pivot(arr: list[int]):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = []
    mid = []
    right = []

    for elem in arr:
        if elem < pivot:
            left += [elem]
        elif elem == pivot:
            mid += [elem]
        else:
            right += [elem]

    return qsort_random_pivot(left) + mid + qsort_random_pivot(right)

arr = list(range(100))
random.shuffle(arr)
arr += arr
print(arr)

res = qsort_random_pivot(arr)
print(res)
assert res == sorted(arr)



def quicksort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # pi - индекс опорного элемента после разбиения
        pi = partition(arr, low, high)

        # Рекурсивно сортируем элементы до и после опорного
        quicksort_inplace(arr, low, pi - 1)
        quicksort_inplace(arr, pi + 1, high)


def partition(arr, low, high):
    # Опорный элемент (можно выбирать по-разному, здесь - последний)
    pivot = arr[high]

    # Индекс меньшего элемента
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Помещаем опорный элемент на правильное место
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

print(arr.sort())

# Пример использования
arr = [10, 7, 8, 9, 1, 5]
quicksort_inplace(arr)
print(arr)  # [1, 5, 7, 8, 9, 10]
