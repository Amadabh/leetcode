class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # basic logic for this question is in first pass u multiply all the elements left of the element and in hte second pass u do reverse as u want to multipily the elements which are on the tright side of it
        ans = []
        pre=1
        for i in nums:
            ans.append(pre)
            pre*=i
        # print(pre,ans)
        post =1
        n = len(nums)
        for i in range(n-1,-1,-1):
            ans[i]*=post
            post*=nums[i]
        # print(ans)
        return ans