"""
ТЕОРИЯ

Преимущества бинарной кучи:

1) Проще реализация - один массив

2) Лучшая константа - меньше накладных расходов

3) Кэш-дружественность - данные в массиве последовательно

4) Встроенная в Python - модуль heapq

Когда биномиальная куча может быть лучше:

1) Частые слияния куч - O(log n) vs O(n)

2) Уменьшение ключа - O(log n) vs O(n) в бинарной

3) Амортизированные O(1) для вставки; В презентации O(log n)
"""


def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return (i - 1) // 2

def first_non_leaf_elem_index(n):
    return n // 2 - 1


def min_heapify(arr, heap_size, index):
    # indexes
    left_kid = left(index)
    right_kid = right(index)
    minimal = index

    if left_kid < heap_size and arr[left_kid] < arr[minimal]:
        minimal = left_kid

    if right_kid < heap_size and arr[right_kid] < arr[minimal]:
        minimal = right_kid

    if minimal != index:
        arr[index], arr[minimal] = arr[minimal], arr[index]
        min_heapify(arr, heap_size, minimal)


def build_min_heap(arr):
    heap_size = len(arr)
    first = first_non_leaf_elem_index(heap_size)
    for i in range(first, -1, -1):
        min_heapify(arr, heap_size, i)


# result is a descending sequent
def min_heap_sort(arr):

    build_min_heap(arr)
    n = len(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        min_heapify(arr, i, 0)


# dijkstra algorithm for ways matrix (not for a graph) + another distance condition
def not_optimal_dijkstra(heaights):    #O(n^2)
    rows_num = len(heaights)
    cols_num = len(heaights[0])

    priority_q = [[0, (0, 0)]]
    distances = [[float("inf")] * cols_num for _ in range(rows_num)]
    distances[0][0] = 0

    while priority_q: #O(n)

        build_min_heap(priority_q)      #TODO O(n) not optimal, we need O(log n) because it is heap => redo    ===DONE===
        current_dist, current_dot = priority_q.pop(0)

        if current_dist > distances[current_dot[0]][current_dot[1]]:
            continue

        # neighbours check
        for i in -1, 1:    # up, down
            if (0 <= current_dot[0] + i < rows_num) and (0 <= current_dot[1] < cols_num):    # borders condition
                dist = max(current_dist, abs(heaights[current_dot[0]][current_dot[1]] - heaights[current_dot[0] + i][current_dot[1]]))   # we need to find max delta = effort

                if dist < distances[current_dot[0] + i][current_dot[1]]:     # if we can minimize it, we do it
                    distances[current_dot[0] + i][current_dot[1]] = dist
                    priority_q.append([dist, (current_dot[0] + i, current_dot[1])])

        for j in -1, 1: # left, right
            if (0 <= current_dot[0] < rows_num) and (0 <= current_dot[1] + j < cols_num):
                dist = max(current_dist, abs(heaights[current_dot[0]][current_dot[1]] - heaights[current_dot[0]][current_dot[1] + j]))

                if dist < distances[current_dot[0]][current_dot[1] + j]:
                    distances[current_dot[0]][current_dot[1] + j] = dist
                    priority_q.append([dist, (current_dot[0], current_dot[1] + j)])

    print(distances[rows_num - 1][cols_num - 1])    #ans
    return distances


class MinHeap:     # for priority queue
    def __init__(self):
        self.heap = []

    def push(self, elem):
        self.heap.append(elem)
        self._shift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()

        min_elem = self.heap[0]
        self.heap[0] = self.heap.pop()     # first elem = last elem (that is deleted by pop)
        self._shift_down(0)               # shift it down to correct place according to min heap condition
        return min_elem

    def _shift_up(self, index):
        while index > 0:
            parent_index = parent(index)
            if self.heap[index][0] >= self.heap[parent_index][0]:
                break
            self.heap[index], self.heap[parent_index] = self.heap[parent_index],  self.heap[index]
            index = parent_index

    def _shift_down(self, index):
        heap_size = len(self.heap)
        while 1:
            left_kid = left(index)
            right_kid = right(index)
            minimal = index

            if left_kid < heap_size and self.heap[left_kid][0] < self.heap[minimal][0]:
                minimal = left_kid

            if right_kid < heap_size and self.heap[right_kid][0] < self.heap[minimal][0]:
                minimal = right_kid

            if minimal == index:
                break

            self.heap[index], self.heap[minimal] = self.heap[minimal], self.heap[index]
            index = minimal



class MinHeapUPD:  # for priority queue
    def __init__(self):
        self.heap = []  # пары (priority, value)
        self.value_to_index = {}  # значение -> индекс в куче

    def push(self, elem):
        """Добавляет элемент (priority, value)."""
        priority, value = elem
        if value in self.value_to_index:
            self.change_priority(value, priority)
            return

        self.heap.append(elem)
        index = len(self.heap) - 1
        self.value_to_index[value] = index
        self._shift_up(index)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            elem = self.heap.pop()
            del self.value_to_index[elem[1]]
            return elem

        min_elem = self.heap[0]
        del self.value_to_index[min_elem[1]]

        # Перемещаем последний в корень
        self.heap[0] = self.heap.pop()
        self.value_to_index[self.heap[0][1]] = 0

        self._shift_down(0)
        return min_elem

    def change_priority(self, value, new_priority):
        """Изменяет приоритет существующего элемента."""
        if value not in self.value_to_index:
            raise ValueError(f"Value {value} not found")

        index = self.value_to_index[value]
        old_priority = self.heap[index][0]
        self.heap[index] = (new_priority, value)

        if new_priority < old_priority:  # приоритет уменьшился (для min-heap)
            self._shift_up(index)
        elif new_priority > old_priority:  # приоритет увеличился
            self._shift_down(index)

    def _shift_up(self, index):
        while index > 0:
            parent_index = parent(index)
            if self.heap[index][0] >= self.heap[parent_index][0]:
                break
            # Меняем местами
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index], self.heap[index]
            )
            # Обновляем индексы в словаре
            self.value_to_index[self.heap[index][1]] = index
            self.value_to_index[self.heap[parent_index][1]] = parent_index
            index = parent_index

    def _shift_down(self, index):
        heap_size = len(self.heap)
        while True:
            left_kid = left(index)
            right_kid = right(index)
            minimal = index

            if left_kid < heap_size and self.heap[left_kid][0] < self.heap[minimal][0]:
                minimal = left_kid
            if right_kid < heap_size and self.heap[right_kid][0] < self.heap[minimal][0]:
                minimal = right_kid

            if minimal == index:
                break

            # Меняем местами
            self.heap[index], self.heap[minimal] = (
                self.heap[minimal], self.heap[index]
            )
            # Обновляем индексы
            self.value_to_index[self.heap[index][1]] = index
            self.value_to_index[self.heap[minimal][1]] = minimal

            index = minimal

    def __contains__(self, value):
        return value in self.value_to_index

    def get_priority(self, value):
        """Возвращает текущий приоритет значения."""
        if value not in self.value_to_index:
            return None
        return self.heap[self.value_to_index[value]][0]


# dijkstra algorithm for ways matrix (not for a graph) + another distance condition
def dijkstra(heaights):    #O(n log n)
    rows_num = len(heaights)
    cols_num = len(heaights[0])
    priority_q = MinHeap()
    priority_q.push([0, (0, 0)])

    distances = [[float("inf")] * cols_num for _ in range(rows_num)]
    distances[0][0] = 0

    while priority_q.heap: # O(n)    + condition of minimal distance at first thanks to MinHeap

        current_dist, current_dot = priority_q.pop()    # O(log n)

        if current_dist > distances[current_dot[0]][current_dot[1]]:
            continue

        # neighbours check
        for i in -1, 1:    # up, down
            if (0 <= current_dot[0] + i < rows_num) and (0 <= current_dot[1] < cols_num):    # borders condition
                dist = max(current_dist, abs(heaights[current_dot[0]][current_dot[1]] - heaights[current_dot[0] + i][current_dot[1]]))   # we need to find max delta = effort

                if dist < distances[current_dot[0] + i][current_dot[1]]:     # if we can minimize it, we do it
                    distances[current_dot[0] + i][current_dot[1]] = dist
                    priority_q.push([dist, (current_dot[0] + i, current_dot[1])])

        for j in -1, 1: # left, right
            if (0 <= current_dot[0] < rows_num) and (0 <= current_dot[1] + j < cols_num):
                dist = max(current_dist, abs(heaights[current_dot[0]][current_dot[1]] - heaights[current_dot[0]][current_dot[1] + j]))

                if dist < distances[current_dot[0]][current_dot[1] + j]:
                    distances[current_dot[0]][current_dot[1] + j] = dist
                    priority_q.push([dist, (current_dot[0], current_dot[1] + j)])

    print(distances[rows_num - 1][cols_num - 1])    #ans
    return distances


