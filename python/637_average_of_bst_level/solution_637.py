

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        queue = [root]
        result = []

        while queue:
            count = len(queue)
            total = 0

            for i in range(count):
                node = queue.pop(0)
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(total / count)

        return result
        