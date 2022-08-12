class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder(self, root: TreeNode):
        arr = []
        
        if root:
            arr += self.inorder(root.left)
            arr += [root.val]
            arr += self.inorder(root.right)

        return arr
    
    def build(self, arr, low, high):
        if low > high:
            return None
        
        mid = low + (high - low) // 2
        head = TreeNode(arr[mid])
        
        head.left = self.build(arr, low, mid - 1)
        head.right = self.build(arr, mid + 1, high)
        
        return head
            
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Inorder traversal to get a sorted array       
        arr = self.inorder(root)
        
        # recursivly use binary search to build the left and right subtree of each node
        root = self.build(arr, 0, len(arr) - 1)
        return root
