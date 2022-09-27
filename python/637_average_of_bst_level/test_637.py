from solution_637 import Solution, TreeNode

def buildTree(arr):
    if len(arr) == 0:
        return null

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
    arr = [3,9,20,None,None,15,7]

    solver = Solution()

    assert solver.averageOfLevels(buildTree(arr)) == [3, 14.5, 11]

def test_example2():
    arr = [3,9,20,15,7]
    solver = Solution()
    assert solver.averageOfLevels(buildTree(arr)) == [3,14.5,11]