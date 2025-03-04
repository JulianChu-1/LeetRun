from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        length = 0
        while head:
            length += 1
            head = head.next
        
        cur = dummy

        for i in range(1, length + 1 - n):
            cur = cur.next
        
        cur.next = cur.next.next

        return dummy.next
