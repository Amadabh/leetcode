class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res =[]
        n = len(intervals)
        intervals.sort()
        res.append([intervals[0][0],intervals[0][1]])
        for i in range(1,n):
            s1,e1 = res[-1]
            s2,e2 = intervals[i]
            if e1>=s2:
                res[-1][1] = max(e1,e2)
            else:
                res.append([s2,e2])
        return res



            

        