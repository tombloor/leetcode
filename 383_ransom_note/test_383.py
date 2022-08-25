from solution_383 import Solution

def example_1():
    note = 'a'
    magazine = 'b'

    solver = Solution()

    assert solver.canConstruct(note, magazine) == False

def example_2():
    note = 'aa'
    magazine = 'ab'

    solver = Solution()

    assert solver.canConstruct(note, magazine) == False

def example_3():
    note = 'aa'
    magazine = 'aab'

    solver = Solution()

    assert solver.canConstruct(note, magazine) == True
