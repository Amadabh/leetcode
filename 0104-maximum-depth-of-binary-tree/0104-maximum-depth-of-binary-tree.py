# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        #bfs
        if not root:
            return 0 
        q = [(root,1)]
        maxlvl =1
        while q:
            node, lvl = q.pop()
            maxlvl = max(lvl,maxlvl)
            if node.left:
                q.append((node.left,lvl+1))
            if node.right:
                q.append((node.right,lvl+1))
        return maxlvl

        # def dfs(root):
        #     if not root:
        #         return 0
        #     return 1 + max(dfs(root.left),dfs(root.right))
        # return dfs(root)
        