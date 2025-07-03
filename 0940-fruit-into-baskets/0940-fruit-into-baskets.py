class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        cnt=0
        d = defaultdict(int)
        l=0
        ans =0
        for r in range(n):
            if fruits[r] not in d:
                cnt+=1
            while cnt>2 and l<r:
                d[fruits[l]]-=1
                if d[fruits[l]]==0:
                    cnt-=1
                    del d[fruits[l]]
                l+=1

            d[fruits[r]]+=1
           
            
            ans = max(r-l+1,ans)
            print(r,l,ans)
        return ans

        