from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()

        while head:
            if head in visited:
                return head
            else:
                visited.add(head)
            head = head.next
            
        return None