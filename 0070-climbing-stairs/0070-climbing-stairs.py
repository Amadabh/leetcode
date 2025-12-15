class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def rec(ind):
            if ind < 0:
                return 0
            if ind==0:
                return 1
            if ind in dp:
                return dp[ind]

            dp[ind] = rec(ind - 1) + rec(ind - 2)
            return dp[ind]
        return rec(n)

         
        