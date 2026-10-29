import time
import matplotlib.pyplot as plt
from main import TodoList
import numpy as np


# рекурентное построение идеально сбалансированного авл дерева из масиива arr длины 2^x - 1
def build_perfect_todo(todo, arr, left, right):
    if left > right:
        return
    mid = (left + right) // 2
    todo.add_task(f"Task {arr[mid]}", arr[mid])
    build_perfect_todo(todo, arr, left, mid - 1)
    build_perfect_todo(todo, arr, mid + 1, right)



def research_find(list_of_n):
    repeats = 20

    time_best = []
    time_avg = []
    time_worst = []

    for n in list_of_n:
        todo = TodoList()
        arr = list(range(1, n + 1))
        build_perfect_todo(todo, arr, 0, n - 1)

        # ЛУЧШИЙ СЛУЧАЙ - поиск корня -> O(1)
        root_priority = todo._avl_tree.root.data[0]

        res_time = 0
        for i in range(repeats):
            start = time.perf_counter()
            todo.find_task(root_priority)
            end = time.perf_counter()
            res_time += (end - start)

        time_best.append(res_time / repeats)

        # СРЕДНИЙ СЛУЧАЙ - элемент на средней глубине -> O(log n)
        mid_priority = arr[len(arr) // 4]

        res_time = 0
        for i in range(repeats):
            start = time.perf_counter()
            todo.find_task(mid_priority)
            end = time.perf_counter()
            res_time += (end - start)

        time_avg.append(res_time / repeats)

        # ХУДШИЙ СЛУЧАЙ - лист -> O(log n)
        leaf_priority = arr[0]

        res_time = 0
        for i in range(repeats):
            start = time.perf_counter()
            todo.find_task(leaf_priority)
            end = time.perf_counter()
            res_time += (end - start)

        time_worst.append(res_time / repeats)

    plt.figure(figsize=(10, 6))
    plt.plot(list_of_n, time_best, 'go-', label="Лучший (корень)", markersize=6)
    plt.plot(list_of_n, time_avg, 'yo-', label="Средний (середина глубины)", markersize=6)
    plt.plot(list_of_n, time_worst, 'ro-', label="Худший (лист)", markersize=6)

    # Линия O(log n)
    x_log = np.array(list_of_n)
    y_log = np.log2(x_log) * (time_worst[-1] / np.log2(list_of_n[-1]))
    plt.plot(list_of_n, y_log, 'k--', alpha=0.5, label='O(log2 n)')

    # Линия O(1)
    avg_best_time = np.mean(time_best)
    plt.axhline(y=float(avg_best_time), color='b', linestyle=':', alpha=0.7,
                label=f'O(1) ≈ {avg_best_time:.2e} с')


    plt.xlabel("Объём данных (n)")
    plt.ylabel("Время выполнения (сек)")
    plt.title("Поиск в AVL дереве (find_task)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()



def research_output(list_of_n): # Theta(n)
    repeats = 10
    times = []

    for n in list_of_n:
        res_time = 0
        for i in range(repeats):
            todo = TodoList()
            arr = list(range(1, n + 1))
            build_perfect_todo(todo, arr, 0, n - 1)

            start = time.perf_counter()
            result = str(todo)
            end = time.perf_counter()
            res_time += (end - start)

        times.append(res_time / repeats)

    plt.figure(figsize=(10, 6))
    plt.plot(list_of_n, times, 'bo-', label="Вывод всех задач", markersize=6)

    # Линия O(n)
    x_linear = np.array(list_of_n)
    y_linear = x_linear * (times[-1] / list_of_n[-1])
    plt.plot(list_of_n, y_linear, 'r--', alpha=0.5, label='O(n)')

    plt.xlabel("Объём данных (n)")
    plt.ylabel("Время выполнения (сек)")
    plt.title("Вывод всех задач (__str__)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()



def research_insert(list_of_n):
    repeats = 20

    time_best = []
    time_avg = []
    time_worst = []

    for n in list_of_n:
        # ЛУЧШИЙ СЛУЧАЙ добавдение листа, удаленного до этого (не требует поворотов)
        res_time = 0
        for i in range(repeats):
            todo = TodoList()
            arr = list(range(1, n + 1))
            build_perfect_todo(todo, arr, 0, n - 1)

            # Удаляем элемент который будем вставлять
            todo.delete_task(n)

            start = time.perf_counter()
            todo.add_task(f"Task {n}", n)  # Вставляем обратно (лист)
            end = time.perf_counter()
            res_time += (end - start)

        time_best.append(res_time / repeats)

        # СРЕДНИЙ СЛУЧАЙ 1 поворот Right
        res_time = 0
        for i in range(repeats):
            todo = TodoList()
            arr = list(range(1, n + 1))
            build_perfect_todo(todo, arr, 0, n - 1)

            # Добавляем элемент чтобы создать ситуацию для одного поворота
            todo.add_task(f"Task {n + 1}", n + 1)

            start = time.perf_counter()
            todo.add_task(f"Task {n + 2}", n + 2)
            end = time.perf_counter()
            res_time += (end - start)

        time_avg.append(res_time / repeats)

        # ХУДШИЙ СЛУЧАЙ 2 поворота Right-Left rotation
        res_time = 0
        for i in range(repeats):
            todo = TodoList()
            arr = list(range(1, n + 1))
            build_perfect_todo(todo, arr, 0, n - 1)

            # Создаем ситуацию для двойного поворота
            todo.add_task(f"Task {n + 2}", n + 2)

            start = time.perf_counter()
            todo.add_task(f"Task {n + 1}", n + 1)
            end = time.perf_counter()
            res_time += (end - start)

        time_worst.append(res_time / repeats)

    plt.figure(figsize=(10, 6))
    plt.plot(list_of_n, time_best, 'go-', label="Лучший (0 поворотов)", markersize=6)
    plt.plot(list_of_n, time_avg, 'yo-', label="Средний (1 поворот)", markersize=6)
    plt.plot(list_of_n, time_worst, 'ro-', label="Худший (2 поворота)", markersize=6)

    # Линия O(log n)
    x_log = np.array(list_of_n)
    y_log = np.log2(x_log) * (time_worst[-1] / np.log2(list_of_n[-1]))
    plt.plot(list_of_n, y_log, 'k--', alpha=0.5, label='O(log2 n)')

    plt.xlabel("Объём данных (n)")
    plt.ylabel("Время выполнения (сек)")
    plt.title("Вставка в AVL дерево (add_task)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()



def research_delete(list_of_n):
    repeats = 10

    time_best = []
    time_avg = []
    time_worst = []

    for n in list_of_n:
        # ЛУЧШИЙ СЛУЧАЙ - удаление листа из идеально сбалансированного дерева
        # (не требует поиска замены и балансировок)
        res_time = 0
        for i in range(repeats):
            todo = TodoList()

            arr = list(range(1, n + 1))
            build_perfect_todo(todo, arr, 0, n - 1)

            start = time.perf_counter()
            todo.delete_task(1)  # Минимальный элемент - лист
            end = time.perf_counter()
            res_time += (end - start)

        time_best.append(res_time / repeats)

        # СРЕДНИЙ СЛУЧАЙ - удаление узла из середины дерева
        # (затраты на поиск замены и проверки на балансировки)
        res_time = 0
        for i in range(repeats):
            todo = TodoList()

            arr = list(range(1, n + 1))
            build_perfect_todo(todo, arr, 0, n - 1)

            # Удаляем элемент на половине глубины
            target = n // 2
            start = time.perf_counter()
            todo.delete_task(target)
            end = time.perf_counter()
            res_time += (end - start)

        time_avg.append(res_time / repeats)

        # ХУДШИЙ СЛУЧАЙ - удаление корня
        # (затраты на поиск замены и проверки на балансировки на всей глубине дерева)
        res_time = 0
        for i in range(repeats):
            todo = TodoList()
            arr = list(range(1, n + 1))
            build_perfect_todo(todo, arr, 0, n - 1)

            root_pr = todo._avl_tree.root.data[0]

            start = time.perf_counter()
            todo.delete_task(root_pr)
            end = time.perf_counter()
            res_time += (end - start)

        time_worst.append(res_time / repeats)

    plt.figure(figsize=(10, 6))
    plt.plot(list_of_n, time_best, 'go-', label="Лучший (удаление листа)", markersize=6)
    plt.plot(list_of_n, time_avg, 'yo-', label="Средний (удаление из середины)", markersize=6)
    plt.plot(list_of_n, time_worst, 'ro-', label="Худший (удаление корня)", markersize=6)

    # Линия O(log n)
    x_log = np.array(list_of_n)
    y_log = np.log2(x_log) * (time_worst[-1] / np.log2(list_of_n[-1]))
    plt.plot(list_of_n, y_log, 'k--', alpha=0.5, label='O(log2 n)')

    plt.xlabel("Объём данных (n)")
    plt.ylabel("Время выполнения (сек)")
    plt.title("Удаление из AVL дерева (delete_task)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()



if __name__ == "__main__":
    list_of_n = [127, 511, 1023, 4095, 8191, 16383, 32767, 65535]

    research_insert(list_of_n)
    research_delete(list_of_n)
    research_find(list_of_n)
    research_output(list_of_n)