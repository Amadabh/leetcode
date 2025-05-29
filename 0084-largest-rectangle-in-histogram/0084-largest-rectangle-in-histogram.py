class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #stack
        n = len(heights)
        st = []
        maxArea = 0
        for ind,height in enumerate(heights):
            start = ind

            while st and st[-1][1]>height:
                pind, pheight = st.pop()
                maxArea = max((ind - pind) * pheight, maxArea)
                # print(maxArea, (ind - pind), pheight)
                start = pind


            st.append((start, height))
        print(st)
        while st:
            ind,height = st.pop()
            maxArea = max((n - ind) * height, maxArea)



        return maxArea

        #Bruteforce
        # n = len(heights)
        # maxArea = 0

        # for ind in range(n):
        #     leftmost= rightmost = ind

        #     while leftmost>=0 and heights[leftmost]>=heights[ind]:
        #         leftmost-=1
            
        #     while rightmost<n and heights[rightmost]>=heights[ind]:
        #         rightmost+=1
        #     rightmost-=1
        #     leftmost+=1
        #     print(rightmost,leftmost)
        #     maxArea = max((rightmost - leftmost + 1 ) * heights[ind], maxArea)
        # return maxArea


        