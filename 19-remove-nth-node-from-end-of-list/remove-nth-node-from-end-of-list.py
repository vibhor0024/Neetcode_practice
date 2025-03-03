from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Find the size of the list
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        # Step 2: Find the target index (0-based)
        target = size - n

        # Step 3: If we need to remove the head
        if target == 0:
            return head.next

        # Step 4: Traverse to the (target-1)th node
        prev = None
        curr = head
        for i in range(target):  # Stop at the node before target
            prev = curr
            curr = curr.next

        # Step 5: Remove the target node
        if prev:
            prev.next = curr.next

        return head

        