class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1+nums2
        num.sort()
        n = len(num)
        mid = n//2
        # print(mid)
        if n%2==0:
            return (num[mid-1] + num[mid] )/2
        else:
            return num[mid]

        