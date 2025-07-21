# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        
        def makeTree(l,r):
            if l>=r:
                return 
            mid = (l+r)//2
            # print(mid)
            root = TreeNode(nums[mid])
            root.left = makeTree(l,mid)
            root.right = makeTree(mid+1,r)
            return root
        root = makeTree(0, n)
        print(root)
        return root
        # return root





        