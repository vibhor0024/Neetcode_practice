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
            newl = self.twosortedlists(lists[0], lists[1])  # Merge first two lists
            del lists[0:2]  # Remove merged lists
            lists.insert(0, newl)  # Insert the merged list at the beginning

        return lists[0]   # Return the final merged list

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