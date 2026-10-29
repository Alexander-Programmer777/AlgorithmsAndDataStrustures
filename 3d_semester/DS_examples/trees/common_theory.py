"""
ОПРЕДЕЛЕНИЯ

Дерево - это связный граф без циклов
Рекуррентное определение:
дерево - это корень и несколько деревьев, которые являются детьми этого корня.
Корневое дерево - дерево с отмеченной вершиной - корнем.

СПОСОБЫ ПРЕДСТАВЛЕНИЯ

1) массив родителей: index <-> parent of index
2) Связный список детей  ОСНОВНОЙ
3) Двусвязный список в обе стороны

ОБХОДЫ:
1) В ширину                               Breadth-first search
2) В глубину:                             Depth-first traversal
    2.1) Центрированный    L-Root-R       In-order traversal
    2.2) Прямой            Root-L-R       Pre-order traversal
    2.3) Обратный          L-R-Root       Post-order traversal
* + their implementation bellow

СЛОЖНОСТИ
худший случай для несбалансированного дерева это вырождение в связный список
так что сложность O(n). Чтобы такого не было используем сбалансированные деревья
например АВЛ, КЧ (полусбалансированное), Rope и др. С алгортимами балансировки
Опред: Дерево является сбалансированным т и т т, когда разница уровней для любых двух соседних поддеревьев (лев и прав) <= 1

У КЧД частичная балансировка: длины отличаются не более чем два раза
АВЛ лучше для поиска но значительно хуже для вставки и удаления за счет сложной балансировки
Поэтому выбирают КЧД, так как в совокупности они оказываются быстрее и тем не менее гарантируют логарифмическую сложность (просто с другими коэффициентами)
КЧД основа std::map from cpp -> O(log n) complexity и упорядоченность
но существует и std::unordered_map -> O(1) как словарь в питоне (оба являются ХТ)




"""




class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root: Node = None):
        self.root = root


    def search(self, current: Node, elem: int):  # returns node with finding value
        if current is None or elem == current.key:
            return current
        if elem < current.key:
            return self.search(current.left, elem)
        if elem > current.key:
            return self.search(current.right, elem)


    def append(self, elem: int) -> None:
        if self.root is None:
            self.root = Node(elem)
        else:
            self._append_recursive(self.root, elem)

    def _append_recursive(self, current: Node, elem: int):
        if elem < current.key:
            if current.left is None:
                current.left = Node(elem)
            else:
                self._append_recursive(current.left, elem)
        if elem > current.key:
            if current.right is None:
                current.right = Node(elem)
            else:
                self._append_recursive(current.right, elem)


    def delete(self, elem: int) -> None:
        self.root = self._delete_recursive(self.root, elem)

    def _delete_recursive(self, current: Node, elem: int):
        if current is None:
            return None

        if elem < current.key:
            current.left = self._delete_recursive(current.left, elem)
        elif elem > current.key:
            current.right = self._delete_recursive(current.right, elem)
        else:
            # there are 3 cases:
            # 1 + 2 cases: 0 or 1 descendant
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left

            # 3 case:
            min_node = self._find_min(current.right)
            current.key = min_node.key
            current.right = self._delete_recursive(current.right, min_node.key)

        return current

    @staticmethod
    def _find_min(node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current


    def do_BFS(self):

        if self.root is None:
            return
        p = self.root
        q = [p]
        res = []

        level = 0
        while q:
            qn = []
            print(f"level = {level}, vals = {[elem.key for elem in q]}")
            for x in q: # конкретный уровень q. проход по его элементам
                res.append(str(x.key))
                if x.left:
                    qn.append(x.left)
                if x.right:
                    qn.append(x.right)
            q = qn
            level += 1
        total_h = level
        print(f"total_h = {total_h}")
        print("total traversal = ",  " ".join(res))




    # DFS algorithms
    def do_in_order_traversal(self, current: Node, res: list):    # result is an ascending sequent
        if current is None:
            return
        self.do_in_order_traversal(current.left, res)
        res += [str(current.key)]
        self.do_in_order_traversal(current.right, res)


    def do_pre_order_traversal(self, current: Node, res: list):
        if current is None:
            return
        res += [str(current.key)]
        self.do_pre_order_traversal(current.left, res)
        self.do_pre_order_traversal(current.right, res)


    def do_post_order_traversal(self, current: Node, res: list):
        if current is None:
            return
        self.do_post_order_traversal(current.left, res)
        self.do_post_order_traversal(current.right, res)
        res += [str(current.key)]



if __name__ == "__main__":
    bs_tree = BinarySearchTree()
    bs_tree.append(5)
    bs_tree.append(3)
    bs_tree.append(7)
    bs_tree.append(1)
    bs_tree.append(4)
    bs_tree.append(6)
    bs_tree.append(8)

    bs_tree.do_BFS()






