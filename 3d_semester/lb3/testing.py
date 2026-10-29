from main import Node, Rope
import pytest


class TestRope:

    # __init__ testing
    def test_empty_rope(self):
        rope = Rope(string="")
        assert rope.to_string() == ""
        assert rope.root is None

    def test_single_char_rope(self):
        rope = Rope(string="a")
        assert rope.to_string() == "a"
        assert rope.root.is_leaf()
        assert rope.root.substring == "a"

    def test_short_string_rope(self):
        rope = Rope(string="hello")
        assert rope.to_string() == "hello"

    def test_long_string_rope(self):
        long_string = "a" * 20
        rope = Rope(string=long_string)
        assert rope.to_string() == long_string

    # index testing
    def test_index_basic(self):
        rope = Rope(string="hello world")
        assert rope.index(0) == 'h'
        assert rope.index(4) == 'o'
        assert rope.index(6) == 'w'
        assert rope.index(10) == 'd'

    def test_index_edge_cases(self):
        rope = Rope(string="abc")
        assert rope.index(0) == 'a'
        assert rope.index(2) == 'c'

    def test_index_errors(self):
        rope = Rope(string="abc")

        with pytest.raises(IndexError):
            rope.index(-1)
        with pytest.raises(IndexError):
            rope.index(3)

        empty_rope = Rope(string="")
        with pytest.raises(IndexError):
            empty_rope.index(0)

    # split testing
    def test_split_empty(self):
        rope = Rope(string="")
        left, right = rope.split(rope.root, 0)
        assert left is None
        assert right is None

    def test_split_beginning(self):
        rope = Rope(string="hello world")
        left, right = rope.split(rope.root, 0)

        left_rope = Rope()
        left_rope.root = left
        right_rope = Rope()
        right_rope.root = right

        assert left_rope.to_string() == ""
        assert right_rope.to_string() == "hello world"

    def test_split_end(self):
        rope = Rope(string="hello world")
        left, right = rope.split(rope.root, 11)

        left_rope = Rope()
        left_rope.root = left
        right_rope = Rope()
        right_rope.root = right

        assert left_rope.to_string() == "hello world"
        assert right_rope.to_string() == ""

    def test_split_middle(self):
        rope = Rope(string="hello world")
        left, right = rope.split(rope.root, 5)

        left_rope = Rope()
        left_rope.root = left
        right_rope = Rope()
        right_rope.root = right

        assert left_rope.to_string() == "hello"
        assert right_rope.to_string() == " world"

    def test_split_leaf_node(self):
        rope = Rope(string="short")
        left, right = rope.split(rope.root, 2)

        left_rope = Rope()
        left_rope.root = left
        right_rope = Rope()
        right_rope.root = right

        assert left_rope.to_string() == "sh"
        assert right_rope.to_string() == "ort"

    def test_split_errors(self):
        rope = Rope(string="abc")

        with pytest.raises(IndexError):
            rope.split(rope.root, -1)
        with pytest.raises(IndexError):
            rope.split(rope.root, 4)

    # concat testing
    def test_concat_basic(self):
        rope1 = Rope(string="hello")
        rope2 = Rope(string=" world")

        result_root = rope1.concat(rope2)
        result_rope = Rope()
        result_rope.root = result_root

        assert result_rope.to_string() == "hello world"

    def test_concat_with_empty(self):
        rope1 = Rope(string="hello")
        rope2 = Rope(string="")

        # rope1 + empty
        result1 = rope1.concat(rope2)
        result_rope1 = Rope()
        result_rope1.root = result1
        assert result_rope1.to_string() == "hello"

        # empty + rope1
        result2 = rope2.concat(rope1)
        result_rope2 = Rope()
        result_rope2.root = result2
        assert result_rope2.to_string() == "hello"

    # insert testing
    def test_insert_beginning(self):
        rope = Rope(string="world")
        rope.root = rope.insert(rope.root, "hello ", 0)
        assert rope.to_string() == "hello world"

    def test_insert_end(self):
        rope = Rope(string="hello")
        rope.root = rope.insert(rope.root, " world", 5)
        assert rope.to_string() == "hello world"

    def test_insert_middle(self):
        rope = Rope(string="heo")
        rope.root = rope.insert(rope.root, "ll", 2)
        assert rope.to_string() == "hello"

    def test_insert_empty_string(self):
        rope = Rope(string="hello world")
        original = rope.to_string()
        rope.root = rope.insert(rope.root, "", 5)
        assert rope.to_string() == original

    def test_insert_into_empty(self):
        rope = Rope(string="")
        rope.root = rope.insert(rope.root, "hello", 0)
        assert rope.to_string() == "hello"

    def test_insert_errors(self):
        rope = Rope(string="abc")

        with pytest.raises(IndexError):
            rope.insert(rope.root, "test", -1)
        with pytest.raises(IndexError):
            rope.insert(rope.root, "test", 4)

    # delete testing
    def test_delete_beginning(self):
        rope = Rope(string="hello world")
        rope.root = rope.delete(rope.root, 0, 6)
        assert rope.to_string() == "world"

    def test_delete_end(self):
        rope = Rope(string="hello world")
        rope.root = rope.delete(rope.root, 5, 6)
        assert rope.to_string() == "hello"

    def test_delete_middle(self):
        rope = Rope(string="hello world")
        rope.root = rope.delete(rope.root, 5, 1)
        assert rope.to_string() == "helloworld"

    def test_delete_empty_substring(self):
        rope = Rope(string="hello world")
        original = rope.to_string()
        rope.root = rope.delete(rope.root, 3, 0)
        assert rope.to_string() == original

    def test_delete_entire_string(self):
        rope = Rope(string="hello")
        rope.root = rope.delete(rope.root, 0, 5)
        assert rope.to_string() == ""

    def test_delete_errors(self):
        rope = Rope(string="abc")

        with pytest.raises(IndexError):
            rope.delete(rope.root, -1, 1)

        with pytest.raises(IndexError):
            rope.delete(rope.root, 0, -1)

        with pytest.raises(IndexError):
            rope.delete(rope.root, 2, 2)

        empty_rope = Rope(string="")
        with pytest.raises(IndexError):
            empty_rope.delete(empty_rope.root, 0, 1)



    # general tests
    def test_tree_structure(self):
        rope = Rope(MAX_LEAF=3, string="abcdefghij")

        assert rope.to_string() == "abcdefghij"

        for i, char in enumerate("abcdefghij"):
            assert rope.index(i) == char


    def test_combined_operations(self):
        rope = Rope(string="initial")

        rope.root = rope.insert(rope.root, " text", 7)
        assert rope.to_string() == "initial text"

        rope.root = rope.delete(rope.root, 0, 8)
        assert rope.to_string() == "text"

        rope.root = rope.insert(rope.root, "new ", 0)
        assert rope.to_string() == "new text"

        left, right = rope.split(rope.root, 3)

        left_rope = Rope()
        left_rope.root = left
        right_rope = Rope()
        right_rope.root = right

        assert left_rope.to_string() == "new"
        assert right_rope.to_string() == " text"

        result_root = right_rope.concat(left_rope)
        result_rope = Rope()
        result_rope.root = result_root
        assert result_rope.to_string() == " textnew"


    def test_large_operations(self):
        base_string = "a" * 100 + "b" * 100 + "c" * 100
        rope = Rope(string=base_string)

        assert rope.to_string() == base_string

        insert_pos = 150
        rope.root = rope.insert(rope.root, "INSERT", insert_pos)
        result = rope.to_string()
        assert result[insert_pos:insert_pos + 6] == "INSERT"

        delete_pos = 50
        delete_len = 50
        rope.root = rope.delete(rope.root, delete_pos, delete_len)
        result = rope.to_string()
        expected_len = len(base_string) + 6 - delete_len
        assert len(result) == expected_len



    def test_example(self):
        rope = Rope(string="This is a text")
        assert rope.to_string() == "This is a text"

        rope.root = rope.insert(rope.root, "_not", 7)
        assert rope.to_string() == "This is_not a text"

        rope.root = rope.delete(rope.root, 14, 3)
        assert rope.to_string() == "This is_not a t"


class TestNode:

    def test_leaf_node(self):
        node = Node(substring="hello")
        assert node.is_leaf() == True
        assert node.substring == "hello"
        assert node.weight == 5
        assert node.height == 1
        assert node.left is None
        assert node.right is None

    def test_internal_node(self):
        left = Node(substring="hello")
        right = Node(substring=" world")
        node = Node(left=left, right=right)

        assert node.is_leaf() == False
        assert node.substring is None
        assert node.weight == 5
        assert node.height == 2
        assert node.length == 11
        assert node.left == left
        assert node.right == right


if __name__ == "__main__":
    pytest.main(["testing.py", "-v"])

# or bash:  pytest -v testing.py