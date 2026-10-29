from main import SegmentTree
import time
import matplotlib.pyplot as plt
from random import randint


# 1 case only
def research_of_init(list_of_n):
    time_results = []
    for n in list_of_n:
        time_total = 0
        for i in range(1_000):
            start = time.perf_counter()
            seg_tree = SegmentTree(n)
            end = time.perf_counter()
            time_total += end - start
        time_results += [time_total / 1_000]


    plt.figure(figsize=(10, 6))
    plt.plot(list_of_n, time_results, 'bo-', linewidth=1.5, markersize=4)
    plt.xlabel("Размер массива (n)")
    plt.ylabel("Время (секунды)")
    plt.title("ИССЛЕДОВАНИЕ __init__")
    plt.grid(True, alpha=0.3)
    plt.show()


def research_of_add_value(list_of_n):
    worst_time_results = []
    best_time_results = []
    avg_time_results = []

    for n in list_of_n:
        time_total_best = 0
        time_total_worst = 0
        time_total_avg = 0

        # ЛУЧШИЙ случай - один элемент
        seg_tree = SegmentTree(n)
        for i in range(1_000):
            start_best = time.perf_counter()
            seg_tree.add_value(0, 1, 10)
            end_best = time.perf_counter()

            time_total_best += end_best - start_best

        # СРЕДНИЙ случай - случайный небольшой отрезок
        seg_tree = SegmentTree(n)
        for i in range(1_000):
            avg_l = randint(0, n - 50)
            avg_r = avg_l + randint(1, 50)

            start_avg = time.perf_counter()
            seg_tree.add_value(avg_l, avg_r, 10)
            end_avg = time.perf_counter()

            time_total_avg += end_avg - start_avg

        # ХУДШИЙ случай - весь массив
        seg_tree = SegmentTree(n)
        for i in range(1_000):
            start_worst = time.perf_counter()
            seg_tree.add_value(0, n, 10)
            end_worst = time.perf_counter()

            time_total_worst += end_worst - start_worst


        worst_time_results += [time_total_worst / 1_000 * 10**6]
        best_time_results += [time_total_best / 1_000 * 10**6]
        avg_time_results += [time_total_avg / 1_000 * 10**6]


    plt.figure(figsize=(10, 6))
    plt.plot(list_of_n, worst_time_results, 'ro-', linewidth=1.5, markersize=4, label="worst case")
    plt.plot(list_of_n, avg_time_results, 'yo-', linewidth=1.5, markersize=4, label="average case")
    plt.plot(list_of_n, best_time_results, 'go-', linewidth=1.5, markersize=4, label="best case")

    plt.xlabel("Размер массива (n)")
    plt.ylabel("Время (микросекунды)")
    plt.title("ИССЛЕДОВАНИЕ add_value")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


# 1 case only
def research_of_get_value(list_of_n):
    time_results = []
    for n in list_of_n:
        time_total = 0
        seg_tree = SegmentTree(n)
        for i in range(1_000):
            random_index = randint(0, n - 1)

            start = time.perf_counter()
            seg_tree.get_value(random_index)
            end = time.perf_counter()

            time_total += end - start
        time_results += [time_total / 1_000 * 10**6]  # в микросекундах

    plt.figure(figsize=(10, 6))
    plt.plot(list_of_n, time_results, 'bo-', linewidth=1.5, markersize=4)
    plt.xlabel("Размер массива (n)")
    plt.ylabel("Время (микросекунды)")
    plt.title("ИССЛЕДОВАНИЕ get_value")
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    list_of_n = [100, 500, 1_000, 5_000, 10_000, 50_000, 100_000, 250_000, 500_000, 1_000_000, 2_000_000]

    research_of_init(list_of_n)

    research_of_add_value(list_of_n)

    research_of_get_value(list_of_n)