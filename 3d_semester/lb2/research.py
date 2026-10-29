from array import array
from main import timsort
from random import randint, sample
import time
import matplotlib.pyplot as plt


def generate_data_for_best_case(n: int) -> array:
    """Лучший случай - уже отсортированные данные -> O(n)"""
    arr = array('i', [randint(-10_000, 10_000) for i in range(n)])
    timsort(arr, 64, 7)
    return arr


def generate_data_for_average_case(n: int) -> array:
    """Средний случай - случайные, но частично упорядоченные данные -> O(nlogn)"""
    arr = sorted([randint(-10_000, 10_000) for i in range(n)], key=abs, reverse=True)
    disorder_level = 0.1

    for k in range(int(n * disorder_level)):
        i, j = sample(range(n), 2)
        arr[i], arr[j] = arr[j], arr[i]

    return array('i', arr)


def generate_data_for_worst_case(n: int) -> array:
    """Худший случай - полностью случайные данные -> O(nlogn)"""
    return array('i', [randint(-10_000, 10_000) for i in range(n)])


def get_mean_time(arr: array) -> float:
    sm = 0
    for i in range(3):
        test_arr = array('i', arr)
        st = time.perf_counter()
        timsort(test_arr, 64, 7)
        end = time.perf_counter()
        sm += end - st
    return sm / 3


def get_all_times(list_of_n: list) -> tuple:
    times_best = []
    times_average = []
    times_worst = []

    for i, n in enumerate(list_of_n):
        data_best = generate_data_for_best_case(n)
        data_average = generate_data_for_average_case(n)
        data_worst = generate_data_for_worst_case(n)

        time_best = get_mean_time(data_best)
        time_avg = get_mean_time(data_average)
        time_worst = get_mean_time(data_worst)

        times_best.append(time_best)
        times_average.append(time_avg)
        times_worst.append(time_worst)

    return times_best, times_average, times_worst


def research_dependence_on_min_run():
    min_runs = list(range(1, 100 + 1))
    times = [[0] * len(min_runs) for _ in range(3)]
    sizes = [100, 1_000, 5_000]

    for index, n in enumerate(sizes):
        arr = generate_data_for_worst_case(n)
        for k, min_run_value in enumerate(min_runs):
            sm = 0
            for i in range(10):
                test_arr = array('i', arr)
                st = time.perf_counter()
                timsort(test_arr, choose_min_run=min_run_value)
                end = time.perf_counter()
                sm += end - st
            times[index][k] = sm / 10

    for j in range(3):
        draw_plot(min_runs, times[j], f"ЗАВИСИМОСТЬ ОТ MIN_RUN\nдля массива размера {sizes[j]}")


def draw_plot(list_of_n, time_results, title, flag_for_min_run=False):
    plt.figure(figsize=(10, 6))
    plt.plot(list_of_n, time_results, 'bo-', linewidth=1.5, markersize=4)
    plt.xlabel("Размер массива (n)") if not flag_for_min_run else plt.xlabel("Размер min_run")
    plt.ylabel("Время (секунды)")
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.show()


def draw_comparison_plot(list_of_n: list, times_best: list, times_avg: list, times_worst: list):
    plt.figure(figsize=(10, 6))

    plt.plot(list_of_n, times_best, 'go-', label='Лучший случай', linewidth=2, markersize=5)
    plt.plot(list_of_n, times_avg, 'bo-', label='Средний случай', linewidth=2, markersize=5)
    plt.plot(list_of_n, times_worst, 'ro-', label='Худший случай', linewidth=2, markersize=5)

    plt.xlabel('Размер массива (n)')
    plt.ylabel('Время (секунды)')
    plt.title('СРАВНЕНИЕ ВРЕМЕНИ ВЫПОЛНЕНИЯ TIMSORT')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    list_of_n = [10, 50, 100, 500, 1_000, 5_000, 10_000, 50_000, 100_000]

    times_best, times_avg, times_worst = get_all_times(list_of_n)

    draw_plot(list_of_n, times_best, "ЛУЧШИЙ СЛУЧАЙ\nO(n)")
    draw_plot(list_of_n, times_avg, "СРЕДНИЙ СЛУЧАЙ\nO(n log n)")
    draw_plot(list_of_n, times_worst, "ХУДШИЙ СЛУЧАЙ\nO(n log n)")

    draw_comparison_plot(list_of_n, times_best, times_avg, times_worst)
    research_dependence_on_min_run()