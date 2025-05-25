class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l,r = 0,n-1
        nums = numbers
        while l<r:
            if nums[l] + nums[r] == target:
                return [l+1,r+1]
            elif nums[l] + nums[r] < target:
                l+=1
            else:
                r-=1
        

        # n = len(numbers)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if numbers[i]+numbers[j]==target:
        #             return [i+1,j+1]

        