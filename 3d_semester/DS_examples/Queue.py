import time
import matplotlib.pyplot as plt

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item): # O(1)
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def dequeue(self): # O(n) - awful => redo with deq
        if self.is_empty():
            raise IndexError("Q is empty")
        self.items.pop(0)

    def get_first(self):
        return self.items[0]

class LLNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class QueueArray:
    def __init__(self, start_capacity):
        self.capacity = start_capacity
        self.size = 0
        self.arr = [None] * start_capacity
        self.head = 0   # for dequeue
        self.tail = 0   # for enqueue

    def enqueue(self, elem): # O(1) amortized
        if self.size == self.capacity:
            self._resize()
        self.arr[self.tail] = elem
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self): # O(1)
        if self.size == 0:
            raise IndexError
        elem = self.arr[self.head]
        self.arr[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return elem

    def _resize(self): # O(n)
        new_cap = self.capacity * 2
        new_arr = [None] * new_cap
        for i in range(self.capacity):
            new_arr[i] = self.arr[(i + self.head) % self.capacity]

        self.arr = new_arr
        self.capacity = new_cap
        self.head = 0
        self.tail = self.size

    def print_q(self):
        print(self.arr)


class QueueLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, elem):
        """addition to the tail"""
        self.size += 1
        if self.tail is None:
            new_elem = LLNode(elem, None, None)
            self.head = new_elem
            self.tail = new_elem
        else:
            new_elem = LLNode(elem, None, self.tail)
            self.tail.next = new_elem
            self.tail = new_elem

    def dequeue(self):
        """deletion from the head"""
        if self.head is None:
            raise IndexError
        self.size -= 1
        elem = self.head.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        return elem

    def print_q(self):
        tmp = self.head
        while tmp:
            print(tmp.val, end = " <-> ")
            tmp = tmp.next
        print("size =", self.size)


def research_q_ADD():
    repeats = 100
    sizes = [10, 100, 1_000, 10_000, 100_000]
    times_ll = []
    times_arr = []
    for size in sizes:
        # заполнить их на 9/10
        q_ll = QueueLL()
        q_arr = QueueArray(2)
        for i in range(size // 10 * 9):
            q_ll.enqueue(i)
            q_arr.enqueue(i)

        total_ll = 0
        total_arr = 0
        for i in range(repeats):
            st_ll = time.perf_counter()
            q_ll.enqueue(i)
            end_ll = time.perf_counter()
            total_ll += end_ll - st_ll

            st_arr = time.perf_counter()
            q_arr.enqueue(i)
            end_arr = time.perf_counter()
            total_arr += end_arr - st_arr

        times_ll += [total_ll / repeats]
        times_arr += [total_arr / repeats]

    plt.figure(1, (10, 6))
    plt.plot(sizes, times_ll, label="ll")
    plt.plot(sizes, times_arr, label="arr")
    plt.legend()

    plt.grid(True)
    plt.show()





class DequeArray:
    def __init__(self, start_capacity):
        self.capacity = start_capacity
        self.size = 0
        self.arr = [None] * start_capacity
        self.head = 0
        self.tail = 0

    def append_right(self, elem): # O(1) amortized
        if self.size == self.capacity:
            self._resize()
        self.arr[self.tail] = elem
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def pop_left(self): # O(1)
        if self.size == 0:
            raise IndexError
        elem = self.arr[self.head]
        self.arr[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return elem

    def pop_right(self): # O(1)
        if self.size == 0:
            raise IndexError
        self.tail = (self.tail - 1) % self.capacity
        elem = self.arr[self.tail]
        self.arr[self.tail] = None
        self.size -= 1
        return elem

    def append_left(self, elem):
        if self.size == self.capacity:
            self._resize()
        self.head = (self.head - 1) % self.capacity
        self.arr[self.head] = elem
        self.size += 1

    def _resize(self): # O(n)
        new_cap = self.capacity * 2
        new_arr = [None] * new_cap
        for i in range(self.capacity):
            new_arr[i] = self.arr[(i + self.head) % self.capacity]

        self.arr = new_arr
        self.capacity = new_cap
        self.head = 0
        self.tail = self.size

    def print_q(self):
        print(self.arr)



class DequeLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append_right(self, elem):
        """addition to the tail"""
        self.size += 1
        if self.tail is None:
            new_elem = LLNode(elem, None, None)
            self.head = new_elem
            self.tail = new_elem
        else:
            new_elem = LLNode(elem, None, self.tail)
            self.tail.next = new_elem
            self.tail = new_elem

    def append_left(self, elem):
        """addition to the head"""
        self.size += 1
        if self.head is None:
            new_elem = LLNode(elem, None, None)
            self.head = new_elem
            self.tail = new_elem
        else:
            new_elem = LLNode(elem, self.head, None)
            self.head.prev = new_elem
            self.head = new_elem

    def pop_left(self):
        """deletion from the head"""
        if self.head is None:
            raise IndexError
        self.size -= 1
        elem = self.head.val
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        return elem

    def pop_right(self):
        """deletion from the tail"""
        if self.head is None:
            raise IndexError
        self.size -= 1
        elem = self.tail.val
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        return elem

    def print_q(self):
        tmp = self.head
        while tmp:
            print(tmp.val, end = " <-> ")
            tmp = tmp.next
        print("size =", self.size)



if __name__ == "__main__":
    # q = QueueArray(2)
    # q.enqueue(1)
    # q.print_q()
    # q.enqueue(2)
    # q.print_q()
    # q.enqueue(3)
    # q.print_q()
    # q.enqueue(4)
    # q.print_q()
    # q.dequeue()
    # q.print_q()
    # q.dequeue()
    # q.print_q()
    # q.dequeue()
    # q.print_q()
    # q.dequeue()
    # q.print_q() #works

    # dq = DequeArray(2)
    # dq.append_right(1)
    # dq.append_right(2)
    # dq.append_right(3)
    # dq.print_q()
    # dq.pop_right()
    # dq.print_q()
    # dq.pop_left()
    # dq.print_q() # works

    # q = QueueLL()
    # q.enqueue(1)
    # q.print_q()
    # q.enqueue(2)
    # q.print_q()
    # q.enqueue(3)
    # q.print_q()
    # q.enqueue(4)
    # q.print_q()
    # q.dequeue()
    # q.print_q()
    # q.dequeue()
    # q.print_q()
    # q.dequeue()
    # q.print_q()
    # q.dequeue()
    # q.print_q() # works

    research_q_ADD()





