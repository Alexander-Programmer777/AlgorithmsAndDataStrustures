import pytest
from array import array
from main import timsort
from random import randint


def test_using_random_data():
    for i in range(100):
        N = randint(0, 10_000)
        arr = array('i', [randint(-10_000, 10_000) for i in range(N)])
        correctly_sorted = sorted(arr, key = lambda x: -abs(x))
        timsort(arr, 64, 7)
        
        assert  [abs(elem) for elem in correctly_sorted] == [abs(elem) for elem in arr]


def test_edge_cases():
    testing_arrays = [
        array('i', []),
        array('i', [0]),
        array('i', [7]),
        array('i', [-7]),
        array('i', [0, 0, 0]),
        array('i', [7, 7, 7]),
        array('i', [-7, -7, -7]),
        array('i', [1, -1, 2, -2]),
        array('i', [10] * 100),
    ]

    for arr in testing_arrays:

        correctly_sorted = sorted(arr, key = lambda x: -abs(x))
        timsort(arr)

        assert  [abs(elem) for elem in correctly_sorted] == [abs(elem) for elem in arr]


def test_sorted_arrays():
    testing_arrays = [
        array('i', sorted([randint(-100, 0) for i in range(100)])),
        array('i', sorted([randint(0, 100) for i in range(100)])),
        array('i', sorted([randint(-100, 100) for i in range(100)]))
    ]

    for arr in testing_arrays:
        correctly_sorted = sorted(arr, key = lambda x: -abs(x))
        timsort(arr)

        assert [abs(elem) for elem in correctly_sorted] == [abs(elem) for elem in arr]


def test_reversed_arrays():
    testing_arrays = [
        array('i', sorted([randint(-100, 0) for i in range(100)], reverse=True)),
        array('i', sorted([randint(0, 100) for i in range(100)], reverse=True)),
        array('i', sorted([randint(-100, 100) for i in range(100)], reverse=True))

    ]

    for arr in testing_arrays:
        correctly_sorted = sorted(arr, key = lambda x: -abs(x))
        timsort(arr)

        assert [abs(elem) for elem in correctly_sorted] == [abs(elem) for elem in arr]


def test_huge_array():
    arr = array('i', [randint(-100_000, 100_000) for i in range(100_000)])
    correctly_sorted = sorted(arr, key = lambda x: -abs(x))
    timsort(arr, 64, 7)

    assert [abs(elem) for elem in correctly_sorted] == [abs(elem) for elem in arr]


def test_duplicates_and_symmetry():
    testing_arrays = [
        array('i', [5, -5, 5, -5, 5, -5]),
        array('i', [3, -3, 2, -2, 1, -1]),
        array('i', [10, -10, 10, -10, 5, -5, 5, -5]),
        array('i', [0, 1, -1, 0, 2, -2, 0, 3, -3])
    ]

    for arr in testing_arrays:
        correctly_sorted = sorted(arr, key = lambda x: -abs(x))
        timsort(arr)

        assert [abs(elem) for elem in correctly_sorted] == [abs(elem) for elem in arr]


def test_examples_sorting():
    arr1 = array('i', [1, -2, 3, -4, 5, 6, -7, -8, 9, -10, 11, -10, -9, 8, 7, -7, -6, 6, 5, 4])
    arr2 = array('i', [-1, 2, 3, 4, 5, -6, 7, 8, -8, -8, 7, -7, 7, 6, -5, 4])

    timsort(arr1)
    timsort(arr2)

    assert arr1.tolist() == [11, -10, -10, 9, -9, -8, 8, -7, 7, -7, 6, -6, 6, 5, 5, -4, 4, 3, -2, 1]
    assert arr2.tolist() == [8, -8, -8, 7, 7, -7, 7, 6, -6, 5, -5, 4, 4, 3, 2, -1]


def test_examples_output():
    arr1 = array('i', [1, -2, 3, -4, 5, 6, -7, -8, 9, -10, 11, -10, -9, 8, 7, -7, -6, 6, 5, 4])
    arr2 = array('i', [-1, 2, 3, 4, 5, -6, 7, 8, -8, -8, 7, -7, 7, 6, -5, 4])

    output1 = timsort(arr1)
    output2 = timsort(arr2)
    correct1 = ("Part 0: 11 -10 9 -8 -7 6 5 -4 3 -2 1\n" + "Part 1: -10 -9 8 7 -7 -6 6 5 4\n" + "Gallops 0: 0\n" +
                "Merge 0: 11 -10 -10 9 -9 -8 8 -7 7 -7 6 -6 6 5 5 -4 4 3 -2 1\n" +
                "Answer: 11 -10 -10 9 -9 -8 8 -7 7 -7 6 -6 6 5 5 -4 4 3 -2 1")

    correct2 = ("Part 0: 8 7 -6 5 4 3 2 -1\n" + "Part 1: -8 -8 7 -7 7 6 -5 4\n" + "Gallops 0: 1\n" +
                "Merge 0: 8 -8 -8 7 7 -7 7 6 -6 5 -5 4 4 3 2 -1\n" + "Answer: 8 -8 -8 7 7 -7 7 6 -6 5 -5 4 4 3 2 -1")

    assert output1 == correct1
    assert output2 == correct2

if __name__ == "__main__":
    pytest.main([__file__, "-v"])


# or using bash: pytest -v testing.py in work directory