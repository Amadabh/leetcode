# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inod ={}
        for ind,ele in enumerate(inorder):
            inod[ele]=ind
            ind+=1
        print(inod)
        n = len(preorder)
        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None
            ele = preorder[0]
            root = TreeNode(ele)

            ind = inorder.index(ele)
            # print(preorder,inorder,ind)
            root.left = dfs(preorder[1:ind+1], inorder[:ind])
            root.right = dfs(preorder[ind+1:], inorder[ind+1:])
            return root
           
        return dfs(preorder,inorder)