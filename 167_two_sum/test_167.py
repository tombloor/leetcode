from solution import Solution

def test_example_1():
    nums = [2,7,11,15]
    target = 9

    solver = Solution()
    result = solver.twoSum(nums, target)

    assert result == [1,2]

def test_example_2():
    nums = [2,3,4]
    target = 6

    solver = Solution()
    result = solver.twoSum(nums, target)

    assert result == [1,3]

def test_example_3():
    nums = [-1,0]
    target = -1

    solver = Solution()
    result = solver.twoSum(nums, target)

    assert result == [1,2]

def test_example_2_nums():
    nums = [1, 2]
    target = 3

    solver = Solution()
    result = solver.twoSum(nums, target)

    assert result == [1,2]

def test_long_arr():
    nums = [1, 2] * 10000
    nums = nums + [7, 3]
    target = 10

    solver = Solution()
    result = solver.twoSum(nums, target)

    assert result == [len(nums) - 1, len(nums)]
