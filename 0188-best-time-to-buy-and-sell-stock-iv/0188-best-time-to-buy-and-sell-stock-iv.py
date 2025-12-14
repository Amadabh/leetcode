class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        n = len(prices)
        dp = [[-1 for j in range(2*k)] for i in range(n)]
        def rec(ind, state):
            if ind ==n:
                return 0
            if state == 2*k:
                return 0

            if dp[ind][state] != -1:
                return dp[ind][state]
            
            nottake = rec(ind + 1, state)
            ans = 0
            if state % 2 == 0:
                #buy
                ans = rec(ind +1, state + 1) - prices[ind]
            else:
                ans = rec(ind +1, state + 1) + prices[ind]
            
            dp[ind][state] = max(ans, nottake)
            return dp[ind][state]
        return rec(0, 0)
        