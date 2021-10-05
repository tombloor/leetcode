from solution import Solution

def test_length_1_rotate_0():
    nums = [1]
    k = 1

    solver = Solution()
    solver.rotate(nums, k)

    assert nums == [1]

def test_length_1_rotate_1():
    nums = [1]
    k = 1

    solver = Solution()
    solver.rotate(nums, k)

    assert nums == [1]

def test_length_7_rotate_0():
    nums = [1,2,3,4,5,6,7]
    k = 0

    solver = Solution()
    solver.rotate(nums, k)

    assert nums == [1,2,3,4,5,6,7]

def test_length_7_rotate_1():
    nums = [1,2,3,4,5,6,7]
    k = 1

    solver = Solution()
    solver.rotate(nums, k)

    assert nums == [7,1,2,3,4,5,6]

def test_length_7_rotate_2():
    nums = [1,2,3,4,5,6,7]
    k = 2

    solver = Solution()
    solver.rotate(nums, k)

    assert nums == [6,7,1,2,3,4,5]

def test_length_7_rotate_3():
    nums = [1,2,3,4,5,6,7]
    k = 3

    solver = Solution()
    solver.rotate(nums, k)

    assert nums == [5,6,7,1,2,3,4]

def test_length_3000_rotate_lots():
    nums = [1,2,3] * 1000
    k = 1000000

    solver = Solution()
    solver.rotate(nums, k)

    assert nums == [3,1,2] * 1000