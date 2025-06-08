# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balance(root):
            if not root:
                return 0
            left = balance(root.left)
            right = balance(root.right)

            if left==-1 or right==-1:
                return -1

            res = abs(left - right)
            if res<2:
                return 1+max(left,right)
            else:
                return -1
        return balance(root)!=-1
           

            
        #Brute force check height of each node
        # def height(root):
        #     if not root:
        #         return 0
        #     l = height(root.left)
        #     r = height(root.right)
        #     return 1 + max(l,r)
        
        # def balance(root):
        #     if not root:
        #         return True
        #     left = balance(root.left)
        #     right = balance(root.right)
            
        #     l = height(root.left)
        #     r = height(root.right)
          
        #     res = abs(l-r)
        #     bl = False
        #     if res<=1:
        #         bl = True
        #     return bl and left and right
        # return balance(root)
            




            

            
        

        