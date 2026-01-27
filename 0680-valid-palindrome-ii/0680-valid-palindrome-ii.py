class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        n = len(s)
    
        def isPalin(st : str) -> str:
            return st == st[::-1]
        i, j = 0, n - 1

        while i < j:
            if s[i] != s[j]:
                return isPalin(s[:i] + s[i+1:]) or isPalin(s[:j] + s[j+1:])
            i+=1
            j-=1

        return True


            # def isPalin(st : str, rst: str) -> str:
            # return st == rst
        # for i in range(n):
        #     if isPalin(s[:i] + s[i+1:], rev[:n - i - 1] + rev[n-i:]):
        #         return True
        #     # print(s[:i] + s[i+1:], rev[:n - i - 1] + rev[n-i:])
        # return False

    