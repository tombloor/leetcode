from solution_804 import Solution

def test_example1():
    words = ["gin","zen","gig","msg"]

    solver = Solution()

    assert solver.uniqueMorseRepresentations(words) == 2    

def test_example2():
    words = ["a"]

    solver = Solution()

    assert solver.uniqueMorseRepresentations(words) == 1 
