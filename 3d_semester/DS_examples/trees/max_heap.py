def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return (i - 1) // 2

# it is used for heap_sort (ascending) and priority queues (where max elements are deleted at first)
def max_heapify(arr, heap_size, i):    # O(log n)
    l = left(i)
    r = right(i)

    largest = i 

    if l < heap_size and arr[l] > arr[i]:
        largest = l
    
    if r < heap_size and arr[r] > arr[largest]:
        largest = r 
    
    if largest != i:
        # swap elements
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, heap_size, largest)


def build_max_heap(arr):    #O(n)
    heap_size = len(arr)

    for i in range(heap_size//2 - 1, -1, -1):
        max_heapify(arr, heap_size, i)


def run_example():
    arr = [0, 5, 20, 6, 12, 65, 1, 4, 9, 3, 89, 22, 25, 28, 10]
    build_max_heap(arr)

    print(f'Heap: {arr}')

run_example()


