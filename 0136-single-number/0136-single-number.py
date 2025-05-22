class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq =defaultdict(int)
        for i in nums:
            freq[i]+=1

        for key,val in freq.items():
            if val==1:
                return key
        
        