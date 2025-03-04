"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr = head

        dict1 = {None:None}

        while curr:
            copynode = Node(curr.val)
            dict1[curr] = copynode
            curr = curr.next

        curr = head
        while curr:

            dict1[curr].next = dict1[curr.next]
            dict1[curr].random = dict1[curr.random]
            curr = curr.next
        
        return dict1[head]




        