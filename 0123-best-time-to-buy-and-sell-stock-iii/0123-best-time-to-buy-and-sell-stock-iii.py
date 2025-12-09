class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[float("inf") for x in range(2)]for j in range(2)] for i in range(n)]
        def rec(buy, ind, cnt):
            if cnt == 2 or ind == n:
                return 0
            ans = 0 
            if dp[ind][buy][cnt]!= float("inf"):
                return dp[ind][buy][cnt]

            nothing = rec(buy, ind + 1, cnt)
            if buy:
                ans = rec(False, ind + 1, cnt) - prices[ind]
            else:
                ans = rec(True, ind + 1, cnt + 1) + prices[ind]
            
            ans = max(ans, nothing)
            dp[ind][buy][cnt] = ans
            return ans
        return rec(True, 0, 0)