class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Brute force sort the array abd the search for the target by traversing throught the array
        # O(N) solution would be to directly traverse from beginning to the end then u get the target else return -1
        start= 0
        n = len(nums)
        l,r = 0, n-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l= mid+1
            else:
                r = mid
        start = l 
        hypLen = n + start

        l,r =start, hypLen-1
        while l<r:
            mid = (l+r)//2
            left,right = l%n, r%n
            trueMid = mid%n
            print(mid, trueMid, nums[trueMid])
            if nums[trueMid]==target:
                return trueMid
            elif nums[trueMid]<target:
                l = mid+1
            else:
                r= mid-1
        if nums[l%n]==target:
            return l%n
        return -1
            


