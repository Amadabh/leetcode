# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #brute force
        cur = head
        total =0
        while cur:
            total+=1
            cur = cur.next
        find = total - n
        # print(find)
        if find==0:
            return head.next
        dummy = head
        while dummy:
            if find==1:
                dummy.next = dummy.next.next
            find-=1
            dummy = dummy.next
        return head
            
            
        