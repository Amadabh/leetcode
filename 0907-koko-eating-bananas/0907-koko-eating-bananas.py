class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Optimized 
        piles.sort()
        maxi = piles[-1]
        ans = 0
        l,r = 1, maxi

        def checkValidK(k):
            cnt = 0
            for num in piles:
                cnt+= math.ceil(num/k)
            if cnt<=h:
                return True
            return False

        while l<=r:
            mid = (l+r)//2
            # print(mid)
            if checkValidK(mid):
                r = mid-1
            else:
                l = mid+1
        return l
        # Bruteforce
        # piles.sort()
        # maxi = piles[-1]
        # ans =0
        # for k in range(1,maxi+1):
        #     cnt = 0
        #     for num in piles:
        #         cnt+= math.ceil(num/k)
        #     # print(cnt)
        #     if cnt<=h:
        #         ans = k
        #         break
        # return ans

        