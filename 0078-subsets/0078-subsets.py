class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def rec(ind,arr):
            if ind==n:
                ans.append(arr)
                return
            notake = rec(ind+1,arr)
            take = rec(ind+1,arr+[nums[ind]])
        rec(0,[])
        return ans

            
        