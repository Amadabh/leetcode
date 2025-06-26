class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-1 *i for i in nums]
        heapq.heapify(heap)
        ans = 0 
        while k>0:
            ans = heapq.heappop(heap)
            k-=1
        return -1*ans
        

        