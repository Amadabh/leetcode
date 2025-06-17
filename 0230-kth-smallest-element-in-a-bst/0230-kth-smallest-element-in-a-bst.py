# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Brute force traverse the entire tree store it in an array sort it get kth index or use heap to get kth val
        arr = []
        heapq.heapify(arr)
        def dfs(root):
            if not root:
                return
            heapq.heappush(arr,root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        ans =0
        for i in range(k):
            ans = heapq.heappop(arr)
        return ans
        # Array
        # arr = []
        # def dfs(root):
        #     if not root:
        #         return
        #     arr.append(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # arr.sort()
        # return arr[k-1]
        