import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * i for i in nums]
        heapq.heapify(nums)
        ele = 0
        for i in range(k):
            ele = heapq.heappop(nums)
        
        return -1 * ele
        

        