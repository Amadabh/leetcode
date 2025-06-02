# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        copy = head
        d = {}
        cnt =1
        while copy:
            d[cnt] = copy
            copy = copy.next
            cnt+=1
        # print(copy)
        n = cnt-1
        # print(d,ceil(n/2),n)
        for i in range(1,ceil(n//2) +1):
            first, last = d[i], d[n-i+1]
            firstNext = first.next
            # print(first.val,last.val,firstNext.val)
            
            first.next = last
            last.next = firstNext
            if i==ceil(n//2):
                firstNext.next = None
                break
                
        
        return head



        