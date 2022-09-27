from solution_234 import Solution, ListNode

def create_list(arr):
    head = ListNode(arr[0])
    prev = head

    for i in range(1, len(arr)):
        prev.next = ListNode(arr[i])
        prev = prev.next

    return head

def test_example1():
    head = create_list([1,2,2,1])

    solver = Solution()

    assert solver.isPalindrome(head) == True

def test_example2():
    head = create_list([1,2])

    solver = Solution()

    assert solver.isPalindrome(head) == False

def test_single():
    head = create_list([1])

    solver = Solution()

    assert solver.isPalindrome(head) == True

def test_odd():
    head = create_list([1,2,3])

    solver = Solution()

    assert solver.isPalindrome(head) == False

def test_odd():
    head = create_list([1,2,3])

    solver = Solution()

    assert solver.isPalindrome(head) == False   

def test_odd2():
    head = create_list([1,2,5,2,1])

    solver = Solution()

    assert solver.isPalindrome(head) == True   