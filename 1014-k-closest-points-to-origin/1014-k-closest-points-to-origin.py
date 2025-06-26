class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap =[]
        heapq.heapify(heap)
        for i in points:
            a,b = i
            d = sqrt(a**2 + b**2)
            if len(heap)<k:
                heapq.heappush(heap,(-1 * d,[a,b]))
            elif len(heap)==k:
                d2,arr = heapq.heappop(heap)
                # print(arr,[a,b] , d, d2)
                if d< -1 * d2:
                    heapq.heappush(heap,(-1 * d,[a,b]))
                else:
                    heapq.heappush(heap,(d2,arr))
        l =[]
        while heap:
            d, arr = heapq.heappop(heap)
            l.append(arr)
        return l
        

        