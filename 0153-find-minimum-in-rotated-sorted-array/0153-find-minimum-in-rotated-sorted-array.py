class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Brute force sort the array and take nums[0]
        #O(N) solution have two pointers for l,r = 0,1 if nums[r]< nums[l] return nums[r] else return nums[0]   
        # n = len(nums)
        # if n==1:
        #     return nums[0]
        # l,r = 0,1
        # while r<n:
        #     if nums[l]>nums[r]:
        #         return nums[r]
        #     l+=1
        #     r+=1
        # return nums[0]

        # If nums[mid]>nums[r] check rightside arr excluding the mid itself l = mid+1 other wise check leftside along with mid just in case mid is the smallest
        n = len(nums)
        l,r =0,n-1

        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l= mid+1
            else:
                r= mid

        print(nums[l])
        return nums[l]





        