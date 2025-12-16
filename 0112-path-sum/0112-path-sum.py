# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def rec(root, s, parent):
            if not root:
                if not parent.left and not parent.right:
                    if s == targetSum:
                        return True
                return False
            
            return rec(root.left, s + root.val, root) or rec(root.right, s + root.val, root)
        
        return rec(root, 0, TreeNode())