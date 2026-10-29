class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0 if head is None else 1

    def append(self, val): # O(n)
        tmp = self.head
        self.size += 1
        if tmp is None:
            self.head = Node(val)
            return

        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(val)


    def insert_on_head(self, val): # O(1)
        new_node = Node(val, self.head)
        self.head = new_node
        self.size += 1


    def insert_on_index(self, val, index):
        if index > self.size - 1:
            raise IndexError

        if index == 0:
            self.insert_on_head(val)
            return
        if index == self.size - 1:
            self.append(val)
            return

        cur_idx = 0
        tmp = self.head
        while cur_idx != index - 1:
            cur_idx += 1
            tmp = tmp.next

        new_node = Node(val, tmp.next)
        tmp.next = new_node
        self.size += 1


    def delete_on_head(self):
        if self.head is None:
            raise IndexError
        self.head = self.head.next
        self.size -= 1


    def delete_on_tail(self):
        if self.head is None:
            raise IndexError

        tmp = self.head
        if self.size == 1:
            self.head = None
            self.size -= 1
            return

        while tmp.next.next:
            tmp = tmp.next

        tmp.next = None
        self.size -= 1


    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.val, end=" -> ")
            tmp = tmp.next
        print(f" size = {self.size}")



class DLLNode:
    def __init__(self, val, next=None, prev=None):
        self.next = next
        self.val = val
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  

    def push_front(self, val):
        """Вставка в начало - O(1)"""
        new_node = DLLNode(val, self.head, None)

        if self.head is not None:
            self.head.prev = new_node
        else:
            # Если список был пустой, tail тоже указывает на новый узел
            self.tail = new_node

        self.head = new_node
        self.size += 1


    def push_back(self, val):
        """Вставка в конец - O(1) (теперь быстро!)"""
        new_node = DLLNode(val, None, self.tail)

        if self.tail is not None:
            self.tail.next = new_node
        else:
            # Если список был пустой, head тоже указывает на новый узел
            self.head = new_node

        self.tail = new_node
        self.size += 1


    def insert_at(self, val, index):
        """Вставка по индексу - O(n) в худшем случае"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.push_front(val)
            return
        if index == self.size:
            self.push_back(val)
            return

        # Выбираем направление обхода (оптимизация!)
        if index < self.size // 2:
            # Идем с начала
            tmp = self.head
            for _ in range(index):
                tmp = tmp.next
        else:
            # Идем с конца
            tmp = self.tail
            for _ in range(self.size - index - 1):
                tmp = tmp.prev

        # Вставляем перед tmp
        new_node = DLLNode(val, tmp, tmp.prev)
        tmp.prev.next = new_node
        tmp.prev = new_node
        self.size += 1


    def pop_front(self):
        """Удаление из начала - O(1)"""
        if self.head is None:
            raise IndexError("List is empty")

        value = self.head.val

        if self.head.next is not None:
            self.head.next.prev = None
        else:
            # Если был один элемент, обнуляем tail
            self.tail = None

        self.head = self.head.next
        self.size -= 1
        return value


    def pop_back(self):
        """Удаление с конца - O(1) (теперь быстро!)"""
        if self.tail is None:
            raise IndexError("List is empty")

        value = self.tail.val

        if self.tail.prev is not None:
            self.tail.prev.next = None
        else:
            # Если был один элемент, обнуляем head
            self.head = None

        self.tail = self.tail.prev
        self.size -= 1
        return value


    def remove_at(self, index):
        """Удаление по индексу - O(n) в худшем случае"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            return self.pop_front()
        if index == self.size - 1:
            return self.pop_back()

        # Выбираем направление обхода
        if index < self.size // 2:
            tmp = self.head
            for _ in range(index):
                tmp = tmp.next
        else:
            tmp = self.tail
            for _ in range(self.size - index - 1):
                tmp = tmp.prev

        # Удаляем tmp
        value = tmp.val
        tmp.prev.next = tmp.next
        tmp.next.prev = tmp.prev
        self.size -= 1
        return value

    def get(self, index):
        """Получение элемента по индексу - O(n)"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        # Оптимизация: выбираем направление
        if index < self.size // 2:
            tmp = self.head
            for _ in range(index):
                tmp = tmp.next
        else:
            tmp = self.tail
            for _ in range(self.size - index - 1):
                tmp = tmp.prev

        return tmp.val

    def print_forward(self):
        """Печать списка от начала к концу"""
        tmp = self.head
        elements = []
        while tmp:
            elements.append(str(tmp.val))
            tmp = tmp.next
        print(" <-> ".join(elements) + f" (size={self.size})")

    def print_backward(self):
        """Печать списка от конца к началу (проверка prev указателей)"""
        tmp = self.tail
        elements = []
        while tmp:
            elements.append(str(tmp.val))
            tmp = tmp.prev
        print(" <-> ".join(elements) + f" (size={self.size})")



# Небольшой тест
if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.push_back(10)
    dll.push_back(20)
    dll.push_front(5)  # 5 <-> 10 <-> 20

    dll.print_forward()  # 5 <-> 10 <-> 20
    dll.print_backward() # 20 <-> 10 <-> 5

    dll.insert_at(15, 2)  # 5 <-> 10 <-> 15 <-> 20
    print(dll.pop_back())  # 20
    print(dll.pop_front()) # 5

    dll.print_forward()  # 10 <-> 15



#
# if __name__ == "__main__":
#     ll = LinkedList()
#     ll.append(1)
#     ll.append(2)
#     ll.append(3)
#     ll.print_list()
#     ll.insert_on_index(4, 1)
#     ll.print_list()
#     ll.insert_on_head(52)
#     ll.print_list()
#     ll.delete_on_head()
#     ll.print_list()
#     ll.delete_on_tail()
#     ll.print_list()
#     ll.delete_on_tail()
#     ll.print_list()
#     ll.delete_on_tail()
#     ll.print_list()
#     ll.delete_on_tail()
#     ll.print_list()
















