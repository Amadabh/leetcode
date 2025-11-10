class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def search(arr, x):
            l, h = 0, len(arr)

            while l<h:
                mid = (l + h) // 2
                if nums[mid] < x:
                    l = mid + 1
                else:
                    h = mid
            
            return l
        
        lo = search(nums, target)
        hi = search(nums, target + 1) - 1

        if lo>= len(nums) or nums[lo] != target:
            return [-1, -1]

        return [lo, hi]
        