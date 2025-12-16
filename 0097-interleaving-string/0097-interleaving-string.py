class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        cache = {}
        def rec(i, j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i == m and j == n:
                return True
            flag = False
            if i < m and s1[i] == s3[i+j]:
                flag = flag or rec(i + 1, j)
            if j < n and s2[j] == s3[i + j]:
                flag = flag or rec(i, j + 1) 
            cache[(i,j)] = flag
            return flag

        return rec(0,0)    
        