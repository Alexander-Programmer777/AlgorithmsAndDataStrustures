"""Rope data structure implementation"""

class Node:
    def __init__(self, left=None, right=None, substring=None):
        self.substring = substring
        self.left = left
        self.right = right
        self.height = 1

        if self.is_leaf():
            self.weight = len(substring)
        else:
            self.weight = 0

    def is_leaf(self):
        return self.left is None and self.right is None


class Rope:

    def __init__(self, MAX_LEAF=8, string=""):    # O(n log n), n = len(string)
        self.MAX_LEAF = MAX_LEAF
        self.root = self.__build_from_string(string)

    # auxiliary private methods

    def __build_from_string(self, string):    # O(n log n), n = len(string)
        if not string:
            return None
        if len(string) <= self.MAX_LEAF:
            return Node(substring=string)
        mid = len(string) // 2
        left = self.__build_from_string(string[:mid])
        right = self.__build_from_string(string[mid:])

        return self.__concat(left, right)


    def __get_height(self, node):      # O(1)
        return node.height if node else 0


    def __get_balance_factor(self, node):      # O(1)
        return self.__get_height(node.left) - self.__get_height(node.right) if node else 0


    def __update_info(self, node):     # O(log n) because of __get_length
        if node is None:
            return
        node.height = 1 + max(self.__get_height(node.left), self.__get_height(node.right))

        if not node.is_leaf():
            node.weight = self.__get_length(node.left)


    def __get_length(self, node):    # O(log n) - tree depth
        if node is None:
            return 0
        if node.is_leaf():
            return len(node.substring)
        return self.__get_length(node.left) + self.__get_length(node.right)


    # two types of rotation
    def __rotate_left(self, node):       # O(log n) because of __update_info
        if node is None or node.right is None:
            return node
        B = node.right
        Y = B.left

        B.left = node
        node.right = Y

        self.__update_info(node)
        self.__update_info(B)

        return B


    def __rotate_right(self, node):     # # O(log n) because of __update_info
        if node is None or node.left is None:
            return node
        A = node.left
        Y = A.right

        A.right = node
        node.left = Y

        self.__update_info(node)
        self.__update_info(A)

        return A


    def __balance_node(self, node):     # O(log n)
        if node is None:
            return None

        self.__update_info(node)

        bf = self.__get_balance_factor(node)

        # Right rotation
        if bf > 1 and self.__get_balance_factor(node.left) >= 0:
            return self.__rotate_right(node)

        # Left rotation
        if bf < -1 and self.__get_balance_factor(node.right) <= 0:
            return self.__rotate_left(node)

        # Left-Right rotation (Big Right rotation)
        if bf > 1 and self.__get_balance_factor(node.left) < 0:
            node.left = self.__rotate_left(node.left)
            return self.__rotate_right(node)

        # Right-Left rotation (Big Left rotation)
        if bf < -1 and self.__get_balance_factor(node.right) > 0:
            node.right = self.__rotate_right(node.right)
            return self.__rotate_left(node)

        return node


    def __concat(self, left, right):    # O(log n)
        if left is None:
            return right
        if right is None:
            return left

        node = Node(left=left, right=right)

        return self.__balance_node(node)


    # main public methods


    def index(self, ind, node=None):    # O(log n)
        if node is None:
            node = self.root
        if node is None:
            raise IndexError("Rope is empty")
        if ind < 0 or ind >= self.__get_length(node):
            raise IndexError(f"Index {ind} out of range")

        if node.is_leaf():
            return node.substring[ind]

        if ind < node.weight:
            return self.index(ind, node.left)
        else:
            return self.index(ind - node.weight, node.right)


    def split(self, node, ind):         # O(log n)
        if node is None:
            return None, None

        if ind < 0 or ind > self.__get_length(node):
            raise IndexError(f"Split index {ind} out of range")

        if node.is_leaf():
            left_substring = node.substring[:ind]
            right_substring = node.substring[ind:]
            left_node = Node(substring=left_substring) if left_substring else None
            right_node = Node(substring=right_substring) if right_substring else None
            return left_node, right_node

        if ind < node.weight:
            left_part, right_part = self.split(node.left, ind)
            new_right = self.__concat(right_part, node.right)
            return left_part, new_right
        else:
            left_part, right_part = self.split(node.right, ind - node.weight)
            new_left = self.__concat(node.left, left_part)
            return new_left, right_part


    def concat(self, other):            # O(log n)
        return self.__concat(self.root, other.root)


    def insert(self, node, inserting_string, ind_st):    # O(log n + m log m), m = len(inserting_string)
        if inserting_string == "":
            return node
        if node is None:
            return self.__build_from_string(inserting_string)

        if ind_st < 0 or ind_st > self.__get_length(node):   # O(log n)
            raise IndexError(f"Insert index {ind_st} out of range")

        left, right = self.split(node, ind_st)  # O(log n)
        inserting = self.__build_from_string(inserting_string)  # O(m log m)

        return self.__concat(self.__concat(left, inserting), right)  # O(log n)


    def delete(self, node, ind_st, length):    # O(log n)
        if node is None:
            if ind_st == 0 and length == 0:
                return None
            raise IndexError("Cannot delete from empty rope")

        if ind_st < 0 or length < 0 or ind_st + length > self.__get_length(node):
            raise IndexError(f"Delete range [{ind_st}, {ind_st+length}) out of range")

        left, right = self.split(node, ind_st)  # O(log n)
        deleted, new_right = self.split(right, length)  # O(log n)
        return self.__concat(left, new_right)  # O(log n)


    # for output

    def to_string(self, node=None):     # O(n) - full nodes traversal
        if node is None:
            node = self.root
        if node is None:
            return ""

        if node.is_leaf():
            return node.substring

        return self.to_string(node.left) + self.to_string(node.right)


    def __get_rope_info(self, leaves_list, nodes_list, node=None):    # O(n) - full nodes traversal
        if node is None:
            node = self.root
        if node is None:
            return

        if node.is_leaf():
            if node.substring:
                leaves_list += [node.substring]
        else:
            nodes_list += [node.weight]
            self.__get_rope_info(leaves_list, nodes_list, node.left)
            self.__get_rope_info(leaves_list, nodes_list, node.right)


    def print_debug_output(self):      # O(n) - because of to_string and __get_rope_info
        leaves_list = []
        nodes_list = []
        self.__get_rope_info(leaves_list, nodes_list)

        for i in range(len(leaves_list)):
            print(f"Leaf {i + 1}: {leaves_list[i]}")

        for i in range(len(nodes_list)):
            print(f"Node {i + 1}: {nodes_list[i]}")

        print(self.to_string())



if __name__ == "__main__":
    string = input()
    insert_data = input().split(" ", 1)
    delete_data = input().split(" ", 1)

    rope = Rope(string=string)
    rope.print_debug_output()

    rope.root = rope.insert(rope.root, insert_data[1], int(insert_data[0]))
    rope.print_debug_output()

    rope.root = rope.delete(rope.root, int(delete_data[0]), int(delete_data[1]))
    rope.print_debug_output()