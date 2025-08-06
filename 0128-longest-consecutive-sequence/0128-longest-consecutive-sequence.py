class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        d = defaultdict(int)
        maxCount = 0
        for i in s:
            if i-1 not in s:
                l=0
                while i+l in s:
                    l+=1
                maxCount = max(l,maxCount)
        return maxCount

            

        return maxCount


        
       