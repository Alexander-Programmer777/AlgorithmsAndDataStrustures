import time
import matplotlib.pyplot as plt

from main import Rope


class RopeBenchmark:
    def __init__(self):
        self.results = {}

    def generate_data(self, n: int, case_type: str):

        if case_type == "best":
            # Лучший случай - сбалансированные операции
            base_string = 'a' * n
            concat_string = 'b' * n
            search_index = 0
            insert_string = 'b' * (n // 100)
            split_index = n // 2
            insert_index = n
            delete_index = n // 2
            delete_length = n - (n // 2)

        elif case_type == "worst":
            # Худший случай - несбалансированные операции
            base_string = 'a' * n
            concat_string = 'b' * (n // 10)
            search_index = n - 1
            insert_string = 'b' * (n // 30)
            split_index = 0
            insert_index = n // 2
            delete_index = n // 2
            delete_length = 1

        else:
            # Средний случай - средне сбалансированные операции
            base_string = 'a' * n
            concat_string = 'b' * (n // 2)
            search_index = n // 2
            insert_string = 'b' * (n // 100)
            split_index = n // 2
            insert_index = n // 2
            delete_index = n // 2
            delete_length = n // 50

        return base_string, concat_string, search_index, insert_string, split_index, insert_index, delete_index, delete_length

    def benchmark_method(self, method_name: str, max_leaf_sizes: list[int], data_sizes: list[int], case_type: str,
                         num_runs: int = 5):

        results = {size: [] for size in max_leaf_sizes}

        for n in data_sizes:

            for max_leaf in max_leaf_sizes:
                times = []

                for i in range(num_runs):

                    base_str, concat_string, search_index, insert_str, split_index, insert_index, delete_index, delete_len = self.generate_data(
                        n, case_type)

                    rope1 = Rope(MAX_LEAF=max_leaf, string=base_str)
                    rope_concat = Rope(MAX_LEAF=max_leaf, string=concat_string)

                    if method_name == "concat":
                        start_time = time.perf_counter()
                        rope1.concat(rope_concat)
                        end_time = time.perf_counter()
                        times.append(end_time - start_time)

                    elif method_name == "split":
                        start_time = time.perf_counter()
                        rope1.split(rope1.root, split_index)
                        end_time = time.perf_counter()
                        times.append(end_time - start_time)

                    elif method_name == "index":
                        start_time = time.perf_counter()
                        rope1.index(search_index)
                        end_time = time.perf_counter()
                        times.append(end_time - start_time)

                    elif method_name == "insert":
                        start_time = time.perf_counter()
                        rope1.insert(rope1.root, insert_str, insert_index)
                        end_time = time.perf_counter()
                        times.append(end_time - start_time)

                    elif method_name == "delete":
                        start_time = time.perf_counter()
                        rope1.delete(rope1.root, delete_index, delete_len)
                        end_time = time.perf_counter()
                        times.append(end_time - start_time)

                results[max_leaf].append(sum(times) / len(times))  # avg time

        return results

    def run_complete_benchmark(self, data_sizes: list[int], num_runs: int = 5):

        max_leaf_sizes = [128, 256, 512, 1024]
        case_types = ["best", "average", "worst"]
        methods = ["concat", "split", "index", "insert", "delete"]

        for method in methods:
            self.results[method] = {}
            for case_type in case_types:
                self.results[method][case_type] = self.benchmark_method(method, max_leaf_sizes, data_sizes, case_type,
                                                                        num_runs)

    def draw_comparison_plot(self, data_sizes: list[int]):

        max_leaf_sizes = [128, 256, 512, 1024]

        case_types = ["best", "average", "worst"]
        colors = ['blue', 'green', 'red', 'orange']
        line_styles = {'best': '-', 'average': '--', 'worst': ':'}

        fig, axes = plt.subplots(2, 3, figsize=(12, 8))
        axes = axes.flatten()

        methods = ["concat", "split", "index", "insert", "delete"]

        for i, method in enumerate(methods):
            if i >= len(axes):
                break

            ax = axes[i]
            for j, max_leaf in enumerate(max_leaf_sizes):
                for case_type in case_types:
                    if method in self.results and case_type in self.results[method]:
                        times = self.results[method][case_type][max_leaf]
                        ax.plot(data_sizes[:len(times)], times,
                                color=colors[j],
                                linestyle=line_styles[case_type],
                                label=f'MAX_LEAF={max_leaf} ({case_type})',
                                alpha=0.7)

            ax.set_xlabel('Размер входных данных (n)')
            ax.set_ylabel('Время (секунды)')
            ax.set_title(f'Исследование {method.upper()}')
            ax.grid(True, alpha=0.3)
            ax.legend(fontsize=8)

        for j in range(len(methods), len(axes)):
            axes[j].set_visible(False)

        plt.tight_layout()
        plt.show()

    def draw_case_plots(self, data_sizes: list[int]):
        max_leaf_sizes = [128, 256, 512, 1024]
        case_types = ["best", "average", "worst"]
        colors = ['blue', 'green', 'red', 'orange']

        methods = ["concat", "split", "index", "insert", "delete"]

        for method in methods:
            fig, axes = plt.subplots(2, 2, figsize=(12, 8))
            axes = axes.flatten()

            for i, max_leaf in enumerate(max_leaf_sizes):
                if i >= len(axes):
                    break

                ax = axes[i]
                for case_type in case_types:
                    if method in self.results and case_type in self.results[method]:
                        times = self.results[method][case_type][max_leaf]
                        ax.plot(data_sizes[:len(times)], times,
                                marker='o',
                                label=f'{case_type} case',
                                alpha=0.8)

                ax.set_xlabel('Размер входных данных (n)')
                ax.set_ylabel('Время (секунды)')
                ax.set_title(f'{method.upper()} - MAX_LEAF={max_leaf}')
                ax.grid(True, alpha=0.3)
                ax.legend()

            plt.tight_layout()
            plt.show()


if __name__ == "__main__":
    data_sizes = [100, 1_000, 5_000, 10_000, 30_000, 50_000, 80_000, 100_000]

    benchmark = RopeBenchmark()

    benchmark.run_complete_benchmark(data_sizes, num_runs=5)

    benchmark.draw_case_plots(data_sizes)

    benchmark.draw_comparison_plot(data_sizes)
