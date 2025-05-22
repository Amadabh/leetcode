class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(val,ind) for ind,val in enumerate(nums)]
        arr.sort()
        n = len(nums)
        l,r = 0,n-1
        print(arr)
        while l<r:
            if arr[l][0]+arr[r][0]==target:
                return [arr[l][1],arr[r][1]]
            
            elif arr[l][0]+arr[r][0]>target:
                r-=1
            else:
                l+=1
        