from solution_203 import Solution, ListNode

def list_to_arr(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

def test_empty():
    head = None
    t = 1

    solver = Solution()
    result = solver.removeElements(head, t)

    assert list_to_arr(result) == []

def test_1_item():
    head = ListNode(0)
    t = 1

    solver = Solution()
    result = solver.removeElements(head, t)

    assert list_to_arr(result) == [0]

def test_1_item_match():
    head = ListNode(1)
    t = 1

    solver = Solution()
    result = solver.removeElements(head, t)

    assert list_to_arr(result) == []

def test_all_matches():
    head = ListNode(5, ListNode(5, ListNode(5)))
    t = 5

    solver = Solution()
    result = solver.removeElements(head, t)

    assert list_to_arr(result) == []

def test_no_matches():
    head = ListNode(1, ListNode(2, ListNode(3)))
    t = 5

    solver = Solution()
    result = solver.removeElements(head, t)

    assert list_to_arr(result) == [1, 2, 3]
