class DequeSizeError(Exception):
    pass

class CircularDeque:
    def __init__(self, n: int, push_force: bool):
        self.cap = n
        self.push_force = push_force
        self.length = 0
        self.index_of_front = 0
        self.deque = [0] * n


    def push_front(self, x: int):
        if self.length == self.cap:
            if not self.push_force:
                raise DequeSizeError("Deque is full. Pushing cannot be done.")
            index_of_back = (self.index_of_front + self.length - 1) % self.cap
            self.deque[index_of_back] = x
            self.index_of_front = (self.index_of_front - 1) % self.cap
        else:
            self.index_of_front = (self.index_of_front - 1) % self.cap
            self.deque[self.index_of_front] = x
            self.length += 1


    def push_back(self, x: int):
        if self.length == self.cap:
            if not self.push_force:
                raise DequeSizeError("Deque is full. Pushing cannot be done.")
            self.deque[self.index_of_front] = x
            self.index_of_front = (self.index_of_front + 1) % self.cap
        else:
            index_of_new_back = (self.index_of_front + self.length) % self.cap
            self.deque[index_of_new_back] = x
            self.length += 1


    def pop_front(self) -> int:
        if self.length == 0:
            raise DequeSizeError("Deque is empty. Deletion cannot be done.")
        res = self.deque[self.index_of_front]
        self.index_of_front = (self.index_of_front + 1) % self.cap
        self.length -= 1
        return res


    def pop_back(self) -> int:
        if self.length == 0:
            raise DequeSizeError("Deque is empty. Deletion cannot be done.")
        index_of_back = (self.index_of_front + self.length - 1) % self.cap
        res = self.deque[index_of_back]
        self.length -= 1
        return res


    def front(self) -> int:
        if self.length == 0:
            raise DequeSizeError("Deque is empty.")
        return self.deque[self.index_of_front]


    def back(self) -> int:
        if self.length == 0:
            raise DequeSizeError("Deque is empty.")
        index_of_back = (self.index_of_front + self.length - 1) % self.cap
        return self.deque[index_of_back]


    def size(self) -> int:
        return self.length


    def empty(self) -> bool:
        return self.length == 0


    def full(self) -> bool:
        return self.length == self.cap


    def resize(self, new_capacity : int):
        if new_capacity < 0:
            raise ValueError("New capacity cannot be negative.")
        if new_capacity == self.cap:
            return
        new_deque = [0] * new_capacity       #O(new_capacity)
        amount_to_copy = min(self.length, new_capacity)
        for i in range(amount_to_copy):      #O(amount_to_copy)
            prev_index = (self.index_of_front + i) % self.cap
            new_deque[i] = self.deque[prev_index]
        self.deque = new_deque
        self.cap = new_capacity
        self.length = amount_to_copy
        self.index_of_front = 0




#     #additional method for debugging
#     def __str__(self):
#         elements_of_array = list(map(str, self.deque))
#         elements_of_ans = []
#         for i in range(self.length):
#             index = (self.index_of_front + i) % self.cap
#             elements_of_ans += [self.deque[index]]
#         elements_of_ans = list(map(str, elements_of_ans))
#         return (f"array = [{", ".join(elements_of_array)}]\n"
#                 f"ans = [{", ".join(elements_of_ans)}]"
#                 f"\nfront = {self.front()}\nback = {self.back()}")
#
# dq = CircularDeque(3, True)
#
# dq.push_back(1)
# dq.push_back(2)
# dq.push_back(3)
# dq.pop_back()
# print(dq)