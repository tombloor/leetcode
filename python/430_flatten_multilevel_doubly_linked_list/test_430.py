from solution_430 import Solution, Node

def result_to_arr(head):
    v = []
    n = head
    while n.next:
        v.append(n.val)
        n = n.next
    v.append(n.val)
    return v

def test_one_node():
    n = Node(1, None, None, None)

    solver = Solution()
    result = solver.flatten(n)

    assert result_to_arr(result) == [1]

def test_empty():
    solver = Solution()
    result = solver.flatten(None)

    assert result == None

def test_flat():
    head = Node(1, None, None, None)
    n = head
    for i in range(2, 5):
        n.next = Node(i, n, None, None)
        n = n.next
    
    solver = Solution()
    result = solver.flatten(head)

    assert result_to_arr(result) == [1, 2, 3, 4]

# This is a pain to test, my solution already passed using leetcode's tests and I don't
# feel the need to spend more time on this
