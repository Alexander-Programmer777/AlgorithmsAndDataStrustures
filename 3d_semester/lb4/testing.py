from main import SegmentTree
import pytest


class TestSegmentTree:
    def test_initialization(self):
        st = SegmentTree(10)
        assert st.n == 10
        assert st.size == 16
        assert len(st.tree) == 2 * st.size

        for i in range(10):
            assert st.get_value(i) == 0


    def test_single_addition(self):
        st = SegmentTree(5)
        st.add_value(0, 3, 5)  # [0, 3) = [0, 2]

        assert st.get_value(0) == 5
        assert st.get_value(1) == 5
        assert st.get_value(2) == 5
        assert st.get_value(3) == 0
        assert st.get_value(4) == 0


    def test_multiple_additions(self):
        st = SegmentTree(5)

        st.add_value(0, 2, 3)
        st.add_value(1, 4, 2)
        st.add_value(0, 5, 1)

        assert st.get_value(0) == 3 + 1
        assert st.get_value(1) == 3 + 2 + 1
        assert st.get_value(2) == 2 + 1
        assert st.get_value(3) == 2 + 1
        assert st.get_value(4) == 1


    def test_intersecting_ranges(self):
        st = SegmentTree(10)

        st.add_value(0, 5, 10)
        st.add_value(3, 8, 5)
        st.add_value(2, 4, 3)

        assert st.get_value(0) == 10
        assert st.get_value(2) == 10 + 3
        assert st.get_value(3) == 10 + 5 + 3
        assert st.get_value(4) == 10 + 5
        assert st.get_value(5) == 5
        assert st.get_value(7) == 5


    def test_edge_cases(self):
        st = SegmentTree(1)
        st.add_value(0, 1, 100)
        assert st.get_value(0) == 100

        st = SegmentTree(2)
        st.add_value(0, 1, 5)
        st.add_value(1, 2, 10)
        assert st.get_value(0) == 5
        assert st.get_value(1) == 10


    def test_large_values(self):
        st = SegmentTree(100)
        st.add_value(0, 100, 10 ** 9)
        assert st.get_value(50) == 10 ** 9

        st.add_value(25, 75, 10 ** 9)
        assert st.get_value(50) == 2 * 10 ** 9


    def test_index_errors(self):
        st = SegmentTree(5)

        # negative indexes
        with pytest.raises(IndexError):
            st.add_value(-1, 3, 5)
        with pytest.raises(IndexError):
            st.add_value(0, -1, 5)
        with pytest.raises(IndexError):
            st.get_value(-1)

        # indexes out of range
        with pytest.raises(IndexError):
            st.add_value(0, 6, 5)
        with pytest.raises(IndexError):
            st.add_value(5, 6, 5)


    def test_empty_range(self):
        st = SegmentTree(5)
        st.add_value(2, 2, 100)
        for i in range(5):
            assert st.get_value(i) == 0


    def test_example(self):
        st = SegmentTree(5)
        st.add_value(0, 3, 3)
        assert st.get_value(1) == 3

        st.add_value(2, 4, 4)
        assert st.get_value(3) == 4
        assert st.get_value(4) == 0