# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:  # Handle empty input
            return None
        
        while len(lists) > 1:
            merged = []

            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.twosortedlists(l1,l2))
            lists = merged
        
        return lists[0]

    def twosortedlists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to build the merged list
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next  # Move tail forward

        # Attach remaining nodes
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next  # Return the merged linked list