from solution_94 import Solution, TreeNode

def buildTree(arr):
    if len(arr) == 0:
        return None

    root = TreeNode(arr[0])

    pending = [(root, 0)]

    while pending:
        node, index = pending.pop(0)
        left_index = (2 * index) + 1
        right_index = (2 * index) + 2

        if left_index < len(arr) and arr[left_index]:
            node.left = TreeNode(arr[left_index])
            index += 1
            pending.append((node.left, index))

        if right_index < len(arr) and arr[right_index]:
            node.right = TreeNode(arr[right_index])
            index += 1
            pending.append((node.right, index))

    return root

def test_example1():
    root = buildTree([1,None,2,3])
    solver = Solution()
    assert solver.inorderTraversal(root) == [1, 3, 2]

def test_example2():
    root = buildTree([])
    solver = Solution()
    assert solver.inorderTraversal(root) == []

def test_example3():
    root = buildTree([1])
    solver = Solution()
    assert solver.inorderTraversal(root) == [1]
