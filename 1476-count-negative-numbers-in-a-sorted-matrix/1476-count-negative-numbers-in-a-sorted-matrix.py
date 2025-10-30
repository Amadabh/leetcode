class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        ans = 0
        def rowCount(row):
            l, r = 0, n
            while l < r:
                mid = (l+r)//2
                if row[mid] < 0:
                    r = mid
                else:
                    l = mid + 1
               

            # print(l)
            return n - l
        

        for r in grid:
            ans += rowCount(r)
            print(ans)
        
        return ans

        