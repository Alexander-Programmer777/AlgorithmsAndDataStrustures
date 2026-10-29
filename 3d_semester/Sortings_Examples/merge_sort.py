

# O(nlogn) log2(n) from recurrent function with division by 2
# n from full loop
# sustainable

def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:   # lowest recursion case
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left : list[int], right : list[int]) -> list[int]:
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):   #O(N)
        if left[i] <= right[j]:
            merged.append(left[i])   # O(1) without .pop(0) <-> O(N)
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


import random
N = 100
a = []
for i in range(N):
    a.append(random.randint(-100, 100))
print(a)
a = merge_sort(a)
print(a)

print(a == sorted(a))



