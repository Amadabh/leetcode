class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        cache = {}
        m, n = len(matrix), len(matrix[0])
        def rec(r, c):
            if r >= m or c >= n:
                return 0
            if (r, c) not in cache:
                down = rec(r + 1, c)
                right = rec(r, c + 1)
                diag = rec(r + 1, c + 1)
                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r,c)] = 1 + min(down, right, diag)
            
            return cache[(r,c)]
        
        rec(0, 0)
        return max(cache.values()) ** 2

                


        