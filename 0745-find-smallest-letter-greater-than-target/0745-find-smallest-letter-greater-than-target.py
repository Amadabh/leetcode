class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        n = len(letters)
        nums = letters
        l, r = 0, n - 1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:

                while mid+1 < n and nums[mid+1] ==target:
                    mid+=1
                if mid == n-1:
                    return nums[0]
                print(mid)
                return nums[mid+1]
            elif nums[mid]<target:
                l = mid + 1
            else:
                r = mid - 1
        print(l)
        if l>n-1:
            return letters[0]
        return letters[l]
        