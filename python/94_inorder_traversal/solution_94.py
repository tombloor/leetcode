

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        # Inorder traversal means we visit left child, then self, the right child        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
        