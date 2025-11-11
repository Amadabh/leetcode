class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        n = len(intervals)
        pos ={}
        for i in range(n):
            pos[tuple(intervals[i])] = i
            ans.append(0)
        
        arr = sorted(intervals, key = lambda x: x[0])
        # print(arr)
        for i in range(n):
            m = float("inf")
            ind = -1
            for j in range(i,n):
                # print(intervals[j])
                if arr[i][1] <= arr[j][0]:
                    # print(intervals[i][1], intervals[j][0])
                    ind = pos[tuple(arr[j])]
                    break

            ans[pos[tuple( arr[i] ) ]] = ind
        return ans

        # ans = []
        # for i in range(n):
        #     m = float("inf")
        #     ind = -1
        #     for j in range(i+1,n):
        #         if intervals[i][1] <= intervals[j][0]:
        #             if m>intervals[j][0]:
        #                 ind = j
        #     ans.append(ind)
        # return ans
                    