class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Recursion
        # if prices == sorted(prices, reverse=True):
        #     return 0
        # n = len(prices)
        # dp = [[float("inf") for j in range(2)] for i in range(n)]
        
        # def rec(buy, ind):
        #     if ind == n:
        #         return 0
        #     take = 0
        #     notTake = rec(buy, ind + 1)
        #     if dp[ind][buy]!= float("inf"):
        #         return dp[ind][buy]

        #     if buy:
        #         take = rec(False, ind + 1) - prices[ind]
        #     else:
        #         take = rec(True, ind + 1) + prices[ind]
            
        #     dp[ind][buy] = max(take, notTake)
        #     return dp[ind][buy]
        # return rec(True, 0)

        # Tabulation
        profit = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit