class Node:
    def __init__(self, data):  # data = (priority: int, task: str)
        if data[0] < 0:
            raise ValueError("Приоритет задачи должен быть неотрицательным")
        if not isinstance(data[0], int):
            raise ValueError("Приоритет задачи это целое число")
        if not isinstance(data[1], str):
            raise ValueError("Задача это строка")
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


# static functions:

def get_height(node):
    if not node:
        return 0
    return node.height


def get_min_value_node(root):
    current = root
    while current.left:
        current = current.left
    return current


# rotations, O(1)
def right_rotate(node):
    A = node.left
    Y = A.right

    A.right = node
    node.left = Y

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    A.height = 1 + max(get_height(A.left), get_height(A.right))

    return A


def left_rotate(node):
    B = node.right
    Y = B.left

    B.left = node
    node.right = Y

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    B.height = 1 + max(get_height(B.left), get_height(B.right))

    return B


def get_balance_factor(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)


class AVLTree:
    def __init__(self):
        self.root = None

    # O(log n)
    def _search(self, root, priority):
        if not root:    # не нашелся => None
            return root

        if root.data[0] < priority:
            return self._search(root.right, priority)
        elif root.data[0] > priority:
            return self._search(root.left, priority)
        else:           # нашелся => текущий корневой узел
            return root


    # O(log n)
    def _insert(self, root, data):
        if not root:
            return Node(data)

        if data[0] < root.data[0]:
            root.left = self._insert(root.left, data)
        elif data[0] > root.data[0]:
            root.right = self._insert(root.right, data)
        else:
            raise ValueError(f"Данный приоритет ({data[0]}) уже занят задачей \"{root.data[1]}\"")

        # BALANCING

        root.height = 1 + max(get_height(root.left), get_height(root.right))
        balance_factor = get_balance_factor(root)

        # Right rotation
        if balance_factor > 1 and data[0] < root.left.data[0]:
            return right_rotate(root)

        # Left rotation
        if balance_factor < -1 and data[0] > root.right.data[0]:
            return left_rotate(root)

        # Left-Right rotation
        if balance_factor > 1 and data[0] > root.left.data[0]:
            root.left = left_rotate(root.left)
            return right_rotate(root)

        # Right-Left rotation
        if balance_factor < -1 and data[0] < root.right.data[0]:
            root.right = right_rotate(root.right)
            return left_rotate(root)

        return root


    # O(log n)
    def _delete(self, root, data):
        if not root:
            return root

        if data[0] < root.data[0]:
            root.left = self._delete(root.left, data)
        elif data[0] > root.data[0]:
            root.right = self._delete(root.right, data)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = get_min_value_node(root.right)
            root.data = temp.data
            root.right = self._delete(root.right, temp.data)

        if not root:
            return root

        # BALANCING

        root.height = 1 + max(get_height(root.left), get_height(root.right))
        balance_factor = get_balance_factor(root)

        # Right rotation
        if balance_factor > 1 and get_balance_factor(root.left) >= 0:
            return right_rotate(root)

        # Left rotation
        if balance_factor < -1 and get_balance_factor(root.right) <= 0:
            return left_rotate(root)

        # Left-Right rotation
        if balance_factor > 1 and get_balance_factor(root.left) < 0:
            root.left = left_rotate(root.left)
            return right_rotate(root)

        # Right-Left rotation
        if balance_factor < -1 and get_balance_factor(root.right) > 0:
            root.right = right_rotate(root.right)
            return left_rotate(root)

        return root


    def insert_data(self, data): # O(log n)
        self.root = self._insert(self.root, data)

    def delete_data(self, data): # O(log n)
        self.root = self._delete(self.root, data)

    def search_data(self, data): # O(log n)
        return self._search(self.root, data[0])


    def do_in_order_traversal(self, current, res):    # result is an ascending sequent
        if current is None:
            return
        self.do_in_order_traversal(current.left, res)
        priority, task = current.data
        res.append(f"{priority}) {task}\n")
        self.do_in_order_traversal(current.right, res)



# Здесь реализуем именно сам класс менеджера задач на основе авл дерева,
# тем самым делая шаг абстракции для пользователя, чтобы он не вызывал методы напрямую через авл дерево
class TodoList:
    def __init__(self):
        self._avl_tree = AVLTree()

    def add_task(self, task: str, priority: int):
        self._avl_tree.insert_data((priority, task))


    # удаление только по приоритету
    def delete_task(self, priority):
        self._avl_tree.delete_data((priority, ""))
    
    
    # только по приоритету
    def find_task(self, priority):
        return self._avl_tree.search_data((priority, ""))
    
    
    # поиск + вывод информации о поиске для пользователя
    def find_and_print_task(self, priority):
        res = self.find_task(priority)
        print(f"Поиск задачи с приоритетом {priority} ...")
        print(f"Результат поиска:")
        if not res:
            print("Ничего не найдено. Нет задачи с таким приоритетом")
        else:
            print(f"приоритет: {priority}, задача: {res.data[1]}\n")


    # Отображение отсортированного списка задач в виде строки
    def __str__(self):
        result = []
        root = self._avl_tree.root
        self._avl_tree.do_in_order_traversal(root, result)          # O(n)
        return "".join(result) if result else "Список задач пуст"   # O(n)



# usage example
if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.add_task("write the code", 1)

    todo_list.add_task("write the tests", 3)

    todo_list.add_task("draw the plots", 2)

    todo_list.add_task("go to bed", 5)

    print(todo_list)

    todo_list.add_task("complete code review", 4)

    print(todo_list)

    todo_list.delete_task(3)

    print(todo_list)

    todo_list.add_task("write amazing tests!", 3)

    print(todo_list)

    todo_list.find_and_print_task(1)
    todo_list.find_and_print_task(10)
