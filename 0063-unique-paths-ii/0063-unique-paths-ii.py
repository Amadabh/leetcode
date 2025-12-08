class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:


        m, n = len(obstacleGrid), len(obstacleGrid[0])
        grid = [ [ obstacleGrid[i][j] for j in range(n)] for i in range(m)]

        dp = [[-1 for j in range(n)] for i in range(m)]

        # print(grid, vis)
        dr = [(0, 1), (1, 0)]

        if grid[0][0] == 1:
            return 0

        def dfs(row, col):

            
            if grid[row][col]:
                return 0

            if row == m - 1 and col == n - 1:
                return 1

            if dp[row][col]!=-1:
                return dp[row][col]
            s = 0
            
            for r, c in dr:
                r1, c1 = row + r, col + c
                if r1 < m and c1 < n and not grid[r1][c1]:
                     
                    s += dfs(r1, c1)
            dp[row][col] = s
            return s
        return dfs(0, 0)