class MedianFinder:

    def __init__(self):
        self.sm_heap, self.bg_heap = [] , []
        heapq.heapify(self.sm_heap)
        heapq.heapify(self.bg_heap)
        self.cnt = 0

        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.sm_heap, -num)
        heapq.heappush(self.bg_heap, -heapq.heappop(self.sm_heap))

        if len(self.bg_heap) > len(self.sm_heap):
            heapq.heappush(self.sm_heap, -heapq.heappop(self.bg_heap))

        self.cnt += 1
            

    def findMedian(self) -> float:
        if self.cnt % 2 == 0:
            # print(self.
            return ((-1 * self.sm_heap[0]) + self.bg_heap[0]) / 2
        else:
            # print(self.sm_heap, self.bg_heap, " " , float(-1 * self.sm_heap[0]))
            return float(-1 * self.sm_heap[0])

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()sm_heap, self.bg_heap, " ", ((-1 * self.sm_heap[0]) + self.bg_heap[0]) / 2)