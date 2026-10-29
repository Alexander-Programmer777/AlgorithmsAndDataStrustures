from array import array


# DONE \/
def get_min_run(n: int, parameter: int) -> int:
    flag = 0
    while n >= parameter:
        flag |= n & 1
        n >>= 1
    return n + flag


def cmp(a: int, b: int) -> bool:
    return abs(a) >= abs(b)


def find_natural_run(arr: "array", st: int) -> int:
    n = len(arr)
    if st == n - 1:
        return 1

    i = st + 1
    decrease = cmp(arr[st], arr[i]) if i < n else True

    while i < n and cmp(arr[i - 1], arr[i]) == decrease:
        i += 1

    run_length = i - st

    return run_length


def reverse_part(arr: "array", left: int, right: int) -> None:
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def insertion_sort(arr: "array", left: int, right: int) -> None:
    for i in range(left + 1, right + 1):
        saved = arr[i]
        j = i - 1
        while j >= left and not cmp(arr[j], saved):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = saved


def inexact_search(arr: "array", t: int) -> int:
    n = len(arr)
    l = 0
    r = n - 1
    res = n
    while l <= r:
        mid = (l + r) // 2
        if cmp(arr[mid], t):
            l = mid + 1
        else:
            res = mid
            r = mid - 1
    return res


def merge(arr: "array", left: int, mid: int, right: int, index_of_merge: int, merge_info: str, gallop_threshold: int) -> (int, str):
    len1 = mid - left + 1
    len2 = right - mid
    left_arr = array('i', arr[left : mid + 1])
    right_arr = array('i', arr[mid + 1 : right + 1])

    i = j = 0
    k = left

    l_count = 0
    r_count = 0
    min_gallop = gallop_threshold
    gallop_count = 0

    while i < len1 and j < len2:
        if cmp(left_arr[i], right_arr[j]):
            arr[k] = left_arr[i]
            l_count += 1
            r_count = 0
            i += 1
            k += 1

            if l_count >= min_gallop:
                gallop_count += 1
                position = inexact_search(array('i', left_arr[i:]), right_arr[j])
                for p in range(position):
                    if i >= len1:
                        break
                    arr[k] = left_arr[i]
                    i += 1
                    k += 1
        else:
            arr[k] = right_arr[j]
            r_count += 1
            l_count = 0
            j += 1
            k += 1
            if r_count >= min_gallop:
                gallop_count += 1
                position = inexact_search(array('i', right_arr[j:]), left_arr[i])
                for p in range(position):
                    if j >= len2:
                        break
                    arr[k] = right_arr[j]
                    j += 1
                    k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

    # for debugging output
    merge_info += f"Gallops {index_of_merge}: {gallop_count}\n"
    merge_info += f"Merge {index_of_merge}: " + " ".join(map(str, arr[left : right + 1])) + "\n"

    return index_of_merge + 1, merge_info


def check_invariant(arr: "array", runs_starts: "array", runs_lens: "array", index_of_merge: int, merge_info: str, gallop_threshold: int) -> (int, str):
    while len(runs_starts) > 1:
        n = len(runs_starts)
        Z = runs_lens[-3] if n >= 3 else float('inf')
        Y = runs_lens[-2]
        X = runs_lens[-1]

        if n >= 3 and Z <= Y + X:
            if Z < X:
                index_of_merge, merge_info = merge_two(arr, runs_starts, runs_lens, n - 3, index_of_merge, merge_info, gallop_threshold)
            else:
                index_of_merge, merge_info = merge_two(arr, runs_starts, runs_lens, n - 2, index_of_merge, merge_info, gallop_threshold)
        elif Y <= X:
            index_of_merge, merge_info = merge_two(arr, runs_starts, runs_lens, n - 2, index_of_merge, merge_info, gallop_threshold)
        else:
            break
    return index_of_merge, merge_info


def merge_two(arr: "array", runs_starts: "array", runs_lens: "array", i: int, index_of_merge: int, merge_info: str, gallop_threshold: int) -> (int, str):
    st1, len1 = runs_starts[i], runs_lens[i]
    st2, len2 = runs_starts[i + 1], runs_lens[i + 1]

    index_of_merge, merge_info = merge(arr, st1, st1 + len1 - 1, st1 + len1 + len2 - 1, index_of_merge, merge_info, gallop_threshold)
    runs_starts[i], runs_lens[i] = st1, len1 + len2
    runs_starts.pop(i + 1)
    runs_lens.pop(i + 1)
    return index_of_merge, merge_info


def timsort(arr: "array", min_run_parametr: int = 16, gallop_threshold: int = 3, choose_min_run=None) -> str:
    n = len(arr)
    min_run = get_min_run(n, min_run_parametr) if choose_min_run is None else choose_min_run    #for research
    runs_starts = array('i')
    runs_lens = array('i')
    i = 0
    index_of_merge = 0
    index_of_sorting = 0

    parts_info = ""
    merge_info = ""
    result = ""

    while i < n:
        run_len = find_natural_run(arr, i)

        if run_len > 1:
            decrease = cmp(arr[i], arr[i + 1])
            if not decrease:
                reverse_part(arr, i, i + run_len - 1)

        if run_len < min_run:
            end = min(i + min_run, n)
            insertion_sort(arr, i, end - 1)
            run_len = end - i

        else:
            insertion_sort(arr, i, i + run_len - 1)

        # for debugging output
        parts_info += f"Part {index_of_sorting}: " + " ".join(map(str, arr[i:i + run_len])) + "\n"
        index_of_sorting += 1

        runs_starts.append(i)
        runs_lens.append(run_len)

        index_of_merge, merge_info = check_invariant(arr, runs_starts, runs_lens, index_of_merge, merge_info, gallop_threshold)
        i += run_len

    while len(runs_lens) > 1:
        index_of_merge, merge_info = merge_two(arr, runs_starts, runs_lens, len(runs_starts) - 2, index_of_merge, merge_info, gallop_threshold)

    # for debugging output
    result += parts_info + merge_info + "Answer: " + " ".join(map(str, arr))
    return result


if __name__ == "__main__":
    n = int(input())
    arr = array('i', map(int, input().split()))
    print(timsort(arr))

