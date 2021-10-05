from solution import Solution

def test_length_3_3_zeroes():
    solver = Solution()
    nums = [0, 0, 0]

    solver.moveZeroes(nums)

    assert nums == [0, 0, 0]

def test_length_5_2_zeroes():
    solver = Solution()
    nums = [1, 0, 2, 0, 6]

    solver.moveZeroes(nums)

    assert nums == [1, 2, 6, 0, 0]

def test_length_1_0_zeroes():
    solver = Solution()
    nums = [1]

    solver.moveZeroes(nums)

    assert nums == [1]

def test_length_1_1_zeroes():
    solver = Solution()
    nums = [0]

    solver.moveZeroes(nums)

    assert nums == [0]

def test_long_arr_0_zeroes():
    solver = Solution()
    nums = [1, 3, 6, 3, 1, 3] * 10000

    solver.moveZeroes(nums)

    assert nums == [1, 3, 6, 3, 1, 3] * 10000

def test_length_3_2_leading_zeroes():
    solver = Solution()
    nums = [0,0,1]

    solver.moveZeroes(nums)

    assert nums == [1, 0, 0]
