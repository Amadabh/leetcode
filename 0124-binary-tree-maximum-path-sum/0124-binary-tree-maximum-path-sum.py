# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [float("-inf")]

        def dfs(root):
            if not root:
                return 0
            
            l = max(0,dfs(root.left))
            r = max(dfs(root.right),0)
            res[0] = max(res[0], max([l+r + root.val, root.val]))
            return max(l,r) + root.val
        res[0] = max(dfs(root), res[0])
        return res[0]
        