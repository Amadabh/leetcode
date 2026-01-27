class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        n = len(s)
        rev = s[::-1]
        if s== rev:
            return True
        def isPalin(st : str, rst: str) -> str:
            return st == rst
        
        for i in range(n):
            if isPalin(s[:i] + s[i+1:], rev[:n - i - 1] + rev[n-i:]):
                return True
            # print(s[:i] + s[i+1:], rev[:n - i - 1] + rev[n-i:])
        return False

    