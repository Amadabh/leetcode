class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dp = [[-1 for i in range(n)] for j in range(m)]

        def rec(i, j):
            if i==m-1 and j ==n-1:
                return grid[i][j]

            if i >= m or j >= n:
                return float("inf")
            
            if dp[i][j] != -1:
                return dp[i][j]

            right, down = rec(i, j+1), rec(i + 1 , j)
            ans = grid[i][j]  + min(right, down)
            dp[i][j] = ans
            return ans
        
        return rec(0, 0)


        