class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        arr = triangle
        ans = [0]
        dp = [[None for i in range(len(arr[j]))] for j in range(m)]
        def rec(i, j) -> int:
            if i == m-1:
                return arr[i][j]
            if dp[i][j] is not None:
                return dp[i][j]
            p = rec(i + 1, j)
            p_next = rec(i + 1, j + 1)
            ans = arr[i][j] + min(p, p_next)
            dp[i][j] = ans
            return ans
        return rec(0, 0)






        