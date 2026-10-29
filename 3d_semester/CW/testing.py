import pytest
from main import TodoList


class TestTodoListBasic:
    def test_empty_todo_list(self):
        todo = TodoList()
        assert str(todo) == "Список задач пуст"


    def test_add_single_task(self):
        todo = TodoList()
        todo.add_task("Позвонить маме", 1)
        assert "1) Позвонить маме\n" == str(todo)


    def test_add_multiple_tasks_sorted(self):
        todo = TodoList()
        todo.add_task("Задача 3", 3)
        todo.add_task("Задача 1", 1)
        todo.add_task("Задача 2", 2)

        result = str(todo)

        assert result.index("1)") < result.index("2)") < result.index("3)")


    def test_delete_task(self):
        todo = TodoList()
        todo.add_task("Купить молоко", 2)
        todo.add_task("Сделать уроки", 1)

        todo.delete_task(1)

        assert "1) Сделать уроки" not in str(todo)
        assert "2) Купить молоко" in str(todo)


    def test_find_existing_task(self):
        todo = TodoList()
        todo.add_task("Важная задача", 5)

        node = todo.find_task(5)
        assert node is not None
        assert node.data[1] == "Важная задача"


    def test_find_non_existing_task(self):
        todo = TodoList()
        todo.add_task("Задача", 1)

        assert todo.find_task(99) is None


    def test_str(self):
        todo = TodoList()
        cmp_result = ""
        for i in range(1, 11):
            cmp_result += f"{i}) {i}\n"
            todo.add_task(str(i), i)

        assert str(todo) == cmp_result


class TestTodoListErrorCases:
    def test_duplicate_priority_error(self):
        todo = TodoList()
        todo.add_task("Первая задача", 1)

        with pytest.raises(ValueError, match="уже занят"):
            todo.add_task("Вторая задача с тем же приоритетом", 1)


    def test_delete_from_empty_list(self):
        todo = TodoList()
        # Не должно вызывать ошибок
        todo.delete_task(1)
        assert str(todo) == "Список задач пуст"


    def test_delete_non_existing_task(self):
        todo = TodoList()
        todo.add_task("Задача 1", 1)

        # Не должно вызывать ошибок
        todo.delete_task(999)
        assert "1) Задача 1\n" == str(todo)


    def test_negative_priority(self):
        todo = TodoList()
        with pytest.raises(ValueError, match="Приоритет задачи должен быть неотрицательным"):
            todo.add_task("Отрицательная задача", -1)


    def test_not_int_priority(self):
        todo = TodoList()
        with pytest.raises(ValueError, match="Приоритет задачи это целое число"):
            todo.add_task("Задача с дробным приоритетом", 1.5)


    def test_not_str_task(self):
        todo = TodoList()
        with pytest.raises(ValueError, match="Задача это строка"):
            todo.add_task(777, 1)


class TestTodoListEdgeCases:
    def test_single_task_operations(self):
        todo = TodoList()

        todo.add_task("Единственная задача", 1)
        assert str(todo) == "1) Единственная задача\n"

        # Ищем её
        node = todo.find_task(1)
        assert node.data[1] == "Единственная задача"

        # Удаляем
        todo.delete_task(1)
        assert str(todo) == "Список задач пуст"

        # Пробуем найти удаленную
        assert todo.find_task(1) is None


    def test_consecutive_priorities(self):      # последовательный приоритет
        todo = TodoList()

        for i in range(1, 11):
            todo.add_task(f"Задача {i}", i)

        # Удаляем каждую вторую
        for i in range(2, 11, 2):
            todo.delete_task(i)

        result = str(todo)
        # Проверяем, что остались только нечетные
        for i in range(1, 11):
            if i % 2 == 1:
                assert f"{i}) Задача {i}" in result
            else:
                assert f"{i}) Задача {i}" not in result


    def test_very_large_priority_numbers(self):
        todo = TodoList()

        large_numbers = [1000000, 999999, 0]

        for num in large_numbers:
            todo.add_task(f"Задача {num}", num)

        result = str(todo)
        lines = result.strip().split('\n')

        assert len(lines) == 3

        assert str(todo) ==  "0) Задача 0\n999999) Задача 999999\n1000000) Задача 1000000\n"

    def test_zero_priority(self):
        todo = TodoList()
        todo.add_task("0 приоритет задача", 0)

        assert str(todo) == "0) 0 приоритет задача\n"


    def test_empty_string_task(self):
        todo = TodoList()
        todo.add_task("", 1)

        assert str(todo) == "1) \n"


class TestTodoListIntegration:
    def test_daily_todo_plot(self):
        todo = TodoList()

        # Утро: добавляем задачи на день
        morning_tasks = [
            ("Зарядка", 1),
            ("Завтрак", 2),
            ("Работа", 3),
            ("Обед", 4),
            ("Тренировка", 5)
        ]

        for task, priority in morning_tasks:
            todo.add_task(task, priority)

        # День: отмечаем выполненные
        todo.delete_task(1)  # Сделали зарядку
        todo.delete_task(2)  # Позавтракали

        # Вечер: добавляем вечерние задачи
        todo.add_task("Ужин", 6)
        todo.add_task("Отдых", 7)

        result = str(todo)

        assert "1) Зарядка" not in result
        assert "2) Завтрак" not in result

        assert "3) Работа" in result
        assert "4) Обед" in result
        assert "5) Тренировка" in result
        assert "6) Ужин" in result
        assert "7) Отдых" in result



if __name__ == "__main__":
    pytest.main([__file__, "-v"])
# or in bash pytest -v testing.py