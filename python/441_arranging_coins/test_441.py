from solution_441 import Solution

def test_min():
    solver = Solution()
    answer = solver.arrangeCoins(1)

    assert answer == 1

def test_5():
    solver = Solution()
    answer = solver.arrangeCoins(5)

    assert answer == 2

def test_8():
    solver = Solution()
    answer = solver.arrangeCoins(8)

    assert answer == 3

def test_max():
    solver = Solution()
    answer = solver.arrangeCoins(2147483647)

    assert answer == 65535
