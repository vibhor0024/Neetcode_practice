# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        dummy = ListNode(0,head)
        groupprev = dummy

        while True:
            kth = self.getkth(groupprev,k)
            if not kth:
                break
            groupnext = kth.next
            prev = kth.next
            curr = groupprev.next

            while curr != groupnext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            tmp = groupprev.next
            groupprev.next = kth
            groupprev = tmp
        
        return dummy.next


        
    


    def getkth(self,node,k):
        while node and k >0:
            node = node.next
            k -= 1
        return node