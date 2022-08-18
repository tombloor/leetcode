from solution_1338 import Solution

def test_example1():
    arr = [3,3,3,3,5,5,5,2,2,7]

    solver = Solution()

    assert solver.minSetSize(arr) == 2

def test_example2():
    arr = [7,7,7,7,7,7]

    solver = Solution()

    assert solver.minSetSize(arr) == 1

def test_large_unique():
    items = 100000
    arr = range(0, items)

    solver = Solution()

    assert solver.minSetSize(arr) == items // 2
