class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = []
      
        if x<0:
            return False

        while x>0:

            rem=x%10
            arr.append(rem)
            x=x//10
        # print(arr)
        return arr == arr[::-1]
        