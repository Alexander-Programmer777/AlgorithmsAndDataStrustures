# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.height = 1
#
#
# # static functions, not methods, cuz they don't use self things
# def get_height(node):
#     if not node:
#         return 0
#     return node.height
#
#
# def min_value_node(root):
#     current = root
#     while current.left:
#         current = current.left
#     return current
#
#
# # rotations, both O(1)
# def right_rotate(node):
#     A = node.left
#     Y = A.right
#
#     A.right = node
#     node.left = Y
#
#     node.height = 1 + max(get_height(node.left), get_height(node.right))
#     A.height = 1 + max(get_height(A.left), get_height(A.right))
#
#     return A
#
#
# def left_rotate(node):
#     B = node.right
#     Y = B.left
#
#     B.left = node
#     node.right = Y
#
#     node.height = 1 + max(get_height(node.left), get_height(node.right))
#     B.height = 1 + max(get_height(B.left), get_height(B.right))
#
#     return B
#
#
# def get_balance(node):
#     if not node:
#         return 0
#     return get_height(node.left) - get_height(node.right)
#
#
# class AVLTree:
#     def __init__(self):
#         self.root = None
#
#     # O(log n)
#     def search(self, root, value):
#         if not root or root.value == value:
#             return root
#         if root.value < value:
#             return self.search(root.right, value)
#         return self.search(root.left, value)
#
#
#
#     # O(log n)
#     def insert(self, root, value):
#         if not root:
#             return Node(value)
#         elif value < root.value:
#             root.left = self.insert(root.left, value)
#         else:
#             root.right = self.insert(root.right, value)
#
#         # BALANCING    (recursion!!! from new node to main root)
#
#         root.height = 1 + max(get_height(root.left), get_height(root.right))
#         balance = get_balance(root)
#
#         # Right rotation
#         if balance > 1 and value < root.left.value:
#             return right_rotate(root)
#
#         # Left rotation
#         if balance < -1 and value > root.right.value:
#             return left_rotate(root)
#
#         # Left-Right rotation
#         if balance > 1 and value > root.left.value:
#             root.left = left_rotate(root.left)
#             return right_rotate(root)
#
#         # Right-Left rotation
#         if balance < -1 and value < root.right.value:
#             root.right = right_rotate(root.right)
#             return left_rotate(root)
#
#         return root
#
#
#
#     # O(log n)
#     def delete(self, root, value):
#         if not root:
#             return root
#
#         if value < root.value:
#             root.left = self.delete(root.left, value)
#         elif value > root.value:
#             root.right = self.delete(root.right, value)
#         else:
#             if not root.left:
#                 temp = root.right
#                 root = None
#                 return temp
#             elif not root.right:
#                 temp = root.left
#                 root = None
#                 return temp
#
#             temp = min_value_node(root.right)
#             root.value = temp.value
#             root.right = self.delete(root.right, temp.value)
#
#         if not root:
#             return root
#
#         # BALANCING
#
#         root.height = 1 + max(get_height(root.left), get_height(root.right))
#         balance = get_balance(root)
#
#         # Right rotation
#         if balance > 1 and balance(root.left) >= 0:
#             return right_rotate(root)
#
#         # Left rotation
#         if balance < -1 and balance(root.right) <= 0:
#             return left_rotate(root)
#
#         # Left-Right rotation
#         if balance > 1 and balance(root.left) < 0:
#             root.left = left_rotate(root.left)
#             return right_rotate(root)
#
#         # Right-Left rotation
#         if balance < -1 and balance(root.right) > 0:
#             root.right = right_rotate(root.right)
#             return left_rotate(root)
#
#         return root
#
#
#     def insert_value(self, value):
#         self.root = self.insert(self.root, value)
#
#     def delete_value(self, value):
#         self.root = self.delete(self.root, value)
#
#     def search_value(self, value):
#         return self.search(self.root, value)
#
#
#
#
#     # visualisation outputs
#     def do_BFS(self):
#         if self.root is None:
#             return
#         p = self.root
#         q = [p]
#         res = []
#         while q:
#             qn = []
#             for x in q:
#                 res.append(str(x.value))
#                 if x.left:
#                     qn.append(x.left)
#                 if x.right:
#                     qn.append(x.right)
#             q = qn
#         print(" ".join(res))
#
#
#
#     # DFS algorithms
#     def do_in_order_traversal(self, current: Node, res: list):    # result is an ascending sequent
#         if current is None:
#             return
#         self.do_in_order_traversal(current.left, res)
#         res += [str(current.value)]
#         self.do_in_order_traversal(current.right, res)
#
#
#     def do_pre_order_traversal(self, current: Node, res: list):
#         if current is None:
#             return
#         res += [str(current.value)]
#         self.do_pre_order_traversal(current.left, res)
#         self.do_pre_order_traversal(current.right, res)
#
#
#     def do_post_order_traversal(self, current: Node, res: list):
#         if current is None:
#             return
#         self.do_post_order_traversal(current.left, res)
#         self.do_post_order_traversal(current.right, res)
#         res += [str(current.value)]




class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None


    def height(self, node):
        if not node:
            return 0
        return node.height


    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)


    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Right rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Left rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


    def delete(self, root, value):
        if not root:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Right Rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root


    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y


    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y


    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current


    def search(self, root, value):
        if not root or root.value == value:
            return root
        if root.value < value:
            return self.search(root.right, value)
        return self.search(root.left, value)


    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def search_value(self, value):
        return self.search(self.root, value)


# Example usage:
if __name__ == "__main__":
    tree = AVLTree()
    tree.insert_value(10)
    tree.insert_value(20)
    tree.insert_value(30)
    tree.insert_value(40)
    tree.insert_value(50)

    print("Tree after insertion:")
    # In-order traversal to print the tree
    def inorder_traversal(root):
        if root:
            inorder_traversal(root.left)
            print(root.value),
            inorder_traversal(root.right)

    inorder_traversal(tree.root)
    print()

    tree.delete_value(20)
    print("Tree after deletion of 20:")
    inorder_traversal(tree.root)
    print()

    result = tree.search_value(30)
    if result:
        print("Node found")
    else:
        print("Node not found")
