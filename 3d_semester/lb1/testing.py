import pytest
from aisd.lb1.alg_lb1 import CircularDeque, DequeSizeError


@pytest.fixture
def deque_default():
    return CircularDeque(5, False)


@pytest.fixture
def deque_full():
    dq = CircularDeque(5, False)
    for i in range(5):
        dq.push_back(i)
    return dq


@pytest.fixture
def deque_force():
    return CircularDeque(3, True)


# Тесты инициализации
def test_initialization(deque_default):
    assert deque_default.cap == 5
    assert deque_default.length == 0
    assert deque_default.index_of_front == 0
    assert len(deque_default.deque) == 5


# Тесты добавления элементов
def test_push_front(deque_default):
    for i in range(5):
        deque_default.push_front(i)
        assert deque_default.front() == i
        assert deque_default.size() == i + 1


def test_push_back(deque_default):
    for i in range(5):
        deque_default.push_back(i)
        assert deque_default.back() == i
        assert deque_default.size() == i + 1


# Тесты удаления элементов
def test_pop_front(deque_full):
    for i in range(5):
        assert deque_full.pop_front() == i
        assert deque_full.size() == 5 - i - 1


def test_pop_back(deque_full):
    for i in range(5):
        assert deque_full.pop_back() == 5 - i - 1
        assert deque_full.size() == 5 - i - 1


# Тесты доступа к элементам
def test_front_back(deque_default):
    deque_default.push_front(100)
    deque_default.push_back(200)
    assert deque_default.front() == 100
    assert deque_default.back() == 200


# Тесты проверки состояния
def test_empty_full(deque_default, deque_full):
    assert deque_default.empty()
    assert not deque_default.full()
    assert not deque_full.empty()
    assert deque_full.full()


# Тесты обработки ошибок
def test_push_force_false(deque_full):
    with pytest.raises(DequeSizeError):
        deque_full.push_back(18)


def test_pop_empty(deque_default):
    with pytest.raises(DequeSizeError):
        deque_default.pop_front()
    with pytest.raises(DequeSizeError):
        deque_default.pop_back()


def test_front_back_empty(deque_default):
    with pytest.raises(DequeSizeError):
        deque_default.front()
    with pytest.raises(DequeSizeError):
        deque_default.back()


# Тесты изменения размера
def test_resize():
    dq = CircularDeque(5, False)

    for i in range(3):
        dq.push_back(i)
    dq.resize(8)
    assert dq.cap == 8
    assert dq.size() == 3
    assert dq.pop_front() == 0
    assert dq.pop_front() == 1
    assert dq.pop_front() == 2

    for i in range(3):
        dq.push_back(i)
    dq.resize(2)
    assert dq.cap == 2
    assert dq.size() == 2
    assert dq.pop_front() == 0
    assert dq.pop_front() == 1


def test_resize_negative(deque_default):
    with pytest.raises(ValueError):
        deque_default.resize(-1)


# Тесты кругового поведения
def test_circular_behavior(deque_default):
    for i in range(5):
        deque_default.push_back(i)
    deque_default.pop_front()
    deque_default.pop_front()
    deque_default.push_back(5)
    deque_default.push_back(6)

    assert deque_default.pop_front() == 2
    assert deque_default.pop_front() == 3
    assert deque_default.pop_front() == 4
    assert deque_default.pop_front() == 5
    assert deque_default.pop_front() == 6


# тесты для push_force = true
def test_push_force_true_push_back(deque_force):
    for i in range(1, 4):
        deque_force.push_back(i)
    deque_force.push_back(4)
    assert deque_force.front() == 2
    assert deque_force.back() == 4


def test_push_force_true_push_front(deque_force):
    for i in range(1, 4):
        deque_force.push_back(i)
    deque_force.push_front(4)
    assert deque_force.front() == 4
    assert deque_force.back() == 2


# bash:
# pytest -v testing.py