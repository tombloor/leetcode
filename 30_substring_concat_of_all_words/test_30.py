from solution_30 import Solution

def test_example1():
    s = "barfoothefoobarman"
    words = ["foo","bar"]

    solver = Solution()

    assert solver.findSubstring(s, words) == [0, 9]

def test_example2():
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]

    solver = Solution()

    assert solver.findSubstring(s, words) == []

def test_example3():
    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]

    solver = Solution()

    assert solver.findSubstring(s, words) == [6, 9, 12]

def test_example4():
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]

    solver = Solution()

    assert solver.findSubstring(s, words) == [8]