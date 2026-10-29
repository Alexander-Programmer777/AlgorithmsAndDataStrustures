from random import randint

# O(N ^ 2)
def bubble_sort(arr : list[int]) -> list[int]:
    N = len(arr)
    k = 0

    for i in range(N):
        for j in range(N - 1):

            if j == N - k - 1:  # tiny optimization
                break

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        k += 1

    return arr


N = 15
a = []
for i in range(15):
    a.append(randint(-100, 100))

print(a)

a = bubble_sort(a)
print(a)
print(a == sorted(a))