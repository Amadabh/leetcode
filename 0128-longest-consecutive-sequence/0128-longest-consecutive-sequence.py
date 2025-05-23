class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        nums = list(set(nums))
        heap = nums.copy()
        heapq.heapify(heap)

        maxSeq = 1
        prev = nums[0]
        cnt=1
        while heap:
            ele = heapq.heappop(heap)
            # print(ele,cnt)?
            if ele==prev+1:
                cnt+=1
            else:
                maxSeq = max(cnt,maxSeq)
                cnt = 1
            prev = ele
        maxSeq = max(cnt,maxSeq)

        return maxSeq

        