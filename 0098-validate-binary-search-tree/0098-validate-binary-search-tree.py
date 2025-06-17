# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #BFS
        q = [(root,float("-inf"),float("inf"))]

        while q:
            node, mini,maxi =q.pop(0)

            if not mini<node.val<maxi:
                return False

            if node.left:
                q.append((node.left,mini,node.val))
            
            if node.right:
                q.append((node.right,node.val,maxi))
        return True

        # def dfs(root,mini,maxi):
        #     if not root:
        #         return True
            
        #     if not mini<root.val<maxi:
        #         return False

        #     l = dfs(root.left,mini,root.val)
        #     r = dfs(root.right,root.val,maxi)
        #     return l and r
        # return dfs(root,float("-inf"),float("inf")) 

        