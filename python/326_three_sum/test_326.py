from solution_326 import Solution

def test_example1():
    solver = Solution()
    assert solver.isPowerOfThree(27) == True

def test_example2():
    solver = Solution()
    assert solver.isPowerOfThree(0) == False

def test_example3():
    solver = Solution()
    assert solver.isPowerOfThree(9) == True

def test_negative():
    solver = Solution()
    assert solver.isPowerOfThree(-3) == False

def test_zero():
    solver = Solution()
    assert solver.isPowerOfThree(0) == False

def test_failed():
    solver = Solution()
    assert solver.isPowerOfThree(243) == True