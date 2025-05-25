class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0,n-1
        area = min(height[l],height[r]) * (r-l)
        maxarea = area
        while l<r:
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
            area = min(height[l],height[r]) * (r-l)
            maxarea = max(area,maxarea)
        return maxarea
            
        #brute force
        # n = len(height)
        # maxarea = 0
        # for l in range(n):
        #     for r in range(l+1,n):
        #         area = min(height[l],height[r]) * (r-l)
        #         maxarea = max(area,maxarea)
        # return maxarea

        