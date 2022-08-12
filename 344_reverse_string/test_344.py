from solution_344 import Solution

def test_hello():
    i = ['h', 'e', 'l', 'l', 'o']
    solver = Solution()

    solver.reverseString(i)

    assert i == ['o', 'l', 'l', 'e', 'h']

def test_length_1():
    i = ['a']
    solver = Solution()

    solver.reverseString(i)

    assert i == ['a']

def test_long_string():
    i = ['a', 'b', 'c'] * 30000
    solver = Solution()

    solver.reverseString(i)

    assert i == ['c', 'b', 'a'] * 30000
