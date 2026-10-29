import time, matplotlib.pyplot as plt
import numpy as np
from aisd.lb1.alg_lb1 import CircularDeque

list_of_n = [100, 500, 1_000, 5_000, 10_000, 50_000, 100_000, 500_000, 1_000_000]


def draw_plot(numbers, time_results, title, label, mean_time=None, is_O_of_n=False):
    plt.figure(figsize=(10, 6))
    plt.plot(numbers, time_results, 'bo-', linewidth=1.5, markersize=4, label=label)
    if mean_time is not None:
        plt.axhline(y=mean_time, color='r', linestyle='--', label='O(1)')
    if is_O_of_n:
        coefficients = np.polyfit(numbers, time_results, 1)       #linear regression
        linear_fit = np.poly1d(coefficients)
        plt.plot(numbers, linear_fit(numbers), 'r--', label='O(n)')
    plt.xlabel("Размер массива (n)")
    plt.ylabel("Время выполнения (микросекунды)")
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

def fill_deque(dq: CircularDeque) -> CircularDeque:
    for i in range(dq.cap):
        dq.push_back(i)
    return dq

def research_of_init(numbers: list):
    time_results = []
    for n in numbers:
        sm = 0
        for i in range(1_000):
            st = time.perf_counter()
            dq = CircularDeque(n, True)
            end = time.perf_counter()
            sm += end - st
        time_results += [sm / 1_000]
    time_results = [t * 1_000_000 for t in time_results]
    draw_plot(numbers, time_results, "Исследование __init__", "init", is_O_of_n=True)
    return time_results


def research_of_push_front(numbers: list):
    time_results = []
    for n in numbers:
        sm = 0
        dq = CircularDeque(n, True)
        for i in range(10_000):
            st = time.perf_counter()
            dq.push_front(i)
            end = time.perf_counter()
            sm += end - st
        time_results += [sm / 10_000]
    time_results = [t * 1_000_000 for t in time_results]
    mean_time = sum(time_results) / len(time_results)

    draw_plot(numbers, time_results, "Исследование push_front", "push_front", mean_time)
    return time_results


def research_of_push_back(numbers: list):
    time_results = []
    for n in numbers:
        sm = 0
        dq = CircularDeque(n, True)
        for i in range(10_000):
            st = time.perf_counter()
            dq.push_back(i)
            end = time.perf_counter()
            sm += end - st
        time_results += [sm / 10_000]
    time_results = [t * 1_000_000 for t in time_results]
    mean_time = sum(time_results) / len(time_results)
    draw_plot(numbers, time_results, "Исследование push_back", "push_back", mean_time)
    return time_results


def research_of_pop_back(numbers: list):
    time_results = []
    for n in numbers:
        dq = CircularDeque(n, True)
        dq = fill_deque(dq)
        sm = 0
        for i in range(10_000):
            if dq.empty():
                dq = fill_deque(dq)
            st = time.perf_counter()
            dq.pop_back()
            end = time.perf_counter()
            sm += end - st
        time_results += [sm / 10_000]
    time_results = [t * 1_000_000 for t in time_results]
    mean_time = sum(time_results) / len(time_results)
    draw_plot(numbers, time_results, "Исследование pop_back", "pop_back", mean_time)
    return time_results


def research_of_pop_front(numbers: list):
    time_results = []
    for n in numbers:
        dq = CircularDeque(n, True)
        dq = fill_deque(dq)
        sm = 0
        for i in range(10_000):
            if dq.empty():
                dq = fill_deque(dq)
            st = time.perf_counter()
            dq.pop_front()
            end = time.perf_counter()
            sm += end - st
        time_results += [sm / 10_000]
    time_results = [t * 1_000_000 for t in time_results]
    mean_time = sum(time_results) / len(time_results)
    draw_plot(numbers, time_results, "Исследование pop_front", "pop_front", mean_time)
    return time_results


def research_of_front(numbers: list):
    time_results = []
    for n in numbers:
        dq = CircularDeque(n, True)
        dq = fill_deque(dq)
        sm = 0
        for i in range(10_000):
            if dq.empty():
                dq = fill_deque(dq)
            st = time.perf_counter()
            dq.front()
            end = time.perf_counter()
            sm += end - st
        time_results += [sm / 10_000]
    time_results = [t * 1_000_000 for t in time_results]
    mean_time = sum(time_results) / len(time_results)
    draw_plot(numbers, time_results, "Исследование front", "front", mean_time)
    return time_results


def research_of_back(numbers: list):
    time_results = []
    for n in numbers:
        dq = CircularDeque(n, True)
        dq = fill_deque(dq)
        sm = 0
        for i in range(10_000):
            if dq.empty():
                dq = fill_deque(dq)
            st = time.perf_counter()
            dq.back()
            end = time.perf_counter()
            sm += end - st
        time_results += [sm / 10_000]
    time_results = [t * 1_000_000 for t in time_results]
    mean_time = sum(time_results) / len(time_results)
    draw_plot(numbers, time_results, "Исследование back", "back", mean_time)
    return time_results


def research_of_resize(numbers: list):
    time_results_up = []
    for n in numbers:
        sm = 0
        for i in range(100):
            dq = CircularDeque(n, True)
            st = time.perf_counter()
            dq.resize(n * 2)
            end = time.perf_counter()
            sm += end - st

        time_results_up += [sm / 100]

    time_results_down = []
    for n in numbers:
        sm = 0
        for i in range(100):
            dq = CircularDeque(n, True)
            st = time.perf_counter()
            dq.resize(n // 2)
            end = time.perf_counter()
            sm += end - st
        time_results_down += [sm / 100]

    time_results_up = [t * 1_000_000 for t in time_results_up]
    time_results_down = [t * 1_000_000 for t in time_results_down]

    plt.figure(figsize=(10, 6))
    plt.plot(numbers, time_results_up, 'o-', linewidth=2, markersize=6, label='Увеличение (n * 2)')
    plt.plot(numbers, time_results_down, 's-', linewidth=2, markersize=6, label='Уменьшение (n // 2)')

    coefficients_up = np.polyfit(numbers, time_results_up, 1)
    linear_fit_up = np.poly1d(coefficients_up)
    plt.plot(numbers, linear_fit_up(numbers), 'r--', label='O(n) для увеличения')

    coefficients_dn = np.polyfit(numbers, time_results_down, 1)
    linear_fit_dn = np.poly1d(coefficients_dn)
    plt.plot(numbers, linear_fit_dn(numbers), 'g--', label='O(n) для уменьшения')

    plt.xlabel("Размер массива (n)")
    plt.ylabel("Время выполнения (микросекунды)")
    plt.title("Исследование resize: увеличение или уменьшение размера массива")
    plt.grid(True, alpha=0.3)

    plt.legend()
    plt.show()
    return time_results_up, time_results_down


def total_plot(list_of_t, numbers, labels):
    colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive']
    markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*']
    plt.figure(figsize=(12, 8))

    for i, (t_data, label) in enumerate(zip(list_of_t, labels)):
        plt.plot(numbers, t_data,
                 marker=markers[i % len(markers)],
                 color=colors[i % len(colors)],
                 linewidth=1.5,
                 markersize=4,
                 label=label)

    plt.xlabel("Размер массива (n)")
    plt.ylabel("Время выполнения (микросекунды)")
    plt.title("Сравнение времени выполнения различных операций")
    plt.grid(True, alpha=0.3)

    plt.legend()
    plt.show()


t_resize_up, t_resize_down = research_of_resize(list_of_n)

t_init = research_of_init(list_of_n)

t_pop_front = research_of_pop_front(list_of_n)
t_pop_back = research_of_pop_back(list_of_n)

t_push_front = research_of_push_front(list_of_n)
t_push_back = research_of_push_back(list_of_n)

t_front = research_of_front(list_of_n)
t_back = research_of_back(list_of_n)

labels = ["Увеличение resize", "Уменьшение resize", "Инициализация",
          "Pop_front", "Pop_back", "Push_front", "Push_back",
          "Front", "Back"]
total_plot([t_resize_up, t_resize_down, t_init, t_pop_front, t_pop_back,
            t_push_front, t_push_back, t_front, t_back], list_of_n, labels)