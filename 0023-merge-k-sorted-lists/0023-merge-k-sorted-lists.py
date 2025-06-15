# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def sort(l1,l2):
            L = ListNode()
            dummy = L
            # print(l1,l2)

            while l1 and l2:
                # print(L.val)
                if l1.val<=l2.val:
                    L.next = ListNode(l1.val)
                    l1= l1.next
                else:
                    L.next = ListNode(l2.val)
                    l2 = l2.next
                L = L.next

            while l1:
                L.next = ListNode(l1.val)
                l1= l1.next
                L = L.next
               
            while l2:
                
                L.next = ListNode(l2.val)
                l2 = l2.next
                L = L.next
              
            return dummy.next
            

                


        def merge(l):
            if len(l)==1:
                return l[0]
            if len(l)==0:
                return
            n = len(l)
            left = merge(l[:n//2])
            right = merge(l[n//2:])
            if not left: return right
            if not right: return left

            res = sort(left,right)
            return res
        return merge(lists)
            
        