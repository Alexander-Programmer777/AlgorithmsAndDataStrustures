class SegmentTree:
    def __init__(self, array_length: int):  # O(n) for tree building
        self.n = array_length
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [0] * (2 * self.size)


    def add_value(self, l: int, r: int, value: int) -> None:   # O(log n)
        if l < 0 or r < 0:
            raise IndexError("Index cannot be negative")

        if r > self.n or l >= self.n:
            raise IndexError("Index out of range")

        l += self.size
        r += self.size

        while l < r:
            if l & 1:
                self.tree[l] += value
                l += 1
            if r & 1:
                r -= 1
                self.tree[r] += value

            l //= 2
            r //= 2


    def get_value(self, index: int) -> int:   # O(log n)
        if index < 0:
            raise IndexError("Index cannot be negative")

        pos = index + self.size
        res = 0

        while pos > 0:
            res += self.tree[pos]
            pos //= 2

        return res


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = []
    st = SegmentTree(n)

    for i in range(m):
        op = list(map(int, input().split()))
        if op[0] == 1:
            l, r, value = op[1:]
            st.add_value(l, r, value)
        else:
            index = op[1]
            res += [st.get_value(index)]

    for i in range(len(res)):
        print(res[i])