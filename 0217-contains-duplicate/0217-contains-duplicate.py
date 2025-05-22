class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d= defaultdict(int)
        n = len(nums)
        for i in nums:
            d[i]+=1
            if d[i]>=2:
                return True
        return False
        