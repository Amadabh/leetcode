class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        n = len(nums)
        arr = nums
        for i in range(n):
            
            if dq and dq[0]<=i-k:
                dq.popleft()
            while dq and arr[dq[-1]]<arr[i]:
                dq.pop()
            dq.append(i)
            
            if i>=k-1 and dq:
                res.append(arr[dq[0]])
        return res

        

        
        
