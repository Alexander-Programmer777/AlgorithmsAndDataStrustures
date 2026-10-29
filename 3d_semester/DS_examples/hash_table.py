class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_table = [None] * capacity
        self.count = 0

    def hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        hash_code = self.hash(key)
        self.count += 1
        if self.hash_table[hash_code] is None:
            self.hash_table[hash_code] = (key, value)
        else: #collision
            i = hash_code
            while self.hash_table[i] is not None:
                i += 1               # open addressing with linear probing
                if i == self.capacity:
                    i = 0
            self.hash_table[i] = (key, value)

        if self.count / self.capacity >= 0.75:
            self._resize()

    def search(self, key):
        hash_code = self.hash(key)
        i = hash_code
        while i != hash_code - 1: #full loop
            if self.hash_table[i] is not None and self.hash_table[i][0] == key:
                return self.hash_table[i]
            i += 1
            if i == self.capacity:
                i = 0
        return None

    def remove(self, key):
        hash_code = self.hash(key)
        i = hash_code

        while i != hash_code - 1:
            if self.hash_table[i] is not None and self.hash_table[i][0] == key:
                self.hash_table[i] = None
                self.count -= 1
                return
            i += 1
            if i == self.capacity:
                i = 0

    def _resize(self):
        capacity = self.capacity * 2
        hash_table = HashTable(capacity)    #is empty
        for el in self.hash_table:
            if el is not None:
                hash_table.insert(el[0], el[1])
        self.hash_table = hash_table.hash_table
        self.capacity = capacity

# UPD
class HashMapChain:
    """Chain storage for collision solving"""
    def __init__(self, start_capacity: int):
        self.capacity = start_capacity
        self.arr = [list() for _ in range(start_capacity)]
        self.size = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        self.capacity *= 2
        prev_arr = self.arr
        self.arr = [list() for _ in range(self.capacity)]

        for bucket in prev_arr:
            if bucket:
                for i, (k, v) in enumerate(bucket):
                    new_index = self._hash(k)
                    self.arr[new_index].append((k, v))

    def add(self, key, value):
        index = self._hash(key)
        if not self.arr[index]:
            self.arr[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.arr[index]):
                if k == key:
                    self.arr[index][i] = (key, value)
                    return
            self.arr[index].append((key, value))

        self.size += 1
        if self.size / self.capacity >= 0.75:
            self._resize()

    def find(self, key):
        index = self._hash(key)
        ln = len(self.arr[index])
        if ln == 0:
            return None
        elif ln == 1:
            return self.arr[index][0][1]
        else: # collision
            for elem in self.arr[index]:
                if elem[0] == key:
                    return elem[1]

    def delete(self, key):
        index = self._hash(key)
        ln = len(self.arr[index])
        if ln == 0:
            raise ValueError
        elif ln == 1:
            self.arr[index] = []
        else:  # collision
            for i, elem in enumerate(self.arr[index]):
                if elem[0] == key:
                    self.arr[index].pop(i)
        self.size -= 1


class HashMapOpenAddressing:
    """Open addressing (linear probing) for collision solving"""
    # linear probing is the easiest, but remember about square probing and double hashing for finding the step

    def __init__(self, start_capacity):
        self.capacity = start_capacity
        self.arr = [None] * start_capacity
        self.size = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        new_hash_table = HashMapOpenAddressing(self.capacity * 2)
        for elem in self.arr:
            if elem:
                new_hash_table.add(elem[0], elem[1])
        self.arr = new_hash_table.arr


    def add(self, key, value):
        index = self._hash(key)
        if self.arr[index] is None: # free
            self.arr[index] = (key, value)
            self.size += 1
        else: # collision
            i = index + 1
            while i != index - 1:
                if i == self.capacity:
                    i = 0
                if self.arr[i] is None:
                    self.arr[i] = (key, value)
                    self.size += 1
                    break
                i += 1

        if self.size / self.capacity >= 0.75:
            self._resize()

    def find(self, key):
        index = self._hash(key)
        i = index
        while i != index - 1:
            if i == self.capacity:
                i = 0
            if self.arr[i] is not None and self.arr[i][0] == key:
                return self.arr[i][1]
            i += 1
        return None

    def delete(self, key):
        index = self._hash(key)
        i = index
        while i != index - 1:
            if i == self.capacity:
                i = 0
            if self.arr[i] is not None and self.arr[i][0] == key:
                self.arr[i] = None
                break
            i += 1


if __name__ == "__main__":
    # hm = HashMapChain(8)
    # hm.add(0, "A")
    # hm.add(1, "b")
    # hm.add(2, "c")
    # hm.add(3, "d")
    # hm.add(4, "s")
    #
    # print(hm.arr)
    #
    # hm.delete(0)
    # hm.delete(3)
    #
    # print(hm.arr) # works

    hm = HashMapOpenAddressing(8)
    hm.add(0, "A")
    hm.add(1, "b")
    hm.add(2, "c")
    hm.add(3, "d")
    hm.add(4, "s")

    print(hm.arr)

    hm.delete(0)
    hm.delete(3)

    print(hm.arr)




    ...

