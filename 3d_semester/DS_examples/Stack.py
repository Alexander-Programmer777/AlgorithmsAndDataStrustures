class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        self.items.pop()

    def size(self): # O(n). it would be better to cache it!
        return len(self.items)


# UPDATED NEW BEFORE EXAM
class StackArray:
    def __init__(self):
        self.items = []
        self.size = 0    # cahced

    def push(self, elem):
        self.items.append(elem)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("stack is empty")
        self.size -= 1
        return self.items.pop()

    def __len__(self):
        return self.size  # O(1) instead os O(n), cuz it is cached


class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class StackLL:
    # for O(1) we use add into and remove from HEAD (cuz it is naive linked list)

    def __init__(self):
        self.head = None

    def push(self, elem):
        new_node = LinkedListNode(elem, self.head)
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise IndexError("stack is empty")
        val = self.head.val
        self.head = self.head.next
        return val

    def print_list(self):
        tmp = self.head
        while tmp:
            print(tmp.val, end=" -> ")
            tmp = tmp.next




if __name__ == "__main__":

    # 1
    my_stack = StackArray()

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop()) # works

    print()

    # 2
    my_stack = StackLL()

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    print(my_stack.print_list())

    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())  # works









