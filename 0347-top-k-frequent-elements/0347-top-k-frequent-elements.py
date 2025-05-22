class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        heap =[ (-val, key) for key,val in d.items()]

        heapq.heapify(heap)
        cnt=0
        ans =[]
        while cnt<k:
            val, key = heapq.heappop(heap)
            ans.append(key)
            cnt+=1
        return ans
        