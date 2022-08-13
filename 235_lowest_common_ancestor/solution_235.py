
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    # Find the lowest node that is greater than p and less than q
    def lowestCommonAncestor(self, root, p, q):
        # Cleanup args
        lower_bound = min(p.val, q.val)
        upper_bound = max(p.val, q.val)

        # Binary Search
        while root:
            if root.val < lower_bound:
                root = root.right
            elif root.val > upper_bound:
                root = root.left
            else:
                return root
        
        # No common ancestor
        return None