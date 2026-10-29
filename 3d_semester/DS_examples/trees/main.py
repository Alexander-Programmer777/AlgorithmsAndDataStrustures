def do_Root_L_R(current):
    if current is None: return

    do_Root_L_R(current.left)
    do_Root_L_R(current.right)


class RootNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def solve(head):
    arr = []

    tmp = head
    while tmp:
        arr += [tmp.val]
        tmp = tmp.next

    mid_ind = (len(arr) - 1) // 2

    root = RootNode(arr.pop(mid_ind))





