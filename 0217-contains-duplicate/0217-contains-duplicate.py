class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                return True
        return False
        #Dictionary Solution
        # d= defaultdict(int)
        # n = len(nums)
        # for i in nums:
        #     d[i]+=1
        #     if d[i]>=2:
        #         return True
        # return False
        