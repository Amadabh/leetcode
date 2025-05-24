class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlen = 0
        for n in numset:
            if (n-1) not in numset:
                length=0
                while (n+length) in numset:
                    length+=1
                maxlen= max(length,maxlen)
        return maxlen
        # if not nums:
        #     return 0 
        # nums = list(set(nums))
        # heap = nums.copy()
        # heapq.heapify(heap)

        # maxSeq = 1
        # prev = nums[0]
        # cnt=1
        # while heap:
        #     ele = heapq.heappop(heap)
        #     # print(ele,cnt)?
        #     if ele==prev+1:
        #         cnt+=1
        #     else:
        #         maxSeq = max(cnt,maxSeq)
        #         cnt = 1
        #     prev = ele
        # maxSeq = max(cnt,maxSeq)

        # return maxSeq

        