
# stored like an array, not like a BS tree fex
class SumSegmentTree:
    def __init__(self, arr):    # Space complexity O(n), Time O(n)
        n = len(arr)
        self.size = 1                         # only for nodes, not leaves
        while self.size < n:                  # the loop is needed, cuz tree_array length = 2^smth, that is first more than n
            self.size *= 2
        self.tree = [0] * (2 * self.size)     # *2 for leaves

        # alternating way:
        # import math
        # self.size = 1 << (math.ceil(math.log2(self.n)))  # bit shift

        # Fill leaves, where the array elements are stored
        for i in range(n):
            self.tree[self.size + i] = arr[i]

        # tree build from down to up
        for i in range(self.size - 1, 0, -1):       # [0] is empty
            self.tree[i] = (self.tree[2 * i] + self.tree[2 * i + 1])  # it depends on tree main operation !!



    def update(self, index, value): # Time complexity O(log n)
        pos = self.size + index
        self.tree[pos] = value     # insertion is done
                                   # then we need to update help info
        pos //= 2                  # now pos is a parent of inserted value

        while pos >= 1:            # parents traversal and update
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]
            pos //= 2


    # O(log n)
    def query_sum(self, l, r):       # we consider half-closed interval [l, r) = [l, r-1], cuz it is discrete
        l += self.size
        r += self.size
        res = 0

        while l < r:
            if l & 1:              # last bit is 1, so it is odd, right child
                res += self.tree[l]
                l += 1             # jump to next node
            if r & 1:
                r -= 1
                res += self.tree[r]

            l //= 2               # jump to parents
            r //= 2

        return res


# sst = SumSegmentTree([1, 2, 3, 4, 5, 6, 7])
# print(sst.tree)




class MinSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [[0, 1] for _ in range((2 * self.size))]

        # leaves
        for i in range(self.n):
            self.tree[self.size + i] = [arr[i], 1]


        for i in range(self.size - 1, 0, -1):
            left_child = self.tree[i * 2]
            right_child = self.tree[i * 2 + 1]
            if left_child[0] < right_child[0]:
                self.tree[i] = left_child
            elif left_child[0] > right_child[0]:
                self.tree[i] = right_child
            else:
                self.tree[i] = [right_child[0], right_child[1] + left_child[1]]


    def update(self, index, value):
        i = self.size + index
        self.tree[i] = [value, 1]

        i //= 2

        while i >= 1:

            left_child = self.tree[i * 2]
            right_child = self.tree[i * 2 + 1]
            if left_child[0] < right_child[0]:
                self.tree[i] = left_child
            elif left_child[0] > right_child[0]:
                self.tree[i] = right_child
            else:
                self.tree[i] = [right_child[0], right_child[1] + left_child[1]]

            i //= 2



    def query_min(self, l, r):
        l += self.size
        r += self.size
        res_min = [float("inf"), 0]

        while l < r:
            if l & 1:
                if res_min[0] > self.tree[l][0]:
                    res_min = self.tree[l]
                elif res_min[0] == self.tree[l][0]:
                    res_min[1] += self.tree[l][1]
                l += 1
            if r & 1:
                r -= 1
                if res_min[0] > self.tree[r][0]:
                    res_min = self.tree[r]
                elif res_min[0] == self.tree[r][0]:
                    res_min[1] += self.tree[r][1]

            l //= 2
            r //= 2

        return res_min






# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     arr = list(map(int, input().split()))
#     res = []
#
#     mst = MinSegmentTree(arr)
#
#     for i in range(m):
#         op = list(map(int, input().split()))
#         if op[0] == 1:
#             index, val = op[1:]
#             mst.update(index, val)
#         else:
#             l, r = op[1:]
#             res += [mst.query_min(l, r)]
#
#     print(mst.tree)
#     print(*res)














# prefix sum practice

# n = int(input())
# arr = list(map(int, input().split()))
# pref_s = [arr[0]] + [0] * (n - 1)
# for i in range(1, n):
#     pref_s[i] = pref_s[i - 1] + arr[i]
# print(pref_s)
#
# m = int(input())
# for i in range(m):
#     l, r = map(int, input().split())
#     print(pref_s[r] - pref_s[l])