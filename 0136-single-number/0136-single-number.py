class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans =0
        for i in nums:
            ans^=i
        return ans
        # freq =defaultdict(int)
        # for i in nums:
        #     freq[i]+=1

        # for key,val in freq.items():
        #     if val==1:
        #         return key
        
        