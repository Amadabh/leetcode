class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = {}
        def rec(ind):
            if ind<0:
                return 0
            if ind in cache:
                return cache[ind]
            maxi = 0
            for j in range(2, ind + 1):
                maxi = max(maxi,  rec(ind - j))
            cache[ind] = nums[ind] + maxi
            return cache[ind]
        
        return max(rec(n-1), rec(n-2))

