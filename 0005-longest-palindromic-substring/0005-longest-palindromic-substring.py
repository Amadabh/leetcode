# class Solution:
#     def longestPalindrome(self, s: str) -> str:
        # n = len(s)

        # res = ""
        # resLen = 0

        # for i in range(n):

        #     l, r = i, i

        #     while l >= 0 and r < n and s[l] == s[r]:
        #         if (r - l + 1) > resLen:
        #             resLen = r - l + 1
        #             res = s[l : r + 1]
        #         l-=1
        #         r+=1
            
        #     l, r = i, i+1
        #     while l >= 0 and r < n and s[l] == s[r]:
        #         if (r - l + 1) > resLen:
        #             resLen = r - l + 1
        #             res = s[l : r + 1]
        #         l-=1
        #         r+=1

        # return res



class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        max_str = s[0]
        maxLen = 1

        # length 1
        for i in range(n):
            dp[i][i] = True

        # length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                max_str = s[i:i+2]
                maxLen = 2

        # length >= 3
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > maxLen:
                        maxLen = length
                        max_str = s[i:j+1]

        return max_str



        
        
            

        


