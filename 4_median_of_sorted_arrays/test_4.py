from solution import Solution
import pytest

def test_ex_1():
    solver = Solution()
    n1 = [1, 3]
    n2 = [2]

    result = solver.findMedianSortedArrays(n1, n2)

    assert result == float(2)

def test_ex_2():
    solver = Solution()
    n1 = [1, 2]
    n2 = [3, 4]

    result = solver.findMedianSortedArrays(n1, n2)

    assert result == float(2.5)