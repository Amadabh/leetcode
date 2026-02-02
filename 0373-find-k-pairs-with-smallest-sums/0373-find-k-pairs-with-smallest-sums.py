class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap =[]
        heapq.heapify(heap)
        n, m = len(nums1), len(nums2)
        n1, n2 = nums1, nums2

        for i in range(n):
            s = n1[i] + n2[0]
            heapq.heappush(heap, (s, i , 0))
        res = []
        while k> 0 and heap:
            _, i , j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
      
            if j+1 < m:
                s = n1[i] + n2[j+1]
                heapq.heappush(heap, (s, i , j + 1))
            k -= 1
        return res
            


        
