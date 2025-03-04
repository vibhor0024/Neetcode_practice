# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        x = 1
        n1, n2 = 0, 0
        while l1:
            n1 += l1.val*x
            x *= 10
            l1 = l1.next
        x = 1
        while l2:
            n2 += l2.val*x
            x *= 10
            l2 = l2.next
        
        res = n1 + n2

        digits = len(str(abs(res)))

        head = ListNode(res//(10**(digits-1)))
        res -= (res//(10**(digits-1)))*(10**(digits-1))
        digits -= 1
        curr = head
        while digits:

            curr.next = ListNode(res//(10**(digits-1)))
            res -= (res//(10**(digits-1)))*(10**(digits-1))
            digits -= 1
            curr = curr.next
        
        curr.next = None

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
        

        




            





        