
def selection_sort(arr : list[int]) -> list[int]:
    N = len(arr)
    for i in range(0, N - 1):
        ind_mn = i
        for j in range(i + 1, N):
            ind_mn = ind_mn if arr[ind_mn] < arr[j] else arr[j]
        if i != ind_mn:
            arr[i], arr[ind_mn] = arr[ind_mn], arr[i]
    return arr

