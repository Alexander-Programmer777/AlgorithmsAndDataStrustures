
# Complexity depends on chosen sequence:
# n ^ 2 for d //= 2 (Shell)
# n ^ (3/2) for d : 2 ^ i - 1 <= N where i = from 0 to maximum possible (Khibard)
# n (logn)^2 for d : 2 ^ i * 3 ^ j <= N/2 (Pratt)

# unsustainable

from random import randint

N = 100
a = []
for i in range(N):
    a.append(randint(-100, 100))
print(a)
d = N//2
while d != 0: # O(log N)

    #insertion sort algorythm for parts of main array "a"
    for i in range(d, N): # O(N - d) ~ O(n)
        j = i
        prev = j - d
        while prev >= 0 and a[j] < a[prev]: # best case - sorted array: O(1)
            a[j], a[prev] = a[prev], a[j]   # worst case i / d ~ O(n/d)
            j -= d
            prev -= d

    d //= 2




print(a)
print(a == sorted(a))

