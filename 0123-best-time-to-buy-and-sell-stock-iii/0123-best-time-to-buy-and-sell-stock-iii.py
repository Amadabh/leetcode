class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # dp = [[[float("inf") for x in range(2)]for j in range(2)] for i in range(n)]
       
        #3d
        # def rec(buy, ind, cnt):
        #     if cnt == 2 or ind == n:
        #         return 0
        #     ans = 0 
        #     if dp[ind][buy][cnt]!= float("inf"):
        #         return dp[ind][buy][cnt]

        #     nothing = rec(buy, ind + 1, cnt)
        #     if buy:
        #         ans = rec(False, ind + 1, cnt) - prices[ind]
        #     else:
        #         ans = rec(True, ind + 1, cnt + 1) + prices[ind]
            
        #     ans = max(ans, nothing)
        #     dp[ind][buy][cnt] = ans
        #     return ans
        # return rec(True, 0, 0)
        # n = len(prices)
       
        dp = [[ None for j in range(4)] for i in range(n)]
       
        def rec(ind, state):
            if state == 4 or ind == n:
                return 0
            ans = 0 
            # print(ind, state)
            if dp[ind][state] is not None:
                return dp[ind][state]

            nothing = rec(ind + 1, state)
            if state % 2 == 0:
                ans = rec(ind + 1, state + 1) - prices[ind]
            else:
                ans = rec(ind + 1, state + 1) + prices[ind]
            
            ans = max(ans, nothing)
            dp[ind][state] = ans
            return ans
        return rec(0, 0)