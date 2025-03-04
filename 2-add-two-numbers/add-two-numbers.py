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

        head = ListNode(res%10)
        res = res // 10
        curr = head
        while res:
            curr.next = ListNode(res%10)
            res = res//10
            curr = curr.next
        

        return head

       
        

        




            





        