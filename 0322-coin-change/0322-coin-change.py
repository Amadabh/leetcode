class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        cache = {}
        def rec(amt):
            if amt < 0:
                return float("inf")
            if amt==0:
                return 0
            if amt in cache:
                return cache[amt]
                
            cnt = float("inf")
            for i in coins:
                cnt = min(cnt , 1 + rec(amt - i) )
            cache[amt] = cnt
            return cnt
        
        ans = rec(amount)
        if ans == float("inf"):
            return -1
        return ans

        