class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for i in nums:
            d[i]+=1
        freq_val = defaultdict(list)
        for key,cnt in d.items():
            freq_val[cnt].append(key)
        n = len(nums)
        ans =[]
     
        for i in range(n,-1,-1):
            if k==0:
                break

            print("i",i)
            if i in freq_val:
                print(freq_val)
                for val in freq_val[i]:
                    ans.append(val)
                    k-=1
                    if k==0:
                        break
                  
            
        return ans

        # d = defaultdict(int)
        # for i in nums:
        #     d[i]+=1
        # heap =[ (-val, key) for key,val in d.items()]

        # heapq.heapify(heap)
        # cnt=0
        # ans =[]
        # while cnt<k:
        #     val, key = heapq.heappop(heap)
        #     ans.append(key)
        #     cnt+=1
        # return ans
        