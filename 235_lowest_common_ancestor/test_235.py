from solution_235 import Solution, TreeNode

def build_tree(arr):
    root = TreeNode(arr[0])
    stack = [root]
    i = 1
    while len(stack) > 0:
        curr = stack.pop(0)

        if curr.val is not None:
            if len(arr) > i:
                curr.left = TreeNode(arr[i])
                stack.append(curr.left)
                i += 1
            if len(arr) > i:
                curr.right = TreeNode(arr[i])
                stack.append(curr.right)
                i += 1

    return root
        

def test_example_1():
    test = build_tree([6,2,8,0,4,7,9,None,None,3,5])

    solver = Solution()

    assert solver.lowestCommonAncestor(test, TreeNode(2), TreeNode(8)).val == 6


def test_example_2():
    test = build_tree([6,2,8,0,4,7,9,None,None,3,5])

    solver = Solution()

    assert solver.lowestCommonAncestor(test, TreeNode(2), TreeNode(4)).val == 2